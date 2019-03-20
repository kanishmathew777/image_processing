from scipy.signal import find_peaks, peak_widths
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import copy

from scipy_width_path_finder.path_finder import path_function
from scipy_width_path_finder.constants import MASK_BOTTOM, MASK_TOP
from scipy_width_path_finder.polylines_opencv_oprtns import crop_along_points
from scipy_width_path_finder.image_processing import image_noise_removal_contrast


def get_peaks_with_properties(image_path, rel_height=0.7, apply_denoising=7, min_peak_width=20):
    """

    :param image_path: takes the image_path
    :param rel_height: avg height of the peaks in graph
    :param apply_denoising: apply denoising the graph if needed
    :return:
        x: graph_data,
        peaks: the peaks in the graph data,
        width_props: the properties of peaks,
        peaks_with_properties: get combined peak and properties

    support website:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.peak_widths.html#scipy.signal.peak_widths
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html

    """
    # img = cv2.imread(image_path, 0)

    # applying threshold
    # ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    # thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 7)

    img = image_noise_removal_contrast(image_path)

    cv2.imwrite("threshed.png", img)

    y_sum = cv2.reduce(img, 1, cv2.REDUCE_AVG, dtype=cv2.CV_32S)

    ysum = [256 - y_su[0] for y_su in y_sum]

    # reversed_ysum = list(reversed(ysum))
    reversed_ysum = ysum

    x = reversed_ysum
    if apply_denoising:
        s = pd.Series(reversed_ysum)
        x = s.ewm(apply_denoising).mean()

    peaks, _ = find_peaks(x, height=int(0.14 * np.max(ysum)), width=min_peak_width, prominence=0.7)

    width_props = peak_widths(x, peaks, rel_height=rel_height)

    peaks_with_properties = [[peak, width, width_height, left_ips, right_fps] for
                             peak, width, width_height, left_ips, right_fps in
                             zip(peaks, width_props[0], width_props[1], width_props[2],
                                 width_props[3])]

    return x, peaks, width_props, peaks_with_properties


def plot_graph(x, peaks, width_props):
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.hlines(*width_props[1:], color="C3")
    plt.show()


def analyse_graph_data(image_path, peaks_with_props):
    total_paths = []
    tic = time.clock()

    for index, property in enumerate(peaks_with_props):
        print(property)
        crop_line_segments = []
        upper_portion = path_function(image_path, int(property[3]), int(property[3]), line_weight=3,
                                      save_as_image=False, mask=MASK_BOTTOM)
        total_paths.append(upper_portion)
        crop_line_segments.extend(upper_portion)

        lower_portion = path_function(image_path, int(property[4]), int(property[4]), line_weight=3,
                                      save_as_image=False, mask=MASK_TOP)
        total_paths.append(lower_portion)
        reversed_lower_list = copy.deepcopy(lower_portion)
        reversed_lower_list.reverse()
        crop_line_segments.extend(reversed_lower_list)

        crop_along_points(image_path, [crop_line_segments], index=index)

        # for paths in crop_line_segments:
        #     points = np.array(paths)
        #
        #     cv2.polylines(img, np.int32([points]), 0, (0, 255, 0), thickness=3)
        #
        #     cv2.imwrite('contours.png', img)

    toc = time.clock()

    print(f"process_completed in {toc-tic} seconds")

    img = cv2.imread(image_path, 0)

    for paths in total_paths:
        points = np.array(paths)

        cv2.polylines(img, np.int32([points]), 0, (0, 255, 0), thickness=3)

    cv2.imwrite('total_paths.png', img)


image_path = "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/athul_scanned/525/525_1.png"

graph_data, peaks, width_props, peaks_with_props = get_peaks_with_properties(image_path)

plot_graph(graph_data, peaks, width_props)

analyse_graph_data(image_path, peaks_with_props)
