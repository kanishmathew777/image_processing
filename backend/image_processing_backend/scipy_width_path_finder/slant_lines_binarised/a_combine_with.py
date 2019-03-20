from scipy.signal import find_peaks, peak_widths
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import copy
from operator import itemgetter

from scipy_width_path_finder.image_processing import image_noise_removal_contrast
from scipy_width_path_finder.slant_lines_binarised.pathfinder import path_function
from scipy_width_path_finder.constants import MASK_BOTTOM, MASK_TOP

from scipy_width_path_finder.slant_lines_binarised.lines_left_binarised import resultant_left_points
from scipy_width_path_finder.slant_lines_binarised.lines_right_binarised import resultant_right_points
from scipy_width_path_finder.slant_lines_binarised.polylines_opencv_oprtns import crop_along_points, add_color_to_polylines


def analyse_graph_data(image_path, left_peak_with_props, right_peak_with_props):
    original_image_path = image_path
    total_paths = []
    tic = time.clock()

    opencv_image = False
    for index, (left_prop, right_prop) in enumerate(zip(left_peak_with_props, right_peak_with_props)):
        crop_line_segments = []
        upper_portion = path_function(image_path, int(left_prop[3]), int(right_prop[3]),
                                      line_weight=3, save_as_image=False, mask=MASK_BOTTOM, open_cv=opencv_image)
        total_paths.append(upper_portion)
        crop_line_segments.extend(upper_portion)

        lower_portion = path_function(image_path, int(left_prop[4]), int(right_prop[4]),
                                      line_weight=3, save_as_image=False, mask=MASK_TOP, open_cv=opencv_image)
        total_paths.append(lower_portion)
        reversed_lower_list = copy.deepcopy(lower_portion)
        reversed_lower_list.reverse()
        crop_line_segments.extend(reversed_lower_list)

        crop_along_points(image_path, [crop_line_segments], index=index, open_cv=opencv_image)
        image_path = add_color_to_polylines(image_path, [crop_line_segments], index=index, open_cv=opencv_image)
        opencv_image = True

        # crop_along_points(image_path, [crop_line_segments], index=index)

        # for paths in crop_line_segments:
        # img = cv2.imread(image_path)
        # points = np.array(paths)

        # crop_along_points(image_path, [crop_line_segments], index=index, open_cv=False)

        # cv2.polylines(img, np.int32([crop_line_segments]), 0, (0, 255, 0), thickness=3)
        #
        # cv2.imwrite(f'contours{index}.png', img)

    toc = time.clock()

    print(f"process_completed in {toc-tic} seconds")

    img = cv2.imread(original_image_path, 0)

    for paths in total_paths:
        points = np.array(paths)

        cv2.polylines(img, np.int32([points]), 0, (0, 255, 0), thickness=3)

    cv2.imwrite('total_paths.png', img)


image_path = "/home/kanish/Desktop/image_contour.png"

img = image_noise_removal_contrast(image_path, open_cv=False)

plot_graph = True

left_peaks, left_width_props, left_peak_with_props = resultant_left_points(img, opencv=True, plotgraph=plot_graph)
right_peaks, right_width_props, right_peak_with_props = resultant_right_points(img, opencv=True, plotgraph=plot_graph)

sorted_left_props = sorted(left_peak_with_props, key=itemgetter(3, 4, 1))

pop_left_list = []
pop_duplicate_left_list = []
for i, peak_props in enumerate(sorted_left_props):
    sort_left_without_index = copy.deepcopy(sorted_left_props)
    sort_left_without_index.pop(i)
    for index, j_peak_props in enumerate(sort_left_without_index):
        if j_peak_props[3] < peak_props[3] < j_peak_props[4] and \
                j_peak_props[3] < peak_props[4] < j_peak_props[4]:
            pop_left_list.append(i)
        elif j_peak_props[3] == peak_props[3] and \
                j_peak_props[4] == peak_props[4]:
            pop_duplicate_left_list.append((i, index))
        elif j_peak_props[3] == peak_props[3] and \
                j_peak_props[3] < peak_props[4] < j_peak_props[4]:
            pop_left_list.append(i)
        elif j_peak_props[4] == peak_props[4] and \
                j_peak_props[3] < peak_props[3] < j_peak_props[4]:
            pop_left_list.append(i)

duplicate_left_pop = []
for i, items in enumerate(pop_duplicate_left_list):
    duplicate_left_without_index = copy.deepcopy(pop_duplicate_left_list)
    duplicate_left_without_index.pop(i)
    for index, j_peak_props in enumerate(duplicate_left_without_index):
        if items[0] == j_peak_props[1]:
            duplicate_left_pop.append(items[0])

for items in set(duplicate_left_pop):
    pop_left_list.append(items)

avg_new_left_props = [peak_props for index, peak_props in enumerate(sorted_left_props)
                      if index not in pop_left_list]

new_left_peak_with_props = [peak_props for peak_props in avg_new_left_props if peak_props[1] > 29]
# new_left_peak_with_props = avg_new_left_props
print(new_left_peak_with_props)

sorted_right_props = sorted(right_peak_with_props, key=itemgetter(3, 4, 1))

pop_right_list = []
pop_duplicate_right_list = []
for i, peak_props in enumerate(sorted_right_props):
    sort_right_without_index = copy.deepcopy(sorted_right_props)
    sort_right_without_index.pop(i)
    for index, j_peak_props in enumerate(sort_right_without_index):
        if j_peak_props[3] < peak_props[3] < j_peak_props[4] and \
                j_peak_props[3] < peak_props[4] < j_peak_props[4]:
            pop_right_list.append(i)
        elif j_peak_props[3] == peak_props[3] and \
                j_peak_props[4] == peak_props[4]:
            pop_duplicate_right_list.append((i, index))
        elif j_peak_props[3] == peak_props[3] and \
                j_peak_props[3] < peak_props[4] < j_peak_props[4]:
            pop_right_list.append(i)
        elif j_peak_props[4] == peak_props[4] and \
                j_peak_props[3] < peak_props[3] < j_peak_props[4]:
            pop_right_list.append(i)

duplicate_right_pop = []
for i, items in enumerate(pop_duplicate_right_list):
    duplicate_right_without_index = copy.deepcopy(pop_duplicate_right_list)
    duplicate_right_without_index.pop(i)
    for index, j_peak_props in enumerate(duplicate_right_without_index):
        if items[0] == j_peak_props[1]:
            duplicate_right_pop.append(items[0])

for items in set(duplicate_right_pop):
    pop_right_list.append(items)

avg_new_right_props = [peak_props for index, peak_props in enumerate(sorted_right_props)
                       if index not in set(pop_right_list)]

new_right_peak_with_props = [peak_props for peak_props in avg_new_right_props if peak_props[1] > 29]
# new_right_peak_with_props = avg_new_right_props
print(new_right_peak_with_props)

print("left", len(new_left_peak_with_props), '\n', "right", len(new_right_peak_with_props))

analyse_graph_data(image_path, new_left_peak_with_props, new_right_peak_with_props)
