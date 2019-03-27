import cv2
import numpy as np

img = cv2.imread('/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/athul_scanned/525/525_2.png', 0)

kernel = np.ones((5, 1), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imwrite('morphex.png', erosion)

cv2.imshow('gray', erosion)
cv2.waitKey(0)
