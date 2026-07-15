import time
from io import BytesIO

import cairosvg
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass, field
from matplotlib.image import AxesImage
from shapely.geometry import Polygon, LineString, MultiLineString
from util.geometry import find_xy_for_s

def _load_svg(path, output_width=600):
    png_data = cairosvg.svg2png(url=path, output_width=output_width)
    img = mpimg.imread(BytesIO(png_data), format='png')
    # Crop to tight bounding box of non-transparent pixels so whitespace on the SVG canvas
    # (e.g. from an A4-sized Inkscape document) is removed before display
    if img.shape[2] == 4:
        mask = img[:, :, 3] > 0.01
    else:
        mask = ~np.all(img > 0.95, axis=2)
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    if rows.any() and cols.any():
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        padding = 4
        rmin, rmax = max(0, rmin - padding), min(img.shape[0] - 1, rmax + padding)
        cmin, cmax = max(0, cmin - padding), min(img.shape[1] - 1, cmax + padding)
        img = img[rmin:rmax + 1, cmin:cmax + 1]
    return img


def _draw_rect(ax, cx, cy, length, width, angle_deg, color, alpha=0.8, zorder=3):
    angle_rad = np.deg2rad(angle_deg)
    cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)
    corners = np.array([[ length / 2,  width / 2],
                        [-length / 2,  width / 2],
                        [-length / 2, -width / 2],
                        [ length / 2, -width / 2]])
    rot = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
    pts = corners @ rot.T + [cx, cy]
    ax.fill(pts[:, 0], pts[:, 1], color=color, alpha=alpha, zorder=zorder)


_pause_state = {'paused': False}
_registered_figures = set()
_timing_state = {'last_wall_t': None, 'last_sim_i': None, 'speed_x': None}


def _on_key_press(event):
    if event.key == ' ':
        _pause_state['paused'] = not _pause_state['paused']


@dataclass
class TopViewImage:
    path: str
    offset: tuple = (0.0, 0.0)   # lower-left corner in geographic coordinates (meters)
    scale: float  = 1.0           # meters per pixel
    data: np.ndarray       = field(default=None, init=False, repr=False)
    _imshow_artist: object = field(default=None, init=False, repr=False)

    def __post_init__(self):
        self.data = np.flipud(plt.imread(self.path))


def _plot_cyclist_images(ax, x_positions, y_positions, cyclist_img, width_m=2.0, height_m=2.0):
    for x, y in zip(x_positions, y_positions):
        im = AxesImage(ax, zorder=4)
        im.set_data(cyclist_img)
        im.set_extent([x - width_m / 2, x + width_m / 2, y - height_m / 2, y + height_m / 2])
        ax.add_artist(im)


def plot_car_image(ax, car_img, x, y, angle_deg, length_m=5.0, width_m=2.2):
    from scipy.ndimage import rotate as ndimage_rotate
    rotated = ndimage_rotate(car_img, angle_deg, reshape=True, cval=0.0, order=1)
    cos_a = abs(np.cos(np.deg2rad(angle_deg)))
    sin_a = abs(np.sin(np.deg2rad(angle_deg)))
    bb_w = length_m * cos_a + width_m * sin_a
    bb_h = length_m * sin_a + width_m * cos_a
    im = AxesImage(ax, zorder=3)
    im.set_data(rotated)
    im.set_extent([x - bb_w / 2, x + bb_w / 2, y - bb_h / 2, y + bb_h / 2])
    ax.add_artist(im)


PLOT_STEP = 5 


def plot(
    i, fig, ax, gaze_name,sim_dt,
    # --- Scene geometry ---
    shapes, shapely_colors=None, shapely_alphas=None,
    # --- Background / view ---
    top_view_image: TopViewImage = None, view_box=None, transparent_bg=False,
    # --- Car overlay ---
    car_img=None, car_x=None, car_y=None, car_angle_deg=None,
    # --- Cyclist overlays ---
    df=None, cyclist_img_unseen=None, cyclist_img_seen=None,
    s_lane_cyclist=None, x_lane_cyclist=None, y_lane_cyclist=None,
    # --- Video writer ---
    writer=None
):
    fig_id = id(fig)
    if fig_id not in _registered_figures:
        fig.canvas.mpl_connect('key_press_event', _on_key_press)
        _registered_figures.add(fig_id)

    if i % PLOT_STEP == 0:
        now = time.perf_counter()
        if _timing_state['last_wall_t'] is not None and _timing_state['last_sim_i'] is not None:
            wall_dt = now - _timing_state['last_wall_t']
            sim_elapsed = (i - _timing_state['last_sim_i']) * sim_dt
            if wall_dt > 0:
                new_speed = sim_elapsed / wall_dt
                prev = _timing_state['speed_x']
                _timing_state['speed_x'] = new_speed if prev is None else 0.3 * new_speed + 0.7 * prev
        _timing_state['last_wall_t'] = now
        _timing_state['last_sim_i'] = i

        ax.clear()
        if transparent_bg:
            fig.patch.set_alpha(0.0)
            ax.set_facecolor('none')
        speed_str = f"  |  {_timing_state['speed_x']:.2f}x realtime" if _timing_state['speed_x'] is not None else ""
        ax.set_title(f"Step {i}  |  Gaze region: \"{gaze_name}\"{speed_str}", fontsize=11)

        # Background image: create the AxesImage once and re-add it after each clear()
        # so matplotlib can reuse its internal rasterisation cache.
        if top_view_image is not None:
            # The cached artist is only reusable within the figure it was created for
            # (e.g. across clear()'d frames of the same trajectory); a new trajectory
            # gets a new fig/ax, so the artist must be recreated for it.
            if top_view_image._imshow_artist is None or top_view_image._imshow_artist.figure is not fig:
                dx, dy = top_view_image.offset
                h, w = top_view_image.data.shape[:2]
                img_extent = [dx, dx + w * top_view_image.scale,
                              dy, dy + h * top_view_image.scale]
                top_view_image._imshow_artist = ax.imshow(
                    top_view_image.data, extent=img_extent, origin='lower')
            else:
                ax.add_image(top_view_image._imshow_artist)

        plot_shapely_objects(ax, shapes, colors=shapely_colors, alphas=shapely_alphas)

        if car_img is not None and car_x is not None:
            plot_car_image(ax, car_img, car_x, car_y, car_angle_deg)
        elif car_x is not None:
            _draw_rect(ax, car_x, car_y, length=5.0, width=2.2,
                       angle_deg=car_angle_deg, color='steelblue')

        if df is not None and s_lane_cyclist is not None:
            s_cyclist        = df['s_cyclist'].to_numpy()
            cyclist_seen_all = df['carDriverSawCyclist'].to_numpy().astype(bool)

            x_cyclist, y_cyclist, in_bounds = find_xy_for_s(
                s_cyclist, s_lane_cyclist, x_lane_cyclist, y_lane_cyclist
            )
            cyclist_seen = cyclist_seen_all[in_bounds]

            if cyclist_img_unseen is not None:
                _plot_cyclist_images(ax, x_cyclist[~cyclist_seen], y_cyclist[~cyclist_seen], cyclist_img_unseen)
            else:
                for x, y in zip(x_cyclist[~cyclist_seen], y_cyclist[~cyclist_seen]):
                    _draw_rect(ax, x, y, length=2.0, width=1.0, angle_deg=0, color='red', alpha=0.7, zorder=4)

            if cyclist_img_seen is not None:
                _plot_cyclist_images(ax, x_cyclist[cyclist_seen], y_cyclist[cyclist_seen], cyclist_img_seen)
            else:
                for x, y in zip(x_cyclist[cyclist_seen], y_cyclist[cyclist_seen]):
                    _draw_rect(ax, x, y, length=2.0, width=1.0, angle_deg=0, color='green', alpha=0.7, zorder=4)

        ax.set_aspect('equal', adjustable='box')
        if view_box is not None:
            ax.set_xlim(view_box[0], view_box[1])
            ax.set_ylim(view_box[2], view_box[3])

        fig.canvas.draw()

        if writer is not None:
            writer.grab_frame()
        else:
            # plt.pause shows the window and runs the event loop; 1 ms is enough for key presses
            plt.pause(0.001)
            if _pause_state['paused']:
                base_title = ax.get_title()
                ax.set_title(base_title + '  [PAUSED — press Space to continue]')
                fig.canvas.draw()
                while _pause_state['paused']:
                    fig.canvas.start_event_loop(0.05)
                _timing_state['last_wall_t'] = None  # don't count pause duration in speed
                ax.set_title(base_title)
                fig.canvas.draw()


def plot_shapely_objects(ax, shapes, colors=None, alphas=None, labels=None):
    default_colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    for idx, obj in enumerate(shapes):
        color = (colors[idx] if colors is not None and idx < len(colors) and colors[idx] is not None
                 else default_colors[idx % len(default_colors)])
        alpha = (alphas[idx] if alphas is not None and idx < len(alphas) and alphas[idx] is not None
                 else 1.0)
        label = (labels[idx] if labels is not None and idx < len(labels) else None)
        if isinstance(obj, Polygon):
            x, y = obj.exterior.xy
            ax.fill(x, y, color=color, alpha=alpha)
            ax.plot(x, y, color=color)
            if label is not None:
                ax.text(obj.centroid.x, obj.centroid.y, label,
                        ha='center', va='center', fontsize=8, fontweight='bold', color=color)
        elif isinstance(obj, LineString):
            x, y = obj.xy
            ax.plot(x, y, color=color, alpha=alpha)
        elif isinstance(obj, MultiLineString):
            for line in obj.geoms:
                x, y = line.xy
                ax.plot(x, y, color=color, alpha=alpha)
