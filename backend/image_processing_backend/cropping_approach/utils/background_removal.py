import subprocess
import cv2
import os

from .dir_utils import DirUtil
from .image_utils import draw_and_crop_contour

box_folder = 'Box_files_folder'


def generate_box_file(image_file, output_folder):
    box_file_name = DirUtil().get_file_name_without_ext(image_file)
    DirUtil().create_directory(os.path.join(output_folder, box_folder))
    subprocess.call('tesseract {} {}/{}/{} batch.nochop makebox'.
                    format(image_file, output_folder, box_folder, box_file_name), shell=True)

    return "{}/{}/{}.box".format(output_folder, box_folder, box_file_name)


def crop_using_box_file(output_folder, box_file, image_absolute_path):
    image_name = DirUtil().get_file_name_with_extension(image_absolute_path)
    result_file = "{}/{}".format(output_folder, image_name)

    img = cv2.imread(image_absolute_path)
    print(img.shape)
    file = open(box_file, encoding="utf-8")

    lines_splited = []
    for lines in file.read().split('\n'):
        lines_splited.append(lines.split(' '))

    convert_string_to_int = [[int(line[1]), int(line[2]), int(line[3]), int(line[4])] for line in lines_splited
                             if len(line) == 6 and int(line[2]) != 0 and int(line[4]) != 0]

    x1 = min(x[0] for x in convert_string_to_int)
    y1 = img.shape[0] - max(x[3] for x in convert_string_to_int)

    x2 = max(x[2] for x in convert_string_to_int)
    y2 = img.shape[0] - min(x[1] for x in convert_string_to_int)

    small_border = 2

    x1 = x1 if not x1 else x1 - small_border
    y1 = y1 if not y1 else y1 - small_border
    x2 = x2 if not x2 else x2 + small_border
    y2 = y2 if not y2 else y2 + small_border

    crop_cordinates = (x1, y1, x2, y2)

    print(crop_cordinates)

    processed_dst = draw_and_crop_contour(img, crop_cordinates, border_added=0, opencv_image=True,
                                          draw_box=False, box_cordinates=True)

    cv2.imwrite(result_file, processed_dst, )

    return result_file


def tesseract_border_removal(image_file, output_folder):
    box_file_absolute_path = generate_box_file(image_file, output_folder)
    return crop_using_box_file(output_folder, box_file=box_file_absolute_path, image_absolute_path=image_file)
