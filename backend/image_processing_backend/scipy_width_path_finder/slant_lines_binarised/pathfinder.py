from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import cv2
import numpy as np
import random
import pandas as pd

from scipy_width_path_finder.blank_image import create_image
from scipy_width_path_finder.constants import MASK_TOP, MASK_BOTTOM

from scipy_width_path_finder.image_processing import image_noise_removal_contrast


def compute_pixels(img):
    new_img = img >= 150

    c = new_img.astype(int)

    return c


def applying_mask(image_path, np_array_points, index=1, open_cv=False):
    # original image
    image = cv2.imread(image_path) if not open_cv else image_path

    if not open_cv:
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image = image_noise_removal_contrast(grey, open_cv=True)

        # ret, image = cv2.threshold(grey, 100, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
        # image = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 7)

    # create a mask with white pixel and an roi of points
    mask = np.ones(image.shape, dtype=np.uint8)
    mask.fill(255)
    roi_corners = np.array(np_array_points, dtype=np.int32)

    # fill the ROI so it doesn't get wiped out when the mask is applied
    cv2.fillPoly(mask, roi_corners, (0, 0, 0))

    # cv2.imwrite(f'image_masked_{index}.png', mask)

    masked_image = cv2.bitwise_and(image, mask)

    cv2.imwrite(f'applied_mask_{index}.png', masked_image)

    return masked_image


def path_function(image_path, start_point, end_point, line_weight=1, mask=None,
                  save_as_image=False, open_cv=False, x_start=0):
    img = image_noise_removal_contrast(image_path, open_cv=open_cv)

    if mask:
        height, width = img.shape[0:2]
        if mask == MASK_BOTTOM:
            # mask = create_image(width, height - start_point - 1)
            array_points = [[(x_start, start_point + 1),
                             (width, end_point + 1),
                             (width, height),
                             (x_start, height)]]
            img = applying_mask(image_path, array_points, index=1, open_cv=open_cv)
            # img[start_point + 1:height, 0:width] = mask
        elif mask == MASK_TOP:
            array_points = [[(x_start, start_point - 1),
                             (width, end_point - 1),
                             (img.shape[1], 0),
                             (x_start, 0)]]
            img = applying_mask(image_path, array_points, index=1, open_cv=open_cv)
            # mask = create_image(width, start_point - 1)
            # img[0:start_point - 1, 0:width] = mask
        if save_as_image:
            cv2.imwrite(f'mask_applied_{start_point}.png', img)

    immap = compute_pixels(img)

    grid = Grid(matrix=immap)
    start = grid.node(0, start_point)
    end = grid.node(img.shape[1] - 1, end_point)

    finder = AStarFinder(weight=line_weight)
    print('finding path')
    path, runs = finder.find_path(start, end, grid)

    print(f"completed for point start_point: {start_point} and end_point : {end_point}")

    # print('operations:', runs, 'path length:', len(path))
    if save_as_image:
        points = np.array(path)

        cv2.polylines(img, np.int32([points]), 0, (0, 255, 0), thickness=3)

        cv2.imwrite(f'{random.randint(0, 15)}.png', img)

    return path

# image_path = "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/athul_scanned/527/527_8.png"
# np_array_points = [[(0, 74), (1030, 28), (1030, 1158), (0, 1158)]]
# applying_mask(image_path, np_array_points, index=1, open_cv=False)
