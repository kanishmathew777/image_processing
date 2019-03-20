import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

img = cv2.imread("/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/fwdsamplefiles/image.png", 0)

x_sum = cv2.reduce(img, 0, cv2.REDUCE_AVG, dtype=cv2.CV_32S)
y_sum = cv2.reduce(img, 1, cv2.REDUCE_AVG, dtype=cv2.CV_32S)

ysum = [y_su[0] for y_su in y_sum]
reversed_ysum = list(reversed(ysum))

x_axis = [pixel for pixel in range(img.shape[0])]

# plt.plot(reversed_ysum , x_axis)


s = pd.Series(reversed_ysum)
s = s.ewm(3).mean()

plt.plot(s, x_axis)

# smooth_data = pd.(reversed_ysum, 5).plot(style='k')
plt.show()

# plt.ylabel('image_height')
# plt.xlabel('pixel_density')
# plt.show()