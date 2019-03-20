from scipy.signal import chirp, find_peaks, peak_widths, peak_prominences, find_peaks_cwt
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd

img = cv2.imread(
    "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/fwdsamplefiles/image.png", 0)

x_sum = cv2.reduce(img, 0, cv2.REDUCE_AVG, dtype=cv2.CV_32S)
y_sum = cv2.reduce(img, 1, cv2.REDUCE_AVG, dtype=cv2.CV_32S)

ysum = [256 - y_su[0] for y_su in y_sum]

# reversed_ysum = list(reversed(ysum))
reversed_ysum = ysum

x_axis = [pixel for pixel in range(img.shape[0])]

# x = reversed_ysum

s = pd.Series(reversed_ysum)
x = s.ewm(5).mean()

peaks, _ = find_peaks(x)
results_half = peak_widths(x, peaks, rel_height=0.5)

# results_full = peak_widths(x, peaks, rel_height=0.7)

results_full = peak_widths(x, peaks, rel_height=0.6)


for peak, width, width_height, left_ips, right_fps in zip(peaks, results_full[0], results_full[1], results_full[2], results_full[3]):
    print(peak, width, width_height, left_ips, right_fps)
# print(results_full[0])


plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# plt.hlines(*results_half[1:], color="C2")
plt.hlines(*results_full[1:], color="C3")
plt.show()
