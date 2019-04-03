import cv2
import json


img = cv2.imread("image_path")

with open('json_file') as json_file:
    data = json.load(json_file)

    for index, boxes in enumerate(data):
        print(boxes)
        crop_img = img[boxes["start_y"]:boxes["end_y"], boxes["start_x"]:boxes["end_x"]]
        cv2.imwrite(f"cropped_{index}.png", crop_img)
