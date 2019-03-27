from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import cv2
import numpy as np
import pandas as pd

from sauvola import binarize


def compute_pixels(img):

    new_img = img >= 120

    c = new_img.astype(int)

    return c


def new_function():
    img = cv2.imread('/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/fwdsamplefiles/libe_sample_down.jpg', 0)

    # imbw = binarize(img, [20, 20], 150, 0.3)

    immap = compute_pixels(img)

    # immap = np.zeros((imbw.shape), dtype=np.int32)
    #
    # print(immap)
    # np.save('test', immap)

    # matrix = [
    #   [1, 1, 1],
    #   [1, 0, 1],
    #   [1, 1, 1]
    # ]

    grid = Grid(matrix=immap)
    start = grid.node(0, 382)
    end = grid.node(img.shape[1] - 1, 382)

    finder = AStarFinder(weight=1)
    print('finding path')
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(path)
    points = np.array(path)

    cv2.polylines(img, np.int32([points]), 1, (0, 255, 0), thickness=3)

    cv2.imwrite('saved_new_2.png', img)
    # data = grid.grid_str(path=path, start=start, end=end)
    # print(data)
    #
    # with open('new_file.txt', 'w') as file:
    #     file.write(data)


new_function()
