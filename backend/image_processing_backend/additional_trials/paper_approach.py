import cv2
import numpy as np

img = cv2.imread(
    '/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/fwdsamplefiles/live_sample.jpg')
index_to_find = 1


def find_black_pixels_height(image_file, index_value, opencv_image=False):
    img = cv2.imread(image_file, 0) if not opencv_image else image_file
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img

    row_index = 1
    for i in range(0, img.shape[0] - 1, 1):
        print(i)
        pixel_list = []
        for j in range(img.shape[1] - 1):
            pixel_list.append(img[i, j])
        key = 0
        left_pixel = 0
        for index, item in enumerate(pixel_list):
            if row_index % 2 == 1 and item < 100:
                if not left_pixel:
                    left_pixel = index
                key += 1
                if key > 0.07 * img.shape[1]:
                    row_index += 1
                    if index_value == row_index - 1:
                        return left_pixel, i, index
            elif row_index % 2 == 0 and item > 150:
                if not left_pixel:
                    left_pixel = index
                key += 1
                if key > 0.90 * img.shape[1]:
                    row_index += 1
                    if index_value == row_index - 1:
                        return left_pixel, i, index


left, top, right = find_black_pixels_height(img, index_to_find, opencv_image=True)
# if index_to_find % 2 == 0:
#     _, nearest_top, _ = find_black_pixels_height(img, index_to_find + 1, opencv_image=True)
# else:
#     _, nearest_top, _ = find_black_pixels_height(img, index_to_find - 1, opencv_image=True)

print(left, top, right)

points = np.array([[left, top], [img.shape[1], top]])

cv2.polylines(img, np.int32([points]), 1, (0, 255, 0), thickness=3)

cv2.imwrite('saved.png', img)


def find_new_points(image_file, opencv_image=False, top=None, bottom=None):
    img = cv2.imread(image_file, 0) if not opencv_image else image_file

    new_points_list = []
    for j in range(img.shape[1] - 1):
        points_list = []
        pixel_list = []
        for i in range(65):
            points_list.append([j, top + i])
            pixel_list.append(img[top + i, j])
            # print(img[top+i, j])
        if min(pixel_list) < 150:
            min_point_index = pixel_list.index(min(pixel_list))
            new_points_list.append(points_list[min_point_index])
        else:
            new_points_list.append([j, top])

    new_points = np.array(new_points_list)
    # img = cv2.imread('/home/kanish/Desktop/image.png')
    cv2.polylines(img, np.int32([new_points]), 1, (0, 0, 0), thickness=4)

    cv2.imwrite(f'saved_new_latest_.png', img)


img = cv2.imread(
    '/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/fwdsamplefiles/live_sample.jpg', 0)
find_new_points(img, opencv_image=True, top=top)

# new_points = np.array(points_list)
# cv2.polylines(img, np.int32([new_points]), 1, (255, 255, 0), thickness=5)
#
# cv2.imwrite('saved_new.png', img)


# cropped_image 0.985
# sample image 0.96
