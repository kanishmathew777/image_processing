import cv2
import numpy as np
from cropping_new_approach.sort_contours import sort_contours

# img_for_box_extraction_path = '/home/kanish/Desktop/image_processing_proj/backend/image_processing_backend/new_form-1.png'
cropped_dir_path = '/home/kanish/Desktop/output_folder/{}'

image_saved_path = '/home/kanish/Desktop/image_processing_proj/backend/image_processing_backend/new_form-1.png'

# Read the image
img = cv2.imread(image_saved_path, 0)

# Thresholding the image
(thresh, img_bin) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# Invert the image
img_bin = 255 - img_bin
cv2.imwrite("Image_bin.jpg", img_bin)

# Defining a kernel length
hor_kernel_length = np.array(img).shape[1] // 80

ver_kernal_length = np.array(img).shape[1] // 120

# A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, ver_kernal_length))

# A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (hor_kernel_length, 1))

# A kernel of (3 X 3) ones.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Morphological operation to detect vertical lines from an image
img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)

# ####   edited
# kernel = np.ones((7, 1), np.uint8)  # note this is a vertical kernel
# img_temp1 = cv2.morphologyEx(img_temp1, cv2.MORPH_CLOSE, kernel, iterations=1)

verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
cv2.imwrite("verticle_lines.jpg", verticle_lines_img)


# Morphological operation to detect horizontal lines from an image
img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
cv2.imwrite("horizontal_lines.jpg", horizontal_lines_img)

# Weighting parameters, this will decide the quantity of an image to be added to make a new image.
alpha = 0.5
beta = 1.0 - alpha


# This function helps to add two image with specific weight parameter to get a third image as summation of two image.
img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
(thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite("img_final_bin.jpg", img_final_bin)

# Find contours for image, which will detect all the boxes
im2, contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort all the contours by top to bottom.
(contours, boundingBoxes) = sort_contours(contours)

idx = 0
for c, boxes in zip(contours, boundingBoxes):
    # Returns the location and width,height for every contour
    x, y, w, h = cv2.boundingRect(c)

    # x, y, w, h = boxes

    print(x, y)
    # # If the box height is greater then 20, width is > 80, then only save it as a box in "cropped/" folder.
    if (w > int(0.30*im2.shape[1]) and h > int(0.10*im2.shape[0])) and w > 3 * h:
        idx += 1
        new_img = img[y:y + h, x:x + w]
        cv2.imwrite(cropped_dir_path.format(str(idx) + '.png'), new_img)
