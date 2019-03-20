import cv2
from plantcv import plantcv as pcv
import numpy as np

# Set global debug behavior to None (default), "print" (to file), or "plot" (Jupyter Notebooks or X11)

pcv.params.debug = "print"

img, path, filename = pcv.readimage('/home/kanish/Desktop/image.png', mode="gray")

s_thresh = pcv.threshold.binary(~img, 85, 255, 'light')

# cv2.imwrite('new_1.png', s)

# masked = pcv.apply_mask(img, s_thresh, 'white')

# print('Haii')

dist = cv2.distanceTransform(s_thresh, cv2.DIST_L2, 5)

kernel = np.ones((1, 1), np.uint8)
opening = cv2.morphologyEx(s_thresh, cv2.MORPH_OPEN, kernel, iterations=1)

sure_bg = cv2.dilate(opening, kernel, iterations=1)

ret, sure_fg = cv2.threshold(dist, 0.051 * dist.max(), 255, 0)

cv2.imwrite('sure_fg.png', sure_fg)
cv2.imwrite('sure_bg.png', sure_bg)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# markers = cv2.watershed(img, markers)
# img[markers == -1] = [255, 0, 0]
cv2.imwrite('markers.png', ~markers)

# hist_header, hist_data, analysis_images  = pcv.analyze_nir_intensity(img, masked, 256, histplot=True)
