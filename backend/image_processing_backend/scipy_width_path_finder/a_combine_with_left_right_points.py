from scipy.signal import find_peaks, peak_widths
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import copy

from scipy_width_path_finder.image_processing import image_noise_removal_contrast
from scipy_width_path_finder.path_finder import path_function
from scipy_width_path_finder.constants import MASK_BOTTOM, MASK_TOP
from scipy_width_path_finder.polylines_opencv_oprtns import crop_along_points

from scipy_width_path_finder.slant_lines_binarised.lines_left_binarised import resultant_left_points
from scipy_width_path_finder.slant_lines_binarised.lines_right_binarised import resultant_right_points


def analyse_graph_data(image_path, left_peak_with_props, right_peak_with_props):
    total_paths = []
    tic = time.clock()

    for index, (left_prop, right_prop) in enumerate(zip(left_peak_with_props, right_peak_with_props)):
        crop_line_segments = []
        upper_portion = path_function(image_path, int(left_prop[3]), int(right_prop[3]),
                                      line_weight=3, save_as_image=True, mask=MASK_BOTTOM)
        total_paths.append(upper_portion)
        crop_line_segments.extend(upper_portion)

        lower_portion = path_function(image_path, int(left_prop[4]), int(right_prop[4]),
                                      line_weight=3, save_as_image=False, mask=MASK_TOP)
        total_paths.append(lower_portion)
        reversed_lower_list = copy.deepcopy(lower_portion)
        reversed_lower_list.reverse()
        crop_line_segments.extend(reversed_lower_list)

        crop_along_points(image_path, [crop_line_segments], index=index)

        # for paths in crop_line_segments:
        img = cv2.imread(image_path)
        # points = np.array(paths)

        cv2.polylines(img, np.int32([crop_line_segments]), 0, (0, 255, 0), thickness=3)

        cv2.imwrite(f'contours{index}.png', img)

    toc = time.clock()

    print(f"process_completed in {toc-tic} seconds")

    img = cv2.imread(image_path, 0)

    for paths in total_paths:
        points = np.array(paths)

        cv2.polylines(img, np.int32([points]), 0, (0, 255, 0), thickness=3)

    cv2.imwrite('total_paths.png', img)


image_path = "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/athul_scanned/527/527_7.png"

img = image_noise_removal_contrast(image_path, open_cv=False)

left_peaks, left_width_props, left_peak_with_props = resultant_left_points(img, opencv=True)
right_peaks, right_width_props, right_peak_with_props = resultant_right_points(img, opencv=True)

print(left_peak_with_props, '\n', right_peak_with_props)

analyse_graph_data(image_path, left_peak_with_props, right_peak_with_props)
