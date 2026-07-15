import json
import os
from dataclasses import dataclass, asdict
from shapely.geometry import Polygon


@dataclass
class CyclistSamplingConfig:
    v_min: float = 3.0        # m/s  (≈ 9.7 km/h)
    v_max: float = 9.0        # m/s  (≈ 33.1 km/h)
    v_mean: float = 6.233     # m/s  (22.44 km/h, Statista)
    v_stddev: float = 1.0     # m/s  (3.6 km/h, Statista)
    v_step: float = 0.2       # m/s  velocity grid resolution
    s_step: float = 0.5       # m    position-offset grid resolution

    @classmethod
    def from_json(cls, path: str) -> 'CyclistSamplingConfig':
        with open(path) as f:
            return cls(**json.load(f))

    def to_json(self, path: str) -> None:
        with open(path, 'w') as f:
            json.dump(asdict(self), f, indent=4)


@dataclass
class AoiPolygon:
    name: str
    coords: list          # list of [x, y] pairs
    color: str = 'tab:blue'
    alpha: float = 0.4

    def to_polygon(self) -> Polygon:
        return Polygon(self.coords)


@dataclass
class AoiConfig:
    aoi_id: str
    aois: list            # list of AoiPolygon

    @classmethod
    def from_dict(cls, data: dict) -> 'AoiConfig':
        return cls(
            aoi_id=data['aoi_id'],
            aois=[AoiPolygon(**a) for a in data['aois']]
        )

    @classmethod
    def from_json(cls, path: str) -> 'AoiConfig':
        with open(path) as f:
            return cls.from_dict(json.load(f))

    def to_json(self, path: str) -> None:
        with open(path, 'w') as f:
            json.dump(asdict(self), f, indent=4)

    def to_fov_dict(self) -> dict:
        return {aoi.name: aoi.to_polygon() for aoi in self.aois}

    def color_dict(self) -> dict:
        return {aoi.name: aoi.color for aoi in self.aois}

    def alpha_dict(self) -> dict:
        return {aoi.name: aoi.alpha for aoi in self.aois}


@dataclass
class GazeDatabase:
    """Points to a folder that bundles geometry, AOI config, and gaze recordings."""
    folder: str

    XODR_FILENAME       = 'geometry.xodr'
    AOI_CONFIG_FILENAME = 'aoi_config.json'
    GAZE_DATA_FILENAME  = 'gazes_spatiotemporal.feather'
    @property
    def xodr_path(self) -> str:
        return os.path.join(self.folder, self.XODR_FILENAME)

    @property
    def aoi_config_path(self) -> str:
        return os.path.join(self.folder, self.AOI_CONFIG_FILENAME)

    @property
    def gaze_data_path(self) -> str:
        return os.path.join(self.folder, self.GAZE_DATA_FILENAME)

    TOP_VIEW_FILENAME   = 'top_view.png'

    @property
    def top_view_path(self) -> str:
        return os.path.join(self.folder, self.TOP_VIEW_FILENAME)

    def load_aoi_config(self) -> 'AoiConfig':
        return AoiConfig.from_json(self.aoi_config_path)

    def load_gazes(self):
        import pandas as pd
        return pd.read_feather(self.gaze_data_path)

    def validate(self) -> None:
        for path in (self.xodr_path, self.aoi_config_path, self.gaze_data_path):
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Expected file not found in gaze database folder: {path}")
