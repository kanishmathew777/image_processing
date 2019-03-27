import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths

from scipy_width_path_finder.image_processing import image_noise_removal_contrast

patterns = {}
patterns['101'] = '111'
# patterns['1001'] = '1111'


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


image_path = "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/fwdsamplefiles/straighten.jpg"

img = cv2.imread(image_path, 0)

img = image_noise_removal_contrast(img, open_cv=True)

head, tail = os.path.split(image_path)

cv2.imwrite(f"binarised_{tail}", img)

resultant_list = []
for i in range(0, img.shape[0]):
    updated = False
    for j in range(0, img.shape[1]):
        if img[i][j] < 125:
            if j < (0.99 * img.shape[1]):
                upper_limit = j + 12
                # upper_limit = j + int(img.shape[1] * 0.01)
            else:
                upper_limit = int(img.shape[1])
            avg_mean = [img[i][row] for row in range(j, upper_limit, 1)]
            avg_mean = np.average(avg_mean)
            if avg_mean < 55:
                resultant_list.append(1)
                # resultant_list.append((img.shape[1] - j))
                updated = True
                break
            else:
                pass
        else:
            pass
    if not updated:
        resultant_list.append(0)
        # resultant_list.append(img.shape[1])

resultant_list = replace_patterns(resultant_list)
resultant_list = np.array(resultant_list)

peaks, _ = find_peaks(resultant_list, width=27)

width_props = peak_widths(resultant_list, peaks, rel_height=0.15)

plot_graph(resultant_list, peaks, width_props)

print(resultant_list)
