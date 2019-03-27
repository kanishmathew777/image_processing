import cv2
import numpy as np
import copy

from functools import partial

from cropping_approach.utils.dir_utils import DirUtil
from cropping_approach.constants.config_fields_constants import NAME, FIELDS, PROCESS, PROCESS_PARAMS, CROPPED_STATUS, \
    RESULT, SAVED_PATH, SAVED_FOLDER, NUMPY_ARRAY, PARENT, VERTICAL_HORIZONTAL_COMBINE_APPROACH, CONTOUR_APPROACH, \
    CONTOUR_SORT_APPROACH, APPROACH

from cropping_approach.cropping_config_file.config_file import initialise_form_config, get_field_index

# for contour approach
from cropping_approach.image_preprocessing.image_utils import find_contours, draw_and_crop_contour

# for vertical-horizontal lin approach
from cropping_approach.utils.sort_contours import sort_contours

from .crop_failure_methods import crop_failure_image_enhancement
from .process_comments import process_status


class ContourApproach:

    def __init__(self, result_folder, image_path, form_name, save_in_folder=False):
        self.result_folder = result_folder
        self.image_path = image_path
        self.save_in_folder = save_in_folder
        self.form_name = form_name
        self.form_configure = initialise_form_config(image_path=self.image_path,
                                                     output_folder=self.result_folder,
                                                     form_name=self.form_name)

    def get_process(self, process, index, parent_index=None):
        switch = {
            CONTOUR_APPROACH: partial(self.crop_contours, index),
            VERTICAL_HORIZONTAL_COMBINE_APPROACH: partial(self.vertical_horizontal_approach, index),
            CONTOUR_SORT_APPROACH: partial(self.contours_sort_process, index, parent_index)
        }

        func = switch.get(process, lambda: False)

        return func()

    def crop_fields(self):
        for index, field in enumerate(self.form_configure[FIELDS]):
            if self.form_configure[FIELDS][index][PARENT] is None and \
                    self.form_configure[FIELDS][index][RESULT][NUMPY_ARRAY] is None:

                get_proccess_status = self.get_process(self.form_configure[FIELDS][index][PROCESS][APPROACH], index)

                if get_proccess_status:
                    self.form_configure[FIELDS][index][CROPPED_STATUS] = get_proccess_status
                else:
                    print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][index][NAME],
                                         f"Retrying with image enhancements "))

                    self.image_path = crop_failure_image_enhancement(self.image_path)
                    self.form_configure[FIELDS][index][CROPPED_STATUS] = \
                        self.get_process(self.form_configure[FIELDS][index][PROCESS][APPROACH], index)

            elif self.form_configure[FIELDS][index][RESULT][NUMPY_ARRAY] is None:
                parent_index = get_field_index(self.form_configure[FIELDS][index][PARENT],
                                               form_name=self.form_name)
                if parent_index is not None and self.form_configure[FIELDS][parent_index][CROPPED_STATUS]:
                    self.form_configure[FIELDS][index][CROPPED_STATUS] = self.contours_sort_process(index, parent_index)

    def crop_contours(self, field_index):
        """
            Finding and cropping sections using contour approach

        :param field_index: the field to be cropped
        :return: True or False with the crop status
        """

        print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                             f"Cropping using {self.form_configure[FIELDS][field_index][PROCESS][APPROACH]}"))

        image = cv2.imread(self.image_path)

        img_height, img_width = image.shape[:2]

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image

        image, cnts = find_contours(gray, opencv_image=True)

        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)

        max_contour_area = img_height * img_width
        # max_contour_perimeter = cv2.arcLength(cnt[0], True)

        for index in range(0, 3):
            contour = cnt[index]
            contour_area = cv2.contourArea(contour)

            if contour_area > (max_contour_area * self.form_configure[FIELDS][field_index][PROCESS]
            [PROCESS_PARAMS]["contour_min_area"]):
                x, y, w, h = cordinates = cv2.boundingRect(cnt[index])

                top_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["top_distance"]
                bottom_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["bottom_distance"]

                if top_distance * img_height < y and y + h < bottom_distance * img_height:
                    org_dst = draw_and_crop_contour(self.image_path, cordinates, border_added=10,
                                                    draw_box=False)
                    self.form_configure[FIELDS][field_index][RESULT][NUMPY_ARRAY] = org_dst
                    # cv2.imwrite('contour-{}.png'.format(index), org_dst)
                    if self.save_in_folder:
                        DirUtil().create_directory(self.form_configure[FIELDS][field_index][RESULT][SAVED_FOLDER])
                        image_save_path = self.form_configure[FIELDS][field_index][RESULT][SAVED_PATH]
                        cv2.imwrite(image_save_path, org_dst)

                    print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                                         "Cropping SUCCESSFUL"))

                    return True

        print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                             "Cropping FAILED"))

        return False

    def vertical_horizontal_approach(self, field_index):

        print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                             f"Cropping using {self.form_configure[FIELDS][field_index][PROCESS][APPROACH]}"))

        # Read the image
        img = cv2.imread(self.image_path, 0)

        img_height, img_width = img.shape[:2]

        # Thresholding the image
        (thresh, img_bin) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Invert the image
        img_bin = 255 - img_bin

        # Defining a kernel length
        hor_kernel_length = np.array(img).shape[1] // 80

        ver_kernal_length = np.array(img).shape[1] // 140

        # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
        verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, ver_kernal_length))

        # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
        hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (hor_kernel_length, 1))

        # A kernel of (3 X 3) ones.
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        # Morphological operation to detect vertical lines from an image
        img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
        verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)

        # Morphological operation to detect horizontal lines from an image
        img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
        horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)

        # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
        alpha = 0.5
        beta = 1.0 - alpha

        # This function helps to add two image with specific weight parameter to get a third image as
        # summation of two image.
        img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0)
        img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
        (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        cv2.imwrite('final.png', img_final_bin)

        image, cnts = find_contours(img_final_bin, opencv_image=True)

        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)
        max_contour_area = img_height * img_width

        total_cnts = 3 if len(cnts) > 3 else len(cnts)

        for index in range(0, total_cnts):
            contour = cnt[index]
            contour_area = cv2.contourArea(contour)

            if contour_area > (max_contour_area * self.form_configure[FIELDS][field_index][PROCESS]
            [PROCESS_PARAMS]["contour_min_area"]):
                x, y, w, h = cordinates = cv2.boundingRect(cnt[index])
                top_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["top_distance"]
                bottom_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["bottom_distance"]

                if top_distance * img_height <= y and y + h <= bottom_distance * img_height:
                    org_dst = draw_and_crop_contour(self.image_path, cordinates, border_added=10,
                                                    draw_box=False)
                    self.form_configure[FIELDS][field_index][RESULT][NUMPY_ARRAY] = org_dst
                    # cv2.imwrite('contour-{}.png'.format(index), org_dst)
                    if self.save_in_folder:
                        DirUtil().create_directory(self.form_configure[FIELDS][field_index][RESULT][SAVED_FOLDER])
                        image_save_path = self.form_configure[FIELDS][field_index][RESULT][SAVED_PATH]
                        cv2.imwrite(image_save_path, org_dst)

                    print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                                         "Cropping SUCCESSFUL"))

                    return True

        print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                             "Cropping FAILED"))

        return False

    def contours_sort_process(self, field_index, parent_index):

        print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                             f"Cropping using {self.form_configure[FIELDS][field_index][PROCESS][APPROACH]}"))

        img = self.form_configure[FIELDS][parent_index][RESULT][NUMPY_ARRAY]

        img_height, img_width = img.shape[:2]

        im2, cnts = find_contours(img, mode=cv2.RETR_TREE,
                                  approx=cv2.CHAIN_APPROX_NONE,
                                  threshold=cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU,
                                  kernal=1,
                                  opencv_image=True)

        cnts = [cnt for cnt in cnts if cv2.contourArea(cnt) >
                (self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS][
                     'contour_min_area'] * img_height * img_width)]

        cnts, bounding_boxes = sort_contours(cnts)

        sorted_boxes = None
        boxesfound = cnts

        if "inner_boxes" in self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]:
            sorted_boxes = []
            groups = dict()
            previous_dict_key = None

            min_height = 4  # org : 10

            for index, bounding_box in enumerate(bounding_boxes):
                if index + 1 == len(bounding_boxes):
                    if abs(bounding_box[1] - bounding_boxes[index - 1][1]) < min_height:
                        groups[previous_dict_key].append(bounding_box)
                    else:
                        groups[bounding_box[1]] = []
                        groups[bounding_box[1]].append(bounding_box)

                elif abs(bounding_box[1] - bounding_boxes[index + 1][1]) < min_height:
                    if not previous_dict_key in groups:
                        groups[bounding_box[1]] = []
                        previous_dict_key = bounding_box[1]
                    groups[previous_dict_key].append(bounding_box)
                else:
                    if previous_dict_key:
                        groups[previous_dict_key].append(bounding_box)
                    else:
                        previous_dict_key = bounding_box[1]
                        groups[previous_dict_key] = []
                        groups[previous_dict_key].append(bounding_box)
                    previous_dict_key = None

            group_length = len(groups)
            for index, key in enumerate(groups.keys()):
                if index+1 != group_length:
                    if key > self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["top_distance"] * \
                            img_height and list(groups)[index+1] < self.form_configure[FIELDS][field_index][PROCESS] \
                            [PROCESS_PARAMS]["bottom_distance"] * img_height:
                        sorted_boxes = sorted(groups[key], key=lambda value: value[0])
                        boxesfound = copy.deepcopy(sorted_boxes)
                        break
                elif key > self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["top_distance"] * img_height:
                    sorted_boxes = sorted(groups[key], key=lambda value: value[0])
                    boxesfound = copy.deepcopy(sorted_boxes)
                    break

                    # for box in sorted_boxes:
                    #     cordinates = box
                    #     org_dst = draw_and_crop_contour(img, cordinates, border_added=0,
                    #                                     draw_box=False, opencv_image=True)
                    #     cv2.imwrite('image_{}.png'.format(index), org_dst)
                    #     index += 1

        for index in range(0, len(boxesfound)):

            if sorted_boxes:
                x, y, w, h = cordinates = boxesfound[index]
            else:
                x, y, w, h = cordinates = bounding_boxes[index]

            print(x, y, w, h)

            org_dst = draw_and_crop_contour(img, cordinates, border_added=0,
                                            draw_box=False, opencv_image=True)
            cv2.imwrite('image_{}.png'.format(index), org_dst)

            top_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["top_distance"]
            bottom_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["bottom_distance"]
            left_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["left_distance"]
            right_distance = self.form_configure[FIELDS][field_index][PROCESS][PROCESS_PARAMS]["right_distance"]

            if y >= top_distance * img_height and y + h <= bottom_distance * img_height and \
                    x >= left_distance * img_width and x + w <= right_distance * img_width:

                org_dst = draw_and_crop_contour(img, cordinates, border_added=0,
                                                draw_box=False, opencv_image=True)

                # cv2.imwrite('image_{}.png'.format(index), org_dst)
                if self.save_in_folder:
                    DirUtil().create_directory(self.form_configure[FIELDS][field_index][RESULT][SAVED_FOLDER])
                    image_save_path = self.form_configure[FIELDS][field_index][RESULT][SAVED_PATH]
                    cv2.imwrite(image_save_path, org_dst)

                print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                                     "Cropping SUCCESSFUL"))

                return True

        print(process_status(self.form_configure[NAME], self.form_configure[FIELDS][field_index][NAME],
                             "Cropping FAILED"))

        return False
