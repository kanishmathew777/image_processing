import cv2

img = cv2.imread('/home/kanish/Desktop/image_processing_proj/backend/image_processing_backend/additional_trials/text_only.png')

ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                  127, 255, cv2.THRESH_BINARY)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 10))
threshed = cv2.morphologyEx(threshed_img, cv2.MORPH_CLOSE, rect_kernel)
cv2.imwrite('threshed.png', threshed)
