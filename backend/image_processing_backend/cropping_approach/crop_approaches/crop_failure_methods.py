from cropping_approach.image_preprocessing.image_utils import increase_contrast_pil
from cropping_approach.constants.config_fields_constants import SAVED_PATH


def crop_failure_image_enhancement(image_path):
    image = increase_contrast_pil(image_path, factor=50.0,
                                  should_save=True,
                                  save_folder='/home/kanish/Desktop/new_forms_output_folder/out',
                                  file_name='test', file_extension='.png')

    return image[SAVED_PATH]
