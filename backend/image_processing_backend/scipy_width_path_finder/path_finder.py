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


def path_function(image_path, start_point, end_point, line_weight=1, mask=None,
                  save_as_image=False, open_cv=False):

    img = image_noise_removal_contrast(image_path, open_cv=open_cv)

    if mask:
        height, width = img.shape[0:2]
        if mask == MASK_BOTTOM:
            mask = create_image(width, height - start_point - 1)
            img[start_point + 1:height, 0:width] = mask
        elif mask == MASK_TOP:
            mask = create_image(width, start_point - 1)
            img[0:start_point - 1, 0:width] = mask
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
