import cv2
import shutil

from cropping_approach.image_preprocessing.preprocessing import image_pre_processing
from cropping_approach.crop_approaches.crop_methods import ContourApproach
from cropping_approach.utils.background_removal import tesseract_border_removal

from cropping_approach.utils.dir_utils import DirUtil
from cropping_approach.constants.constants import NUMPY_ARRAY

from cropping_approach.cropping_config_file.constant_form_names import *

input_image = '/home/kanish/Desktop/output_folder/box_completed/5.STAR_STENR/images/STENR-1.png'
output_folder = '/home/kanish/Desktop/new_forms_output_folder/'


def process(form_name):
    # file_name = DirUtil().get_file_name_with_extension(input_image)
    # temporary_save_folder = '{}{}_temperory_save'.format(output_folder, form_name)
    # DirUtil().create_directory(temporary_save_folder)
    #
    # PARENT_FOLDER = "{}{}/".format(output_folder, form_name)
    # DirUtil().create_directory(PARENT_FOLDER)
    #
    # # remove borders
    # saved_image_path = tesseract_border_removal(input_image, temporary_save_folder)
    #
    # # image pre processing
    # processed_image = image_pre_processing(image_path=saved_image_path,
    #                                        save_folder=temporary_save_folder,
    #                                        temperory_save=True)
    #
    # shutil.move(temporary_save_folder, PARENT_FOLDER)
    #
    # save_processed_path = '{}processed_{}'.format(PARENT_FOLDER, file_name)
    #
    # cv2.imwrite(save_processed_path, processed_image['de_noised_image'][NUMPY_ARRAY])

    save_processed_path = '/home/kanish/Desktop/new_forms_output_folder/MEDICAL_MMP4/processed_MMP4-1.png'

    # image cropping
    contour_approach = ContourApproach(image_path=save_processed_path,
                                       result_folder=output_folder,
                                       form_name=form_name,
                                       save_in_folder=True)

    contour_approach.crop_fields()


process(MEDICAL_MMP4)
