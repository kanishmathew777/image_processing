import cv2
import numpy as np
from PIL import Image as im
from PIL import ImageEnhance

from utils.dir_utils import DirUtil


def increase_contrast_pil(image_file, pil_image=False, save_folder=None,
                          image_name=None, should_save=True, factor=50.0):

    p_image = im.open(image_file) if not pil_image else image_file
    print(p_image.mode)
    pil_image = p_image.convert("RGBA")
    # image = ImageEnhance.Brightness(pil_image).enhance(25.0)
    contrast = ImageEnhance.Contrast(p_image)
    image = contrast.enhance(factor)
    image = image.convert('RGB')

    if should_save:
        DirUtil().create_directory(save_folder)
        saved_path = save_folder + '/{}.png'.format(image_name)
        image.save(saved_path)

        return saved_path, image

    return None, image


def increase_contrast_opencv():
    alpha = 2.0  # Simple contrast control Enter the alpha value [1.0-3.0]
    beta = 80  # Simple brightness control Enter the beta value [0-100]

    image = cv2.imread('/home/kanish/Desktop/image_processing_proj/backend/image_processing_backend/new_form-1.png')
    new_image = np.zeros(image.shape, image.dtype)

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)

    image_save_path = '/home/kanish/Desktop/output_folder/contrast.png'
    cv2.imwrite(image_save_path, new_image)

    return image_save_path
