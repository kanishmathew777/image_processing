import cv2
import numpy as np

img = cv2.imread('/home/kanish/Documents/OCR/Signature_dtctn/signatue-1.png')

org_image = img

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply GuassianBlur to reduce noise. medianBlur is also added for smoothening, reducing noise.
gray = cv2.GaussianBlur(gray, (5, 5), 0)
gray = cv2.medianBlur(gray, 5)

# Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3.5)

kernel = np.ones((2, 2), np.uint8)
gray = cv2.erode(gray, kernel, iterations=1)

# gray = erosion
gray = cv2.dilate(gray, kernel, iterations=1)

cv2.imwrite("cimg.png", gray)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10,
                           param1=30, param2=14, minRadius=0, maxRadius=14)

idx = 1

if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        print(idx)
        # draw the circle in the output image, then draw a rectangle in the image
        # corresponding to the center of the circle
        cv2.circle(org_image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(org_image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        # time.sleep(0.5)
        print("Column Number: ", x)
        print("Row Number: ", y)
        print("Radius is: ", r)

        idx += 1
    cv2.imwrite('detected circles.png', org_image)
