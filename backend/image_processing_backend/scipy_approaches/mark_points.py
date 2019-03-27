import cv2
import numpy as np


# 1221.8 1273.0666666666666
# 38.8 173.2
# 52.7 87.3
# 60.900000000000006 94.51666666666667

# 127.675 151.325
# 737.8 841.2
# 458.4 563.6
# 180.9 382.1

img = cv2.imread(
    '/home/kanish/Desktop/image_processing_proj/backend/image_processing_backend/scipy_approaches/straighten.jpg')


points = np.array([[25, 77], [25, 172]])

cv2.polylines(img, np.int32([points]), 1, (0, 255, 0), thickness=3)

cv2.imwrite('saved.png', img)