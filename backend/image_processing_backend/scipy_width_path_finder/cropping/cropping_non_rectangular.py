import cv2
import numpy as np


def crop_points(image_path):
    # original image
    image = cv2.imread(image_path)
    # ret, image = cv2.threshold(image, 120, 255, cv2.THRESH_OTSU)

    # create a mask with white pixel and an roi of points
    mask = np.ones(image.shape, dtype=np.uint8)
    mask.fill(255)
    roi_corners = np.array([[(0, 300), (image.shape[1], 300), (image.shape[1], 400), (0, 400)]], dtype=np.int32)
    # fill the ROI so it doesn't get wiped out when the mask is applied
    cv2.fillPoly(mask, roi_corners, (0, 0, 0))

    # cv2.imwrite('image_masked.png', mask)

    masked_image = cv2.bitwise_or(image, mask)

    # cv2.imwrite('new_masked_image.png', masked_image)
