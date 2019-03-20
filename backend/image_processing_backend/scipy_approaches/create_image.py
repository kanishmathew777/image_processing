import numpy as np
import cv2

img = np.zeros([100, 100, 1], dtype=np.uint8)
img.fill(0)
cv2.imwrite('new_blank.png', img)

