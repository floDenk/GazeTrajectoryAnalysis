import numpy as np
from shapely.geometry import LineString, MultiLineString, Point, Polygon
from shapely import intersection


def find_xy_for_s(s_values, s_lane, x_lane, y_lane):
    """Find (x, y) track coordinates for given s-values by nearest-neighbour in s.

    Returns (x, y, in_bounds) where in_bounds is a boolean mask selecting
    entries from s_values that fall within [0, s_lane[-1]].
    """
    in_bounds = (s_values >= 0) & (s_values <= s_lane[-1])
    s_valid = s_values[in_bounds]
    ds = np.abs(s_lane[np.newaxis, :] - s_valid[:, np.newaxis])  # (N_valid, M)
    closest_idx = np.argmin(ds, axis=1)                           # (N_valid,)
    return x_lane[closest_idx], y_lane[closest_idx], in_bounds


def find_s_coverage_for_geometry(geometry, x_lane, y_lane, s_lane):
    """Find s-coordinate coverage intervals on a lane for a LineString or MultiLineString.

    For each vertex of the intersection geometry, the closest track point is found
    via Euclidean distance. Returns a list of (s_min, s_max) tuples, one per segment.
    Returns [] for empty or unsupported geometries.
    """
    if geometry.is_empty:
        return []

    def _s_range_for_line(line):
        coords = np.array(line.coords)               # (N, 2)
        dx = x_lane - coords[:, 0:1]                 # (N, M) via broadcasting
        dy = y_lane - coords[:, 1:2]                 # (N, M)
        closest = np.argmin(dx**2 + dy**2, axis=1)   # (N,) – argmin is monotonic, skip sqrt
        s_vals = s_lane[closest]
        return (float(s_vals.min()), float(s_vals.max()))

    if isinstance(geometry, LineString):
        return [_s_range_for_line(geometry)]
    elif isinstance(geometry, MultiLineString):
        return [_s_range_for_line(line) for line in geometry.geoms]
    return []


def build_lane(road_ids, ref_x, ref_y, s, psi):
    """Build cumulative lane arrays and a Shapely track from xodr data for a sequence of road IDs."""
    s_lane = np.zeros(0)
    for i, road_id in enumerate(road_ids):
        if i == 0:
            s_lane = np.concatenate([s_lane, s[road_id]])
        else:
            s_lane = np.concatenate([s_lane, s[road_id][1:] + s_lane[-1]])
    
    x_lane = np.zeros(0)
    y_lane = np.zeros(0)
    psi_lane = np.zeros(0)
    for i, road_id in enumerate(road_ids):
        x_lane = np.concatenate([x_lane, ref_x[road_id][1:] if i > 0 else ref_x[road_id]])
        y_lane = np.concatenate([y_lane, ref_y[road_id][1:] if i > 0 else ref_y[road_id]])
        psi_lane = np.concatenate([psi_lane, psi[road_id][1:] if i > 0 else psi[road_id]])
    
    track    = LineString(zip(x_lane, y_lane))

    return s_lane, x_lane, y_lane, psi_lane, track


def get_closest_intersection(originPoint, ray, obstacle):
    intersections = []
    intersection = ray.intersection(obstacle)
    if not intersection.is_empty:
        if isinstance(intersection, Point):
            intersections.append(intersection)
        elif isinstance(intersection, LineString):
            intersections.extend(
                [Point(coord) for coord in intersection.coords]
            )
    if intersections:
        closest_points = sorted(
            intersections, key=lambda p: originPoint.distance(p)
        )
        if closest_points[0] == originPoint:
            return closest_points[1] if len(closest_points) > 1 else None
        else:
            return closest_points[0]
    else:
        return None


def pointVisible(origin, point, obstacle):
    ray = LineString([origin, point])
    intersection = ray.intersection(obstacle)
    if (
        intersection.is_empty
        or intersection == point
        or isinstance(intersection, LineString)
        and len(intersection.coords) == 2
        and intersection.coords[0] == intersection.coords[1]
    ):
        return True
    else:
        return False


def construct_rays(originPoint, point):
    dx = point.x - originPoint.x
    dy = point.y - originPoint.y
    angle = np.arctan2(dy, dx)
    extended_point1 = Point(
        originPoint.x + np.cos(angle * 1.000001) * 1000,
        originPoint.y + np.sin(angle * 1.000001) * 1000,
    )
    ray1 = LineString([originPoint, extended_point1])
    extended_point2 = Point(
        originPoint.x + np.cos(angle * 0.999999) * 1000,
        originPoint.y + np.sin(angle * 0.999999) * 1000,
    )
    ray2 = LineString([originPoint, extended_point2])
    return ray1, ray2


def compute_visibility(thisAOI, obstacle):
    thisIntersection = intersection(obstacle, thisAOI)
    if thisIntersection.is_empty:
        return thisAOI
    if not isinstance(thisIntersection, Polygon):
        return thisAOI

    originVertex = thisAOI.exterior.coords[0]
    originPoint = Point(originVertex)

    visibility_polygon_coords = [originPoint]

    rays = []
    for vertex in thisAOI.exterior.coords:
        if vertex == originVertex:
            continue
        rays.append(LineString([originPoint, Point(vertex)]))

    for vertex in thisIntersection.exterior.coords[0:-1]:
        if not pointVisible(originPoint, Point(vertex), obstacle):
            continue

        if any(Point(vertex).distance(ray) < 1e-3 for ray in rays):
            continue

        ray1, ray2 = construct_rays(originPoint, Point(vertex))
        rays.append(ray1)
        rays.append(ray2)

    ray_angles = []
    ref_angle = 0

    for idx, ray in enumerate(rays):
        dx = ray.coords[1][0] - ray.coords[0][0]
        dy = ray.coords[1][1] - ray.coords[0][1]
        angle = (np.arctan2(dy, dx) + 2 * np.pi) % (2 * np.pi)
        if idx == 0:
            ref_angle = angle

        angle = (angle - ref_angle + 2 * np.pi) % (2 * np.pi)
        ray_angles.append(angle)

    rays = [ray for _, ray in sorted(zip(ray_angles, rays))]

    for ray in rays:
        closest_point_obstacle = get_closest_intersection(
            originPoint, ray, obstacle
        )
        closest_point_aoi = get_closest_intersection(originPoint, ray, thisAOI)
        if closest_point_aoi is not None and pointVisible(
            originPoint, closest_point_aoi, obstacle
        ):
            visibility_polygon_coords.append(
                (closest_point_aoi.x, closest_point_aoi.y)
            )
        if closest_point_obstacle is not None and pointVisible(
            originPoint, closest_point_obstacle, obstacle
        ):
            visibility_polygon_coords.append(
                (closest_point_obstacle.x, closest_point_obstacle.y)
            )

    visibility_polygon = Polygon(visibility_polygon_coords)
    return visibility_polygon
