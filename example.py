from equgat import equgat
from util.config import GazeDatabase

# The gaze database 'RightGazeUrban-2022' is available on Zenodo: https://zenodo.org/records/20717040
# Download and extract it, specify the path to the extracted folder in gaze_db_path below.
gaze_db_location = ''

random_trajectory_id = GazeDatabase(gaze_db_location).load_gazes()['trajectory_id'].sample(1, random_state=42).iloc[0]

# Full algorithm run — save results to Feather
equgat(
    gaze_db_path=gaze_db_location,
    trajectory_ids=[random_trajectory_id], # None to process all trajectories
    car_road_ids=[1, 2],
    cycling_road_ids=[4],
    cyclist_sampling_config_file='input/virtual_cyclist_config.json',
)

# Plot results using Kaplan-Meier estimator
import matplotlib.pyplot as plt
import pandas as pd
from lifelines import KaplanMeierFitter

from util.config import GazeDatabase

df = pd.read_feather('output/time_to_perception_event.feather')

# trajectory duration (censoring time for cyclists never perceived)
gazes = GazeDatabase(gaze_db_location).load_gazes()
trajectory_duration = gazes.groupby('trajectory_id')['t'].agg(lambda t: t.max() - t.min())
df['trajectory_duration'] = df['trajectory_id'].map(trajectory_duration)

event_observed = df['carDriverSawCyclist'].astype(bool)
duration = df['tCarAtPerception'].where(event_observed, df['trajectory_duration'])

kmf = KaplanMeierFitter()
kmf.fit(duration, event_observed=event_observed, label='Cyclist perception')

fig, ax = plt.subplots()
kmf.plot_survival_function(ax=ax)
ax.set_xlabel('Time [s]')
ax.set_ylabel('P(cyclist not yet perceived)')
ax.set_ylim(0, 1)

ax.set_title('Kaplan-Meier estimate of driver perception of virtual cyclists')
fig.tight_layout()
plt.show()


# Visualise a gaze data
equgat(
    gaze_db_path=gaze_db_location,
    trajectory_ids=None,
    trajectory_filter=lambda df: (df.groupby('trajectory_id')['v'].transform('max') < (30 / 3.6))
                                 & (df.groupby('trajectory_id')['v'].transform('max') > (20 / 3.6)),  # optional: e.g. only trajectories with max speed between 20 and 30 km/h
                                 
    car_road_ids=[1, 2],
    cycling_road_ids=[4],
    
    cyclist_sampling_config_file='input/virtual_cyclist_config_debug.json',
    
    plot_on=True,
    plot_car_lane=False,
    plot_cycling_lane=False,
    show_gaze_aoi=True, 
    view_box=(0, 130, -10, 10),
    
    # video_path='output/trajectory.gif',
    # video_dpi=600,
)
