from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import cv2
import numpy as np
import pandas as pd

# from sauvola import binarize


def compute_pixels(img):

    new_img = img >= 120

    c = new_img.astype(int)

    return c


def new_function():
    img = cv2.imread('/home/kanish/Desktop/image_processing_proj/backend/image_processing_backend/scipy_approaches/saved.png', 0)

    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_OTSU)

    img = thresh1
    immap = compute_pixels(img)

    # matrix = [
    #   [1, 1, 1],
    #   [1, 0, 1],
    #   [1, 1, 1]
    # ]

    grid = Grid(matrix=immap)
    start = grid.node(0, 77)
    end = grid.node(img.shape[1] - 1, 77)

    finder = AStarFinder(weight=1)
    print('finding path')
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(path)
    points = np.array(path)

    cv2.polylines(img, np.int32([points]), 0, (0, 255, 0), thickness=3)

    cv2.imwrite('saved_new_2.png', img)

new_function()
