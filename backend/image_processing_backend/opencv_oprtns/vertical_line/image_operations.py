import cv2
import numpy as np


def vertical_lines(img, percentage_line_length):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi, int(0.85 * (img.shape[0])))

    if lines is not None and lines.any():
        for line in lines:
            for rho, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)

                x0 = a * rho
                y0 = b * rho

                line_length = img.shape[0]

                x1 = int(x0 + line_length * (-b))
                y1 = int(y0 + line_length * (a)) if y0 != 0.0 else 0
                x2 = int(x0 - line_length * (-b))
                y2 = int(y0 - line_length * (a)) if y0 != 0.0 else img.shape[0]

                if (0.10 * (img.shape[1])) < x1 < (0.90 * (img.shape[1])):
                    crop_cord_list.append([x1, y1, x2, y2])

    else:
        raise ImageProcessingError('Vertically dividing was not possible')
    if not crop_cord_list:
        raise ImageProcessingError('Vertically dividing was not possible')
