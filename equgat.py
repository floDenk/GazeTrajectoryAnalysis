import hashlib
import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import truncnorm
from shapely import affinity, intersection
from shapely.geometry import LineString, MultiLineString, Polygon

from util.config import CyclistSamplingConfig, GazeDatabase
from util.geometry import build_lane, compute_visibility, find_s_coverage_for_geometry
from util.plot import PLOT_STEP, TopViewImage, _load_svg, plot, plot_shapely_objects
from util.xodr import get_occlusion_object_from_xodr, import_xodr


def calc_which_cyclists_visible(df, fov, fov_s_coverage_cycling_track_now):
    cyclist_half_length = 1.0  # meters from center point
    for tuple in fov_s_coverage_cycling_track_now:
        s_start, s_end = tuple
        df.loc[  (df['s_cyclist'] > (s_start - cyclist_half_length))
               & (df['s_cyclist'] < (s_end + cyclist_half_length)), 'cyclistWasInSight'] = 1

def equgat(
    
    # --- Input / Data ---
    gaze_db_path: str,
    car_road_ids: list,
    cycling_road_ids: list,
    trajectory_ids=None,
    s_driver_range=None,
    trajectory_filter=None,
    cyclist_sampling_config_file=None,
    
    # --- Visualization ---
    plot_on=False,
    only_visualize_gaze_trajectory=False,
    plot_aois=False,
    show_gaze_aoi=True,
    plot_car_lane=True,
    plot_cycling_lane=True,
    view_box=(-100, 200, -50, 50),
    transparent_bg=False,
    show_top_view_image=False,
    top_view_offset=(0.0, 0.0),
    top_view_scale=1.0,
    use_simple_object_shapes=True,
    
    # --- Video output ---
    video_path=None,
    animation_fps=None,
    video_dpi=150,
):
    gaze_db = GazeDatabase(gaze_db_path)
    gaze_db.validate()
    xodr_file_location = gaze_db.xodr_path

    df_all = gaze_db.load_gazes()
    if trajectory_ids is not None:
        df_all = df_all[df_all['trajectory_id'].isin(trajectory_ids)]
    if s_driver_range is not None:
        s_driver_min, s_driver_max = s_driver_range
        df_all = df_all[df_all['s_driver'].between(s_driver_min, s_driver_max)]
    if trajectory_filter is not None:
        df_all = df_all[trajectory_filter(df_all)]
    if df_all.empty:
        raise ValueError("No trajectories found for the given trajectory_ids/s_driver_range/trajectory_filter.")

    # reset index to ensure uniqueness starting from 0, which simplifies the data mapping in the loop
    df_gaze_spatiotemp = df_all.reset_index(drop=True)
    col_s_driver  = df_gaze_spatiotemp.columns.get_loc('s_driver')
    col_v         = df_gaze_spatiotemp.columns.get_loc('v')
    col_gazeState = df_gaze_spatiotemp.columns.get_loc('gaze_state')
    col_gazeID    = df_gaze_spatiotemp.columns.get_loc('gaze_id')

    if df_gaze_spatiotemp.index.nunique() != df_gaze_spatiotemp.shape[0]:
        raise ValueError("Index is not unique and will cause problems in the mapping of data!")

    # get time step from data frame, assuming that it is constant
    tStep = df_gaze_spatiotemp.loc[1, 't'] - df_gaze_spatiotemp.loc[0, 't']
    if animation_fps is None:
        animation_fps = 1.0 / (PLOT_STEP * tStep)

    df_time_to_perception = pd.DataFrame()

    #region create car and cycling track
    ref_x, ref_y, s, psi = import_xodr(xodr_file_location)

    s_lane_car,     x_lane_car,     y_lane_car,     psi_lane_car, car_track     = build_lane(car_road_ids,     ref_x, ref_y, s, psi)
    s_lane_cyclist, x_lane_cyclist, y_lane_cyclist, _,            cycling_track = build_lane(cycling_road_ids, ref_x, ref_y, s, psi)

    top_view_image   = TopViewImage(gaze_db.top_view_path, offset=top_view_offset, scale=top_view_scale) \
                       if show_top_view_image else None
    occlusion_object = get_occlusion_object_from_xodr(xodr_file_location, s_lane_car, x_lane_car, y_lane_car, psi_lane_car)

    car_img = None if use_simple_object_shapes else _load_svg('util/car.svg')
    if not only_visualize_gaze_trajectory:
        cyclist_img_unseen = None if use_simple_object_shapes else _load_svg('util/cyclist_red.svg')
        cyclist_img_seen   = None if use_simple_object_shapes else _load_svg('util/cyclist_green.svg')
    #endregion

    #region create FOV polygons for AOIs
    aoi_config = gaze_db.load_aoi_config()
    fov_dict   = aoi_config.to_fov_dict()
    aoi_colors = aoi_config.color_dict()
    aoi_alphas = aoi_config.alpha_dict()

    if plot_on and plot_aois:
        fig, ax = plt.subplots(1, 1)
        plot_shapely_objects(ax, list(fov_dict.values()),
                             colors=[a.color for a in aoi_config.aois],
                             alphas=[a.alpha for a in aoi_config.aois],
                             labels=list(fov_dict.keys()))
    #endregion

    _lane_shapes = ([car_track]     if plot_car_lane    else []) + \
                   ([cycling_track] if plot_cycling_lane else [])
    _lane_colors = ([None] if plot_car_lane    else []) + \
                   ([None] if plot_cycling_lane else [])
    _lane_alphas = _lane_colors[:]

    #region precompute all possible FOVs — load from cache if xodr file, AOI config, and road data match
    def _array_hash(arr):
        return hashlib.md5(np.ascontiguousarray(arr)).hexdigest()


    os.makedirs('cache', exist_ok=True)
    cache_path = 'cache/' + os.path.basename(xodr_file_location) + '.fov_cache.pkl'
    
    cache_hit = False
    if os.path.isfile(cache_path):
        with open(cache_path, 'rb') as f:
            cache = pickle.load(f)
        if (cache['fov_dict'] == fov_dict
                and cache.get('ref_x') == ref_x
                and cache.get('ref_y') == ref_y
                and cache.get('s')     == s
                and cache.get('psi')   == psi):
            fov_dict_polygons           = cache['fov_dict_polygons']
            intersections_cycling_track = cache['intersections_cycling_track']
            fov_s_coverage_cycling_track = cache['fov_s_coverage_cycling_track']
            cache_hit = True
            print("Loaded precomputed FOV polygons from cache.")
        else:
            print("Cache mismatch (xodr file, AOI config, or road reference data changed) — recomputing.")

    if not cache_hit:
        print("Precomputing FOV polygons for all AOIs and all time steps...")
        
        fov_dict_polygons            = {aoi: np.zeros(len(s_lane_car), dtype=Polygon) for aoi in fov_dict}
        intersections_cycling_track  = {aoi: np.zeros(len(s_lane_car), dtype=Polygon) for aoi in fov_dict}
        fov_s_coverage_cycling_track = {aoi: np.empty(len(s_lane_car), dtype=object) for aoi in fov_dict}

        fig, ax = plt.subplots()
        
        for idx in range(len(s_lane_car)):
            for aoi in fov_dict.keys():
                fov_dict_polygons[aoi][idx] = affinity.translate(
                    affinity.rotate(fov_dict[aoi], np.rad2deg(psi_lane_car[idx]), (0, 0)),
                    x_lane_car[idx], y_lane_car[idx])
                if occlusion_object is not None:
                    fov_dict_polygons[aoi][idx] = compute_visibility(fov_dict_polygons[aoi][idx], occlusion_object)

                
                _aoi_shapes = [fov_dict_polygons[aoi][idx]] if show_gaze_aoi else []
                _aoi_colors_now = [aoi_colors[aoi]] if show_gaze_aoi else []
                _aoi_alphas_now = [aoi_alphas[aoi]] if show_gaze_aoi else []
                plot(idx, fig, ax, aoi,tStep,
                        _lane_shapes + _aoi_shapes + [occlusion_object],
                        top_view_image=top_view_image,
                        car_img=car_img, car_x=x_lane_car[idx],
                        car_y=y_lane_car[idx], car_angle_deg=np.rad2deg(psi_lane_car[idx]),
                        shapely_colors=_lane_colors + _aoi_colors_now + [None],
                        shapely_alphas=_lane_alphas + _aoi_alphas_now + [None],
                        view_box=view_box, transparent_bg=transparent_bg)

                intersections_cycling_track[aoi][idx] = intersection(fov_dict_polygons[aoi][idx], cycling_track)
                
                fov_s_coverage_cycling_track[aoi][idx] = find_s_coverage_for_geometry(
                    intersections_cycling_track[aoi][idx], x_lane_cyclist, y_lane_cyclist, s_lane_cyclist
                )

        with open(cache_path, 'wb') as f:
            pickle.dump({'fov_dict': fov_dict,
                         'ref_x': ref_x, 'ref_y': ref_y,
                         's': s, 'psi': psi,
                         'fov_dict_polygons': fov_dict_polygons,
                         'intersections_cycling_track': intersections_cycling_track,
                         'fov_s_coverage_cycling_track': fov_s_coverage_cycling_track}, f)
        print(f"Saved precomputed FOV polygons to cache: {cache_path}")
    #endregion

    if not only_visualize_gaze_trajectory:
        cfg = CyclistSamplingConfig.from_json(cyclist_sampling_config_file)

    for idx_traj, trajectory_id in enumerate(df_gaze_spatiotemp['trajectory_id'].unique()):
        print(f"processing trajectory_id: {trajectory_id} "
              f"({idx_traj + 1}/{len(df_gaze_spatiotemp['trajectory_id'].unique())})")

        idx_this_trajectory_id = df_gaze_spatiotemp.index[df_gaze_spatiotemp['trajectory_id'] == trajectory_id]
        t_length_trajectory = len(idx_this_trajectory_id) * tStep

        if not only_visualize_gaze_trajectory:
            v_cyclist  = np.arange(cfg.v_min, cfg.v_max, step=cfg.v_step)
            N_velocity = len(v_cyclist)

            s_offset_max = cfg.v_max * t_length_trajectory
            s_offset  = np.arange(-s_offset_max, s_offset_max, step=cfg.s_step)
            N_soffset = len(s_offset)

            v_cyclist_grid = np.repeat(v_cyclist, N_soffset)
            s_offset_grid  = np.tile(s_offset, N_velocity)

            N_cyclist_samples_all = N_velocity * N_soffset

            a = (cfg.v_min - cfg.v_mean) / cfg.v_stddev
            b = (cfg.v_max - cfg.v_mean) / cfg.v_stddev
            v_cyclist_rv    = truncnorm(a, b, loc=cfg.v_mean, scale=cfg.v_stddev)
            gewichtung_grid = (v_cyclist_rv.pdf(v_cyclist_grid) * cfg.v_step) * \
                              (np.ones(N_cyclist_samples_all) * (1 / s_offset_max) * cfg.s_step)

            N_cyclist_samples = len(v_cyclist_grid)

            df_gaze_sees_cyclist = pd.DataFrame({
                'trajectory_id':               np.repeat(trajectory_id, N_cyclist_samples),
                's_cyclist':                   s_offset_grid,
                'v_cyclist':                   v_cyclist_grid,
                's_offset':                    s_offset_grid,
                'drelCyclist':                 s_offset_grid,
                'cyclist_probability':         gewichtung_grid,
                'sCarAtPerception':            np.zeros(N_cyclist_samples),
                'tCarAtPerception':            np.zeros(N_cyclist_samples),
                'sCyclistAtPerception':        np.zeros(N_cyclist_samples),
                'carDriverSawCyclist':         np.zeros(N_cyclist_samples),
                'whichGazeCategorySawCyclist': np.repeat(None, N_cyclist_samples),
                'whichGazeIDSawCyclist':       np.zeros(N_cyclist_samples),
                'cyclistWasInSight':           np.zeros(N_cyclist_samples),
            })

            col_sCyclist                    = df_gaze_sees_cyclist.columns.get_loc('s_cyclist')
            col_drelCyclist                 = df_gaze_sees_cyclist.columns.get_loc('drelCyclist')
            col_vCyclist                    = df_gaze_sees_cyclist.columns.get_loc('v_cyclist')
            col_cyclistWasInSight           = df_gaze_sees_cyclist.columns.get_loc('cyclistWasInSight')
            col_sCarAtPerception            = df_gaze_sees_cyclist.columns.get_loc('sCarAtPerception')
            col_tCarAtPerception            = df_gaze_sees_cyclist.columns.get_loc('tCarAtPerception')
            col_carDriverSawCyclist         = df_gaze_sees_cyclist.columns.get_loc('carDriverSawCyclist')
            col_whichGazeCategorySawCyclist = df_gaze_sees_cyclist.columns.get_loc('whichGazeCategorySawCyclist')
            col_whichGazeIDSawCyclist       = df_gaze_sees_cyclist.columns.get_loc('whichGazeIDSawCyclist')

        if plot_on:
            fig, ax = plt.subplots()
            writer = None
            if video_path is not None:
                from pathlib import Path
                from matplotlib.animation import FFMpegWriter, PillowWriter
                p = Path(video_path)
                traj_path = str(p.parent / f"{p.stem}_{trajectory_id}{p.suffix}")
                writer = (PillowWriter(fps=animation_fps) if p.suffix.lower() == '.gif'
                          else FFMpegWriter(fps=animation_fps))
                writer.setup(fig, traj_path, dpi=video_dpi)

        for i, idx in enumerate(idx_this_trajectory_id):
            s_proband = df_gaze_spatiotemp.iat[idx, col_s_driver]
            closest_index_proband_lane = np.argmin(np.abs(s_lane_car - s_proband))

            gazeStateNow         = df_gaze_spatiotemp.iat[idx, col_gazeState]
            fov                  = fov_dict_polygons[gazeStateNow][closest_index_proband_lane]
            # intersection_cycling = intersections_cycling_track[gazeStateNow][closest_index_proband_lane]
            fov_s_coverage_cycling_track_now = fov_s_coverage_cycling_track[gazeStateNow][closest_index_proband_lane]

            if not only_visualize_gaze_trajectory:
                idx_cyclists_not_yet_seen = df_gaze_sees_cyclist.index[
                    df_gaze_sees_cyclist['carDriverSawCyclist'] == 0]

                t_proband = i * tStep
                vCar = df_gaze_spatiotemp.iat[idx, col_v]

                df_gaze_sees_cyclist.iloc[:, col_sCyclist]    += df_gaze_sees_cyclist.iloc[:, col_vCyclist] * tStep
                df_gaze_sees_cyclist.iloc[:, col_drelCyclist] += (df_gaze_sees_cyclist.iloc[:, col_vCyclist] - vCar) * tStep

                df_gaze_sees_cyclist.iloc[idx_cyclists_not_yet_seen, col_cyclistWasInSight] = 0
                gazeID = df_gaze_spatiotemp.iat[idx, col_gazeID]

                calc_which_cyclists_visible(df_gaze_sees_cyclist, fov, fov_s_coverage_cycling_track_now)

                idx_cyclists_now_seen = df_gaze_sees_cyclist.index[
                    (df_gaze_sees_cyclist['cyclistWasInSight'] == 1) &
                    (df_gaze_sees_cyclist['carDriverSawCyclist'] == 0)]

                df_gaze_sees_cyclist.iloc[idx_cyclists_now_seen, col_sCarAtPerception]            = s_proband
                df_gaze_sees_cyclist.iloc[idx_cyclists_now_seen, col_tCarAtPerception]            = t_proband
                df_gaze_sees_cyclist.iloc[idx_cyclists_now_seen, col_carDriverSawCyclist]         = 1
                df_gaze_sees_cyclist.iloc[idx_cyclists_now_seen, col_whichGazeCategorySawCyclist] = gazeStateNow
                df_gaze_sees_cyclist.iloc[idx_cyclists_now_seen, col_whichGazeIDSawCyclist]       = gazeID

            if plot_on:
                _gaze_aoi_shapes = [fov] if show_gaze_aoi else []
                _gaze_aoi_colors = [aoi_colors[gazeStateNow]] if show_gaze_aoi else []
                _gaze_aoi_alphas = [aoi_alphas[gazeStateNow]] if show_gaze_aoi else []
                plot(i, fig, ax, gazeStateNow,tStep,
                     _lane_shapes + _gaze_aoi_shapes + [occlusion_object],
                     top_view_image=top_view_image,
                     car_img=car_img,
                     car_x=x_lane_car[closest_index_proband_lane],
                     car_y=y_lane_car[closest_index_proband_lane],
                     car_angle_deg=np.rad2deg(psi_lane_car[closest_index_proband_lane]),
                     df=None if only_visualize_gaze_trajectory else df_gaze_sees_cyclist,
                     writer=writer,
                     shapely_colors=_lane_colors + _gaze_aoi_colors + [None],
                     shapely_alphas=_lane_alphas + _gaze_aoi_alphas + [None],
                     cyclist_img_unseen=None if only_visualize_gaze_trajectory else cyclist_img_unseen,
                     cyclist_img_seen=None if only_visualize_gaze_trajectory else cyclist_img_seen,
                     s_lane_cyclist=s_lane_cyclist, x_lane_cyclist=x_lane_cyclist, y_lane_cyclist=y_lane_cyclist,
                     view_box=view_box, transparent_bg=transparent_bg)
                if writer is not None and i % PLOT_STEP == 0:
                    total = len(idx_this_trajectory_id)
                    pct = 100 * i / total
                    print(f"\rSaving video {traj_path}: frame {i}/{total} ({pct:.0f}%)", end='', flush=True)

        if plot_on:
            if writer is not None:
                print(f"\rSaving video {traj_path}: done ({len(idx_this_trajectory_id)} frames)        ")
                writer.finish()
            plt.close()

        if not only_visualize_gaze_trajectory:
            df_time_to_perception = pd.concat([df_time_to_perception, df_gaze_sees_cyclist], ignore_index=True)

    #region save data to files
    if not only_visualize_gaze_trajectory:
        df_time_to_perception.drop('cyclistWasInSight', axis=1, inplace=True)

        if not plot_on:
            os.makedirs('output', exist_ok=True)
            df_time_to_perception.to_feather('output/time_to_perception_event.feather')
    #endregion
