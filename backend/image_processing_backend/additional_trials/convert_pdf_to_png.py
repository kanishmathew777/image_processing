import subprocess
import time
from cropping_approach.image_preprocessing.image_utils import increase_contrast_pil


def convert_pdf_to_image(pdf, image_name):
    subprocess.call(['convert', '-version'])

    subprocess.call(['gs', '-dNOPAUSE', '-dBATCH', '-sDEVICE=tiff24nc', '-sCompression=lzw',
                     '-r200', '-sOutputFile={}-%d.png'.format(image_name), "%s" % pdf])
    time.sleep(2)

    print('pdf conversion completed')

increase_contrast_pil('/home/kanish/Documents/ICR advanced forms/cropped.png', factor=50.0, save_folder='/home/kanish/Desktop/image_processing_proj/backend/image_processing_backend/additional_trials',
                      file_name='increase', file_extension='.png', should_save=True)


# convert_pdf_to_image('/home/kanish/Documents/ICR advanced forms/BC Palliative Care Benefits Registration (HLTH 349) - Handwritten.pdf',
#                      'advanced_form')