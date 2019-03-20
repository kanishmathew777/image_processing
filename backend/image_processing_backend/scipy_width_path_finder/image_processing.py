import cv2
import numpy as np

from scipy_width_path_finder.image_preprocessing.image_utils import convert_cv2_image_to_pil_image, increase_contrast_pil, \
    convert_pil_image_to_cv2_image


def image_noise_removal_contrast(image_path, open_cv=False):
    img = cv2.imread(image_path, 0) if not open_cv else image_path

    contrast_params = {'should_save': True, 'save_folder': '/home/kanish/Desktop/scipy_contrast_folder',
                       'file_extension': '.png', 'file_name': 'contrsased'}

    pil_image = convert_cv2_image_to_pil_image(img)

    contrast_factor = 50.0
    contrast_pil_image = increase_contrast_pil(pil_image, factor=contrast_factor,
                                               pil_image=True, **contrast_params)

    contrast_cv_image = convert_pil_image_to_cv2_image(contrast_pil_image["image_object"])

    img = cv2.cvtColor(contrast_cv_image, cv2.COLOR_BGR2GRAY)

    # cv2.imwrite("before.png", img)
    #
    # img_not = cv2.bitwise_not(img)

    # kernel = np.ones((5, 5), np.uint8)/25

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

    dilation = cv2.dilate(img, kernel, iterations=1)

    # thresh1 = cv2.dilate(img_not, kernel, iterations=2)
    #
    # blur = cv2.GaussianBlur(img, (5, 5), 0)

    # cv2.imwrite("eclipse.png", dilation)

    # thresh1 = cv2.bitwise_not(thresh1)

    # thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 151, 21)

    return dilation


image_path = "/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/athul_scanned/527/527_8.png"
image_noise_removal_contrast(image_path, open_cv=False)