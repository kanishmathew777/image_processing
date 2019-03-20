import cv2
import numpy as np


def find_contours_in_image(image, opencv_image=False, join_lines=False, kernal=5,
                           thresholding=cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,
                           retrievelmode=cv2.RETR_EXTERNAL,
                           approximation_method=cv2.CHAIN_APPROX_NONE):

    im = cv2.imread(image) if not opencv_image else image

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) if len(im.shape) == 3 else im

    # blur = cv2.GaussianBlur(gray, (1, 1), 0)
    blur = cv2.GaussianBlur(gray, (kernal, kernal), 0)
    ret2, threshed = cv2.threshold(blur, 0, 255, thresholding)

    # (1) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    if join_lines:
        kernel = np.ones((1, 5), np.uint8)  # note this is a horizontal kernel
        morphed = cv2.morphologyEx(morphed, cv2.MORPH_CLOSE, kernel, iterations=2)

        kernel = np.ones((5, 1), np.uint8)  # note this is a vertical kernel
        morphed = cv2.morphologyEx(morphed, cv2.MORPH_CLOSE, kernel, iterations=1)

    # (2) Find the contours
    image, cnts, hierarchy = cv2.findContours(morphed, retrievelmode, approximation_method)

    return image, cnts, hierarchy


def draw_cordinates(image, contours, colors=(0, 0, 0), index=-1, thickness=2,
                    opencv_image=False, contour_sorting=True):

    img = cv2.imread(image) if not opencv_image else image

    cnts = sorted(contours, key=cv2.contourArea, reverse=contour_sorting)

    if len(cnts) > index:
        cv2.drawContours(img, cnts, index, colors, thickness)
        print(cv2.contourArea(cnts[index]))
    else:
        raise ValueError('Index range is greater than total,  {} - contours detected'.format(len(cnts)))
    # cv2.drawContours(img, cnts, -1, (0,255,0), 5)

    return img


