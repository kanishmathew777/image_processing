import cv2
import numpy as np

# read image through command line
img = cv2.imread("/home/kanish/Documents/ICR_advanced_forms/Advanced handwritting samples/scan/iyvin.jpg")

height, width = img.shape[:2]

# convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret, thresh = cv2.threshold(gray_image, 127, 255, 0)

# find contours in the binary image
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

blank_image = np.ones((height, width, 3), np.uint8)
for c in contours:
    # calculate moments for each contour
    M = cv2.moments(c)

    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.circle(blank_image, (cX, cY), 5, (30, 150, 70), -1)
        # cv2.putText(img, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 200), 3)

# display the image
cv2.imwrite("Image.png", blank_image)
