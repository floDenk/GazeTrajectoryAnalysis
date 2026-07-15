# EQUGAT Algorithm Implementation

Implementation of the EQUGAT algorithm described in 
> Denk, F., Fröhling, F., Brunner, P., Huber, W., Margreiter, M., Bogenberger, K., & Kates, R. (2025). Influence of gaze strategies and cognitive load on safeguarding performance of motorists in right-turning scenarios involving potential conflicts with vulnerable road users. *Transportation Research Part F: Traffic Psychology and Behaviour*, 109, 32–49. https://doi.org/10.1016/j.trf.2024.11.012 (Open Access).

EQUGAT estimates when — and how likely — a car driver would perceive a virtual cyclist at an intersection, given the driver's recorded gaze trajectories. For each gaze trajectory, a population of virtual cyclists is sampled across a grid of velocities and initial positions. The algorithm then steps through each recorded timestep, checks whether any virtual cyclist falls within the driver's visible field of view (determined by which gaze region the driver was looking at, accounting for occlusion), and records the moment of first perception. The result is a probabilistic map of perception events that can be weighted by realistic cyclist speed distributions.

---

## Algorithm Overview

1. **Road geometry**: The `.xodr` file is parsed to extract the car route and cycling route as polylines, and any static occlusion objects (e.g. buildings at intersections).
2. **FOV precomputation**: For every position along the car route, and for every named gaze region (AOI), the corresponding field-of-view polygon is rotated and translated into world coordinates and clipped against occluding objects. Results are cached on disk.
3. **Cyclist sampling**: A grid of virtual cyclist scenarios is created by combining a range of approach velocities with a range of initial position offsets along the cycling track. Each combination is weighted by a truncated normal speed distribution and a uniform position distribution.
4. **Perception loop**: For each recorded trajectory and each timestep, the algorithm:
   - Determines which gaze region the driver was looking at.
   - Looks up the precomputed FOV polygon for that gaze region at the driver's current road position.
   - Advances all virtual cyclist positions by one timestep.
   - Identifies which cyclists (not yet perceived) now fall within the visible segment of the cycling track.
   - Records the car's road position and elapsed time at the moment of first perception for each cyclist.
5. **Output**: A per-trajectory, per-cyclist-sample table of perception events.

---

## Installation

Requires Python 3.10+. Create and activate a virtual environment, then install the project into it from the repository root:

```bash
python -m venv .venv

# activate it
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux

pip install .
```

or, for an editable install while developing:

```bash
pip install -e .
```

This installs the following Python dependencies (see `pyproject.toml`):

| Package | Version tested |
|---|---|
| `pandas` | 2.3.3 |
| `numpy` | 2.0.2 |
| `scipy` | 1.15.3 |
| `shapely` | 2.0.6 |
| `matplotlib` | 3.9.3 |
| `xsdata` | 24.11 — OpenDRIVE XML parsing |
| `pyarrow` | 20.0.0 — Feather file I/O |
| `cairosvg` | 2.9.0 — SVG rendering for car/cyclist icons |

In addition, the `odrplot` command-line tool must be on `PATH`; it is used to sample the OpenDRIVE geometry at fixed arc-length intervals. It is part of [esmini](https://github.com/esmini/esmini) — install esmini and ensure its `bin` folder (containing `odrplot`) is on `PATH`. Tested version of esmini: v2.45.3.

---

## Input Data

### Gaze Database Folder

The primary input is a folder (the *gaze database*) that must contain the following files:

| File | Description |
|---|---|
| `geometry.xodr` | OpenDRIVE road network file defining all roads, lanes, and static objects at the scenario location |
| `aoi_config.json` | Named gaze regions (Areas of Interest) defined as polygons in the car's local coordinate frame |
| `gazes_spatiotemporal.feather` | Recorded gaze data (see schema below) |
| `top_view.png` | *(optional)* Aerial/map image used as plot background when `show_top_view_image=True` |

#### `gazes_spatiotemporal.feather` Schema

An Apache Feather file where each row is one timestep of one recorded drive:

| Column | Type | Description |
|---|---|---|
| `trajectory_id` | int / str | Unique identifier grouping rows into individual drives |
| `t` | float | Elapsed time within the trajectory (seconds) |
| `s_driver` | float | Position of the car along the road (metres) |
| `v` | float | Car speed at this timestep (m/s) |
| `gaze_state` | str | Name of the AOI the driver was looking at (must match a name in `aoi_config.json`) |
| `gaze_id` | int | Numeric identifier of the individual gaze event |

Rows within a trajectory must be sorted by `t` and sampled at a **constant** time step.

#### `aoi_config.json` Format

Defines the field-of-view polygons for each named gaze region in the **car's local coordinate frame** (origin at the driver's eye point, x forward, y left).

```json
{
  "aoi_id": "urban_right_turn",
  "aois": [
    {
      "name": "road_ahead",
      "coords": [[0, -2], [40, -5], [40, 5], [0, 2]],
      "color": "tab:blue",
      "alpha": 0.4
    },
    {
      "name": "right_mirror",
      "coords": [[0, -2], [15, -15], [25, -15], [10, -1]],
      "color": "tab:orange",
      "alpha": 0.4
    }
  ]
}
```

| Field | Description |
|---|---|
| `aoi_id` | Identifier string for this AOI configuration |
| `aois[].name` | Must match the values that appear in `gaze_state` in the gaze data |
| `aois[].coords` | List of `[x, y]` vertices defining the FOV polygon in local car coordinates (metres), Polygon must start at (0,0), which is the reference point for the driver in the car|
| `aois[].color` | Matplotlib color string used in visualisations |
| `aois[].alpha` | Polygon fill transparency (0–1) used in visualisations |

### Virtual Cyclist Configuration File

A JSON file that describes the population of virtual cyclists to be simulated. The default values are based on Statista cycling speed statistics.

```json
{
  "v_min":    5.0,
  "v_max":    9.0,
  "v_mean":   6.233,
  "v_stddev": 1.0,
  "v_step":   1.0,
  "s_step":   25.0
}
```

| Field | Unit | Description |
|---|---|---|
| `v_min` | m/s | Minimum cyclist speed in the sampling grid |
| `v_max` | m/s | Maximum cyclist speed in the sampling grid |
| `v_mean` | m/s | Mean of the truncated normal speed distribution used for probability weighting |
| `v_stddev` | m/s | Standard deviation of the speed distribution |
| `v_step` | m/s | Velocity grid resolution |
| `s_step` | m | Position-offset grid resolution |

Finer grids produce more accurate probability estimates but increase runtime proportionally.

---

## API Reference

### `equgat(gaze_db_path, carRoadIDs, cyclingRoadIDs, plotON, ...)`

The single entry point of the algorithm.

#### Required Parameters

| Parameter | Type | Description |
|---|---|---|
| `gaze_db_path` | `str` | Absolute or relative path to the gaze database folder |
| `carRoadIDs` | `list[int]` | Ordered list of OpenDRIVE road IDs that make up the car route. Roads are concatenated in the given order, so the IDs must be in traversal sequence. |
| `cyclingRoadIDs` | `list[int]` | Ordered list of OpenDRIVE road IDs that make up the cycling route |
| `plotON` | `bool` | Enable frame-by-frame visualisation. Set to `False` for batch processing — much faster and outputs the resulting perception events to a Feather file. |

#### Optional Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `trajectory_ids` | `list` or `None` | `None` | Process only the specified trajectory IDs. `None` processes all trajectories in the gaze database. |
| `s_driver_range` | `tuple(float, float)` or `None` | `None` | Only keep gaze rows whose `s_driver` falls within `(min, max)` (metres). |
| `trajectory_filter` | `callable` or `None` | `None` | Arbitrary row filter for the loaded gaze dataframe. Called as `trajectory_filter(df)` and must return a boolean mask aligned to `df`'s index; only matching rows are kept. E.g. keep only trajectories that never exceed 20 km/h: `trajectory_filter=lambda df: df.groupby('trajectory_id')['v'].transform('max') < (20 / 3.6)`. |
| `show_gaze_aoi` | `bool` | `True` | Whether to draw the driver's current gaze FOV/AOI polygon overlay in the plot. |
| `show_top_view_image` | `bool` | `False` | Overlay the `top_view.png` aerial image as a plot background. Requires `top_view.png` to be present in the gaze database folder and the four coordinate bounds to be set. |
| `top_view_xmin` | `float` | `None` | World x-coordinate corresponding to the left edge of `top_view.png` |
| `top_view_xmax` | `float` | `None` | World x-coordinate corresponding to the right edge of `top_view.png` |
| `top_view_ymin` | `float` | `None` | World y-coordinate corresponding to the bottom edge of `top_view.png` |
| `top_view_ymax` | `float` | `None` | World y-coordinate corresponding to the top edge of `top_view.png` |
| `cyclist_sampling_config_file` | `str` or `None` | `None` | Path to the virtual cyclist JSON configuration file. Required when `only_visualize_gaze_trajectory=False`. |
| `video_path` | `str` or `None` | `None` | If set, saves the animation to this file path instead of displaying it interactively. Supported extensions: `.mp4` (requires ffmpeg) and `.gif`. When multiple trajectories are processed, the trajectory ID is automatically appended to the filename (e.g. `trajectory_5692.mp4`). |
| `animation_fps` | `float` or `None` | `None` | Frames per second for saved video. Defaults to the data sampling rate divided by `PLOT_STEP` (every 4th frame is rendered), so a 100 Hz dataset produces ~25 fps video. |
| `video_dpi` | `int` | `150` | Resolution in dots-per-inch for saved video frames. |
| `only_visualize_gaze_trajectory` | `bool` | `False` | Skip cyclist sampling entirely and only visualise the car's gaze trajectory overlaid on the road geometry. Useful for inspecting the raw gaze data before running the full algorithm. |

---

## Output

### When `plotON=False` (batch mode)

The algorithm writes a single file:

**`output/time_to_perception_event.feather`** — Apache Feather format, one row per virtual cyclist sample per trajectory.

| Column | Type | Description |
|---|---|---|
| `trajectory_id` | int / str | Source trajectory |
| `s_cyclist` | float | Cyclist's position along cycling track (m) |
| `v_cyclist` | float | Cyclist speed (m/s) |
| `s_offset` | float | Initial position offset of the cyclist along the cycling track (m) |
| `drelCyclist` | float | Relative distance between car and cyclist along their respective tracks at end of trajectory (m) |
| `cyclist_probability` | float | Joint probability weight of this cyclist sample (velocity × position distribution) |
| `sCarAtPerception` | float | Car's position along its route at the moment of first perception (m). 0 if never perceived. |
| `tCarAtPerception` | float | Elapsed time at the moment of first perception (s). 0 if never perceived. |
| `sCyclistAtPerception` | float | Cyclist's position along cycling track at moment of perception (m). 0 if never perceived. |
| `carDriverSawCyclist` | int | 1 if the cyclist was perceived at any point during the trajectory, 0 otherwise |
| `whichGazeCategorySawCyclist` | str or None | Name of the AOI (gaze region) through which the cyclist was first perceived |
| `whichGazeIDSawCyclist` | int | Gaze ID during which perception occurred |

### When `plotON=True`

An interactive matplotlib animation is shown step by step. The plot displays, depending on chosen plotting parameters:
- Car route and cycling route polylines
- The car icon at its current position, oriented to the road heading
- The active FOV polygon (coloured by gaze region) with occlusion clipping applied
- The intersection of the FOV polygon with the cycling track (the visible segment)
- Virtual cyclist icons: red for cyclists not yet perceived, green for cyclists already perceived
- Optionally, the aerial top-view image as background

---

## Caching

FOV polygon precomputation is the most expensive step. Results are cached automatically in the `cache/` directory as `<geometry_filename>.fov_cache.pkl`. On subsequent runs, the cache is reused if both the `.xodr` file name and the AOI configuration are unchanged. If either changes, the cache is invalidated and recomputed.

Delete or clear the `cache/` folder to force recomputation (e.g. after modifying road geometry or AOI definitions without changing the filename).

---

## Limitations

- **OpenDRIVE support is limited to simple `.xodr` files without subdivided lane sections.** Roads with multiple `<laneSection>` entries (e.g. lanes that split, merge, or change width partway along a road) are not supported by the geometry parser at the moment.

---

## Funding

This work was supported by the Technische Hochschule Ingolstadt and the European Union within the Horizon Europe programme under Grant No. 101075068 (V4SAFETY).

---

## Project Structure

```
equgat_algorithm_implementation/
├── equgat.py                        # Main algorithm entry point
├── input/
│   └── virtual_cyclist_config.json  # Default cyclist population config
├── output/                          # Algorithm results written here
├── cache/                           # Auto-generated FOV polygon cache
└── util/
    ├── config.py                    # Data classes: GazeDatabase, AoiConfig, CyclistSamplingConfig
    ├── geometry.py                  # Visibility / occlusion polygon computation
    ├── plot.py                      # Matplotlib plotting helpers
    ├── xodr.py                      # OpenDRIVE geometry import and occlusion object extraction
    ├── xodr_xml_parser.py           # Auto-generated OpenDRIVE XML schema bindings
    ├── car.svg                      # Car icon used in visualisations
    ├── cyclist_red.svg              # Cyclist icon (not yet perceived)
    └── cyclist_green.svg            # Cyclist icon (perceived)
```
