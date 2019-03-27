import numpy as np
import time
import cv2
import traceback

from PIL import Image as im
from PIL import ImageEnhance
from scipy.ndimage import interpolation as inter

from cropping_approach.utils.dir_utils import DirUtil
from cropping_approach.constants.constants import NUMPY_ARRAY, SAVED_PATH, PIL_IMAGE_OBJECT


def scale_image(image, opencv_image=False, scaling_factor=2, file_name=None,
                file_extension=None, should_save=False, save_folder=None):
    img = cv2.imread(image) if not opencv_image else image

    height, width = img.shape[:2]
    res = cv2.resize(img, (scaling_factor * width, scaling_factor * height), interpolation=cv2.INTER_LINEAR)

    if should_save:
        image_name = '{}{}'.format(file_name, file_extension)

        DirUtil().create_directory(save_folder)
        saved_path = save_folder + '/{}'.format(image_name)

        cv2.imwrite(saved_path, res)
        return {SAVED_PATH: saved_path, NUMPY_ARRAY: res}

    return {SAVED_PATH: None, NUMPY_ARRAY: res}


def find_contours(image, opencv_image=False,
                  join_horizontal_pixels=False,
                  join_vertical_pixels=False,
                  kernal=5, iterations=2, noise_kernal=2,
                  horizontal_kernal=5, vertical_kernal=5,
                  mode=cv2.RETR_EXTERNAL,
                  approx=cv2.CHAIN_APPROX_NONE,
                  threshold=cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU):

    im = cv2.imread(image) if not opencv_image else image

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) if len(im.shape) == 3 else im

    blur = cv2.GaussianBlur(gray, (kernal, kernal), 0)
    ret2, threshed = cv2.threshold(blur, 0, 255, threshold)

    # (1) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (noise_kernal, noise_kernal))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    if join_horizontal_pixels:
        kernel = np.ones((1, horizontal_kernal), np.uint8)  # note this is a horizontal kernel
        morphed = cv2.morphologyEx(morphed, cv2.MORPH_CLOSE, kernel, iterations=iterations)

    if join_vertical_pixels:
        kernel = np.ones((vertical_kernal, 1), np.uint8)  # note this is a vertical kernel
        morphed = cv2.morphologyEx(morphed, cv2.MORPH_CLOSE, kernel, iterations=iterations - 1)

    # cv2.imwrite('edited.png', morphed)

    # (2) Find the contours
    image, cnts, _ = cv2.findContours(morphed, mode, approx)

    return image, cnts


def opencv_rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def increase_contrast_pil(image_file, factor=3.0, pil_image=False, save_folder=None,
                          file_name=None, file_extension=None, should_save=False):
    p_image = im.open(image_file) if not pil_image else image_file
    pil_image = p_image.convert("RGBA")
    image = ImageEnhance.Contrast(pil_image).enhance(factor)
    image = image.convert('RGB')
    if should_save:
        DirUtil().create_directory(save_folder)
        saved_path = '{}/{}{}'.format(save_folder, file_name, file_extension)
        image.save(saved_path)

        return {SAVED_PATH: saved_path, PIL_IMAGE_OBJECT: image}

    return {SAVED_PATH: None, PIL_IMAGE_OBJECT: image}


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


def find_lower_black_pixels_height(image_file, opencv_image=False):
    print('Finding black pixels in a line...........!!!!!')
    image_in = cv2.imread(image_file, 0) if not opencv_image else image_file
    image_in = cv2.cvtColor(image_in, cv2.COLOR_BGR2GRAY) if len(image_in.shape) == 3 else image_in

    for i in range(image_in.shape[0] - 1, 1, -1):
        pixel_list = []
        for j in range(image_in.shape[1]):
            pixel_list.append(image_in[i, j])
        key = 0
        for item in pixel_list:
            if item < 100:
                key += 1
                if key > 0.70 * image_in.shape[1]:
                    return i


def convert_cv2_image_to_pil_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    pil_image = im.fromarray(img)
    return pil_image


def convert_pil_image_to_cv2_image(image):
    cv2_image = np.asarray(image)
    return cv2_image


def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))


def skew_corr(img, file_name=None, file_extension=None, opencv_image=False,
              should_save=False, save_folder=None):
    """
    Function for skew correction

    Returns:
        [image] -- returns skew corrected image
    """

    # image = Image.open(img)
    cv_img = cv2.imread(img) if not opencv_image else img
    image = convert_cv2_image_to_pil_image(cv_img)

    # convert to binary
    wd, ht = image.size
    pix = np.array(image.convert('1').getdata(), np.uint8)
    bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)

    # plt.imshow(bin_img, cmap='gray')
    # plt.savefig('binary.png')

    def find_score(arr, angle):
        data = inter.rotate(arr, angle, reshape=False, order=0)
        hist = np.sum(data, axis=1)
        score = np.sum((hist[1:] - hist[:-1]) ** 2)
        return hist, score

    delta = .2
    limit = 5
    angles = np.arange(-limit, limit + delta, delta)
    scores = []
    for angle in angles:
        hist, score = find_score(bin_img, angle)
        scores.append(score)

    best_score = max(scores)
    best_angle = angles[scores.index(best_score)]
    print('Best angle: {}'.format(best_angle))

    # correct skew
    print('Skew Corrected for :', img)
    # img2 = cv2.imread(img)
    rotated_image = rotate_bound(cv_img, -best_angle)

    if should_save:
        image_name = '{}{}'.format(file_name, file_extension)

        DirUtil().create_directory(save_folder)
        saved_path = save_folder + '/{}'.format(image_name)

        cv2.imwrite(saved_path, rotated_image)

        return {SAVED_PATH: saved_path, NUMPY_ARRAY: rotated_image}

    return {SAVED_PATH: None, NUMPY_ARRAY: rotated_image}


def denoising_image(image_file, opencv_image=False, file_name=None, file_extension=None,
                    should_save=False, save_folder=None, denoising_params=(45, 13, 31)):
    image_in = cv2.imread(image_file, 0) if not opencv_image else image_file
    (h, templateWindowSize, searchWindowSize) = denoising_params

    denoised_gray = cv2.fastNlMeansDenoising(image_in, None, h,
                                             templateWindowSize, searchWindowSize)

    if should_save:
        image_name = '{}{}'.format(file_name, file_extension)

        DirUtil().create_directory(save_folder)
        saved_path = save_folder + '/{}'.format(image_name)

        cv2.imwrite(saved_path, denoised_gray)

        return {SAVED_PATH: saved_path, NUMPY_ARRAY: denoised_gray}

    return {SAVED_PATH: None, NUMPY_ARRAY: denoised_gray}


def remove_vertical_lines(image_file, opencv_image=False, file_name=None, file_extension=None,
                          should_save=False, save_folder=None):
    print('Remove vertical lines in an image...........!!!!!')
    image_in = cv2.imread(image_file, 0) if not opencv_image else image_file
    image_in = cv2.cvtColor(image_in, cv2.COLOR_BGR2GRAY) if len(image_in.shape) == 3 else image_in

    for i in range(0, image_in.shape[1] - 1, 1):
        pixel_list = []
        for j in range(image_in.shape[0] - 1):
            pixel_list.append(image_in[j, i])
        key = 0
        for item in pixel_list:
            if item < 100:
                key += 1
                if key > 0.60 * image_in.shape[0]:
                    for j in range(image_in.shape[0] - 1):
                        image_in[j, i] = 255

    if should_save:
        image_name = '{}{}'.format(file_name, file_extension)

        DirUtil().create_directory(save_folder)
        saved_path = save_folder + '/{}'.format(image_name)

        cv2.imwrite(saved_path, image_in)
        return {SAVED_PATH: saved_path, NUMPY_ARRAY: image_in}

    return {SAVED_PATH: None, NUMPY_ARRAY: image_in}


def is_box_blank(image_path, opencv_image=False):
    img = cv2.imread(image_path) if not opencv_image else image_path
    image_in = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE) if len(image_path.shape) == 3 else image_path
    height, width = image_in.shape[:2]

    area = height * width
    n_black_pix = np.sum(image_in < 110)

    # print('Number of total pixels:', area)
    # print('Number of black pixels:', n_black_pix)

    if (n_black_pix / area) < 0.035:
        return True

    return False
