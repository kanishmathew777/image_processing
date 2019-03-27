import cv2
import numpy as np

# # Read image
# im = cv2.imread("/home/kanish/Documents/ICR advanced forms/cropped.png", cv2.IMREAD_GRAYSCALE)
#
# # Set up the detector with default parameters.
# detector = cv2.SimpleBlobDetector()
#
# # Detect blobs.
# orb = cv2.ORB_create()
# keypoints, des1 = orb.detectAndCompute(im, None)
#
# # keypoints = detector.detect(im)
#
# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
#                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# kpimg = cv2.drawKeypoints(im, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# # Show keypoints
# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)

# img = cv2.imread("/home/kanish/Documents/ICR advanced forms/cropped.png", 0)
#
# # Initiate FAST object with default values
# fast = cv2.FastFeatureDetector_create()
# 
# # find and draw the keypoints
# kp = fast.detect(img, None)
# img2 = cv2.drawKeypoints(img, kp, np.array([]), color=(255,0,0),
#                          flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
#
# cv2.imwrite('fast_true.png', img2)


img = cv2.imread("/home/kanish/Documents/ICR advanced forms/cropped.png", 0)

orb = cv2.ORB_create(nfeatures=10, scoreType=cv2.ORB_HARRIS_SCORE)
kp = orb.detect(img, None)

kp, des = orb.compute(img, kp)
#
# for key_point in kp:
#     print(key_point.pt)
# print(kp)
img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0),
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# img2 = cv2.drawKeypoints(img, kp, np.array([]), color=(0, 255, 0), flags=0)

cv2.imwrite('fast.png', img2)
