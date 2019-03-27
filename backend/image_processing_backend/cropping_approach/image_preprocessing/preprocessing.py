import traceback

from cropping_approach.utils.dir_utils import DirUtil
from cropping_approach.image_preprocessing.image_utils import remove_vertical_lines, skew_corr,\
    scale_image, convert_cv2_image_to_pil_image, increase_contrast_pil, convert_pil_image_to_cv2_image, \
    denoising_image
from cropping_approach.constants.constants import NUMPY_ARRAY, SAVED_PATH, PIL_IMAGE_OBJECT


def image_pre_processing(image_path, save_folder, temperory_save=False):
    # get file name and extension
    file_extension = DirUtil().get_file_extension(image_path)
    file_name = DirUtil().get_file_name_without_ext(image_path)

    # params for functions
    vertical_line_params = {}
    skew_params = {}
    scale_params = {}
    contrast_params = {}
    denoised_params = {}

    if temperory_save:
        vertical_save_folder = "{}/vertical_lines_removed".format(save_folder)
        vertical_line_params = {'should_save': temperory_save, 'save_folder': vertical_save_folder,
                                'file_extension': file_extension, 'file_name': file_name}

        skew_saved_folder = "{}/skew_saved_folder".format(save_folder)
        skew_params = {'should_save': temperory_save, 'save_folder': skew_saved_folder,
                       'file_extension': file_extension, 'file_name': file_name}

        scale_save_folder = "{}/scale_saved_folder".format(save_folder)
        scale_params = {'should_save': temperory_save, 'save_folder': scale_save_folder,
                        'file_extension': file_extension, 'file_name': file_name}

        contrast_folder = "{}/contrast_folder".format(save_folder)
        contrast_params = {'should_save': temperory_save, 'save_folder': contrast_folder,
                           'file_extension': file_extension, 'file_name': file_name}

        denoised_save_folder = "{}/denoised_folder".format(save_folder)
        denoised_params = {'should_save': temperory_save, 'save_folder': denoised_save_folder,
                           'file_extension': file_extension, 'file_name': file_name}

    vertical_lines = remove_vertical_lines(image_path, opencv_image=False, **vertical_line_params)

    print('skew correction.....!!!!')

    try:
        skew_corrected_image = skew_corr(vertical_lines[NUMPY_ARRAY], opencv_image=True, **skew_params)
    except Exception as e:
        print("skew exception")
        print(e)
        _traceback = traceback.format_exc()
        print(str(_traceback))

    print("scaling and increase contrast....!!!")

    scaled_image = scale_image(skew_corrected_image[NUMPY_ARRAY],
                               opencv_image=True, **scale_params)

    scaled_pil_image = convert_cv2_image_to_pil_image(scaled_image[NUMPY_ARRAY])

    contrast_factor = 2.0
    contrast_pil_image = increase_contrast_pil(scaled_pil_image, factor=contrast_factor,
                                               pil_image=True, **contrast_params)

    contrast_cv_image = convert_pil_image_to_cv2_image(contrast_pil_image[PIL_IMAGE_OBJECT])

    contrast_image = {SAVED_PATH: contrast_pil_image[SAVED_PATH], NUMPY_ARRAY: contrast_cv_image}

    print("denoising.....!!!")
    # denoised_gray = cv2.imread('path')

    denoised_gray = denoising_image(contrast_image[NUMPY_ARRAY], opencv_image=True,
                                    denoising_params=(25, 13, 35), **denoised_params)

    # cv2.imwrite('path', denoised_gray)
    return {'skewed_image': skew_corrected_image, 'scaled_image': scaled_image,
            'contrast_image': contrast_image, 'de_noised_image': denoised_gray}
