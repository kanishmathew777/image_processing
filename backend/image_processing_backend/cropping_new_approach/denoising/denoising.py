import numpy as np
import cv2

img = cv2.imread('/home/kanish/Desktop/output_folder/DENTAL_DTF/contrast.png')

denoised_gray = cv2.fastNlMeansDenoising(img, None, 25, 13, 35)

cv2.imwrite('/home/kanish/Desktop/output_folder/Old_Signature_Analyser/color.png', denoised_gray)
