import numpy as np
import cv2
import random


def create_image(width, height, color=0, save_image=False):
    img = np.zeros([height, width], dtype=np.uint8)
    img.fill(color)

    if save_image:
        cv2.imwrite(f'new_blank {random.randint(0, 15)}.png', img)

    return img


# image_path = "/home/kanish/Desktop/cropped.png"
#
# img = cv2.imread(image_path, 0)
# height, width = img.shape[0:2]
# mask = create_image(width, height-63, save_image=True)
#
# img[63:height, 0:width] = mask
#
# cv2.imwrite('res.png', img)
