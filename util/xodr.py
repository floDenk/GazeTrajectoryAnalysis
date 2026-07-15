import csv
import math
import subprocess
import numpy as np
from shapely.geometry import box
from shapely import affinity
from xsdata.formats.dataclass.parsers import XmlParser
from util.xodr_xml_parser import OpenDrive


def import_xodr(xodr_file):

    csvFileName = xodr_file + ".csv"
    subprocess.run(["odrplot", xodr_file, csvFileName, "0.1"])

    with open(csvFileName) as f:
        reader = csv.reader(f, skipinitialspace=True)
        positions = list(reader)

    H_SCALE = 10
    text_x_offset = 0
    text_y_offset = 0.7
    text_size = 7

    ref_x = []
    ref_y = []
    ref_z = []
    ref_h = []

    lane_x = []
    lane_y = []
    lane_z = []
    lane_h = []

    border_x = []
    border_y = []
    border_z = []
    border_h = []

    road_id = []
    road_id_x = []
    road_id_y = []

    road_start_dots_x = []
    road_start_dots_y = []

    road_end_dots_x = []
    road_end_dots_y = []

    lane_section_dots_x = []
    lane_section_dots_y = []

    arrow_dx = []
    arrow_dy = []

    current_road_id = None
    current_lane_id = None
    current_lane_section = None
    new_lane_section = False

    for i in range(len(positions) + 1):

        if i < len(positions):
            pos = positions[i]

        # plot road id before going to next road
        if i == len(positions) or (pos[0] == 'lane' and i > 0 and current_lane_id == '0'):

            if current_lane_section == '0':
                road_id.append(int(current_road_id))
                index = int(len(ref_x[-1])/3.0)
                h = ref_h[-1][index]
                road_id_x.append(ref_x[-1][index] + (text_x_offset * math.cos(h) - text_y_offset * math.sin(h)))
                road_id_y.append(ref_y[-1][index] + (text_x_offset * math.sin(h) + text_y_offset * math.cos(h)))
                road_start_dots_x.append(ref_x[-1][0])
                road_start_dots_y.append(ref_y[-1][0])
                if len(ref_x) > 0:
                    arrow_dx.append(ref_x[-1][1]-ref_x[-1][0])
                    arrow_dy.append(ref_y[-1][1]-ref_y[-1][0])
                else:
                    arrow_dx.append(0)
                    arrow_dy.append(0)

            lane_section_dots_x.append(ref_x[-1][-1])
            lane_section_dots_y.append(ref_y[-1][-1])

        if i == len(positions):
            break

        if pos[0] == 'lane':
            current_road_id = pos[1]
            current_lane_section = pos[2]
            current_lane_id = pos[3]
            if pos[3] == '0':
                ltype = 'ref'
                ref_x.append([])
                ref_y.append([])
                ref_z.append([])
                ref_h.append([])

            elif pos[4] == 'no-driving':
                ltype = 'border'
                border_x.append([])
                border_y.append([])
                border_z.append([])
                border_h.append([])
            else:
                ltype = 'lane'
                lane_x.append([])
                lane_y.append([])
                lane_z.append([])
                lane_h.append([])
        else:
            if ltype == 'ref':
                ref_x[-1].append(float(pos[0]))
                ref_y[-1].append(float(pos[1]))
                ref_z[-1].append(float(pos[2]))
                ref_h[-1].append(float(pos[3]))

            elif ltype == 'border':
                border_x[-1].append(float(pos[0]))
                border_y[-1].append(float(pos[1]))
                border_z[-1].append(float(pos[2]))
                border_h[-1].append(float(pos[3]))
            else:
                lane_x[-1].append(float(pos[0]))
                lane_y[-1].append(float(pos[1]))
                lane_z[-1].append(float(pos[2]))
                lane_h[-1].append(float(pos[3]))

    s = []
    psi = []
    for i in range(len(ref_x)):
        s.append([0])
        dxInit = ref_x[i][1] - ref_x[i][0]
        dyInit = ref_y[i][1] - ref_y[i][0]
        psi.append([math.atan2(dyInit,dxInit)])
        for j in range(1,len(ref_x[i])):
            dx = ref_x[i][j] - ref_x[i][j-1]
            dy = ref_y[i][j] - ref_y[i][j-1]
            s[i].append(s[i][j-1] + math.sqrt(dx*dx + dy*dy))
            psi[i].append(math.atan2(dy,dx))

    return ref_x, ref_y, s, psi


def get_occlusion_object_from_xodr(xodr_file, ref_s_car, ref_x_car, ref_y_car, ref_psi_car):
    parser = XmlParser()
    xodr_xml = parser.parse(xodr_file, OpenDrive)
    for road in xodr_xml.road:
        if road.objects is None:
            continue
        else:
            obj = road.objects.object_value[0]
            idx_s_center_obj = np.searchsorted(ref_s_car, obj.s)
            x_center_obj = ref_x_car[idx_s_center_obj] - obj.t * math.sin(ref_psi_car[idx_s_center_obj])
            y_center_obj = ref_y_car[idx_s_center_obj] + obj.t * math.cos(ref_psi_car[idx_s_center_obj])

            obj_raw = box(-obj.length/2, -obj.width/2, obj.length/2, obj.width/2)
            obj = affinity.translate(affinity.rotate(obj_raw, np.rad2deg(ref_psi_car[idx_s_center_obj]), (0, 0)), x_center_obj, y_center_obj)

            return obj
