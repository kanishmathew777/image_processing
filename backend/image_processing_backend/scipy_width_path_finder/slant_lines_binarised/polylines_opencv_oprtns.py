import cv2
import numpy as np


def crop_along_points(image_path, np_array_points, index=1, open_cv=False):

    # original image
    image = cv2.imread(image_path) if not open_cv else image_path

    if not open_cv:
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # ret, image = cv2.threshold(grey, 100, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
        image = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 7)

    # create a mask with white pixel and an roi of points
    mask = np.ones(image.shape, dtype=np.uint8)
    mask.fill(255)
    roi_corners = np.array(np_array_points, dtype=np.int32)

    # fill the ROI so it doesn't get wiped out when the mask is applied
    cv2.fillPoly(mask, roi_corners, (0, 0, 0))

    # cv2.imwrite(f'image_masked_{index}.png', mask)

    masked_image = cv2.bitwise_or(image, mask)

    cv2.imwrite(f'masked_new_image_{index}.png', masked_image)


def add_color_to_polylines(image_path, np_array_points, index=1, color=255, open_cv=False):

    # original image
    image = cv2.imread(image_path) if not open_cv else image_path

    if not open_cv:
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 7)

    roi_corners = np.array(np_array_points, dtype=np.int32)

    # fill the ROI so it doesn't get wiped out when the mask is applied
    cv2.fillPoly(image, roi_corners, color)

    cv2.imwrite(f'colored_{index}.png', image)

    return image


# image_path = "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/athul_scanned/527/527_1.png"
#
# np_array_points = [[(0, 300), (1880, 300), (1880, 400), (0, 400)]]
# add_color_to_polylines(image_path, np_array_points, index=1)