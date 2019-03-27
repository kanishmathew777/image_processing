import cv2
from plantcv import plantcv as pcv

img, path, filename = pcv.readimage('/home/kanish/Desktop/image.png')

img1 = pcv.white_balance(img, roi=(400, 800, 200, 200))

s_thresh = pcv.threshold.binary(~img, 85, 255, 'light')
cv2.imwrite('test.png', s_thresh)

dilated = pcv.dilate(s_thresh, 1, 1)
cv2.imwrite('dilated.png', dilated)

id_objects, obj_hierarchy = pcv.find_objects(img1, dilated)

print('Haii')