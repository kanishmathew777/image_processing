import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths

from scipy_width_path_finder.image_processing import image_noise_removal_contrast

patterns = {}
# patterns['101'] = '111'
# patterns['1001'] = '1111'


def compute_pixels(image):

    c = (image >= 120).astype(int)

    return c


def plot_graph(x, peaks, width_props):
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.hlines(*width_props[1:], color="C3")
    plt.show()


def replace_patterns(list_items):
    string_list = ''.join(map(str, list_items))
    for pattern, value in patterns.items():
        # if a pattern is detected, we replace it
        string_list = string_list.replace(pattern, value)
        list_items = [int(x) for x in string_list]

    return list_items


def resultant_right_points(image_path, plotgraph=False, opencv=False):

    img = cv2.imread(image_path, 0) if not opencv else image_path

    inmap = compute_pixels(img)

    resultant_list = []
    for i in range(0, img.shape[0]):
        updated = False
        for index, j in enumerate(range(img.shape[1] - 1, 0, -1)):
            if inmap[i][j] == 0:
                if index < (0.98 * img.shape[1]):
                    upper_limit = j - 12
                else:
                    upper_limit = 0
                print(j, upper_limit, index)
                avg_mean = [inmap[i][row] for row in range(img.shape[1] - index - 1, upper_limit, -1)]
                avg_mean = np.average(avg_mean)
                if avg_mean < 0.25:
                    resultant_list.append(index)
                    updated = True
                    break
        if not updated:
            resultant_list.append(inmap.shape[1])

    # resultant_list = replace_patterns(resultant_list)
    resultant_list = [inmap.shape[1] - items for items in resultant_list]
    resultant_list = np.array(resultant_list)

    peaks, _ = find_peaks(resultant_list, width=20)

    width_props = peak_widths(resultant_list, peaks, rel_height=0.60)

    peaks_with_properties = [[int(peak), int(width), int(width_height), int(left_ips), int(right_fps)] for
                             peak, width, width_height, left_ips, right_fps in
                             zip(peaks, width_props[0], width_props[1], width_props[2],
                                 width_props[3])]

    if plotgraph:
        plot_graph(resultant_list, peaks, width_props)

    return peaks, width_props, peaks_with_properties

# image_path = "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/athul_scanned/522/522_3.png"
#
# img = image_noise_removal_contrast(image_path, open_cv=False)

# right_peaks, right_width_props, right_peak_with_props = resultant_right_points(img, opencv=True, plotgraph=True)
#
# print(right_peak_with_props)
