# common imports
import cv2
import numpy as np

# increase_contrast_pil function imports
from PIL import Image as im
from PIL import ImageEnhance

# other imports
from cropping_approach.utils.dir_utils import DirUtil


def draw_and_crop_contour(original_image, cordinates, border_added=0, opencv_image=False,
                          box=None, draw_box=True, box_cordinates=False):
    original_image = original_image if opencv_image else cv2.imread(original_image)

    height, width = original_image.shape[:2]
    if draw_box:
        cv2.drawContours(original_image, [box], 0, (0, 0, 0), 2)

    x = cordinates[0]
    y = cordinates[1]

    if box_cordinates:
        w = cordinates[2] - cordinates[0]
        h = cordinates[3] - cordinates[1]
    else:
        w = cordinates[2]
        h = cordinates[3]

    height_to_crop = y + h + border_added
    width_to_crop = x + w + border_added
    if y + h + border_added > height:
        height_to_crop = height
    if x + w + border_added > width:
        width_to_crop = width
    if x - border_added < 0 or y - border_added < 0:
        border_added = 0

    dst = original_image[y - border_added:height_to_crop, x - border_added:width_to_crop]

    return dst


def lines_inside_image(image_file, opencv_image=False, minLineLength=70, maxLineGap=30):

    proc_img = cv2.imread(image_file) if not opencv_image else image_file

    gray = cv2.cvtColor(proc_img, cv2.COLOR_BGR2GRAY) if len(proc_img.shape) == 3 else proc_img

    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    vertical_lines = cv2.HoughLinesP(edges, 1, np.pi / 2, threshold=80, minLineLength=minLineLength,
                                     maxLineGap=maxLineGap)

    return vertical_lines


def increase_contrast_pil(image_file, pil_image=False, save_folder=None,
                          image_name=None, should_save=True, factor=50.0):

    p_image = im.open(image_file) if not pil_image else image_file
    pil_image = p_image.convert("RGBA")
    image = ImageEnhance.Contrast(pil_image).enhance(factor)
    image = image.convert('RGB')

    if should_save:
        DirUtil().create_directory(save_folder)
        saved_path = save_folder + '/{}.png'.format(image_name)
        image.save(saved_path)

        return saved_path, image

    return None, image
