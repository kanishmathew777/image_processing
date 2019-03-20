import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread('/home/kanish/Desktop/image.png', cv2.IMREAD_GRAYSCALE)

_, It = cv2.threshold(I, 0., 255, cv2.THRESH_OTSU)
It = cv2.bitwise_not(It)
_, labels = cv2.connectedComponents(I)

result = np.zeros((I.shape[0], I.shape[1], 3), np.uint8)

for i in range(labels.min(), labels.max() + 1):
    mask = cv2.compare(labels, i, cv2.CMP_EQ)

    _, ctrs, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    result = cv2.drawContours(result, ctrs, -1, (0xFF, 0, 0))

cv2.imwrite('new_image.png', result)