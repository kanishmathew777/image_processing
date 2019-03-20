import cv2
import numpy as np
import matplotlib.pyplot as plt


src = cv2.imread("/home/kanish/Documents/ICR advanced forms/Advanced handwritting samples/fwdsamplefiles/straighten.jpg")

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

gray = cv2.bitwise_not(gray)
bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

vertical = np.copy(bw)

# Specify size on vertical axis
rows = vertical.shape[0]
verticalsize = int(rows / 40)
# Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
# Apply morphology operations
vertical = cv2.erode(vertical, verticalStructure)
vertical = cv2.dilate(vertical, verticalStructure)
# Show extracted vertical lines
cv2.imwrite('new1.png', vertical)


def plot_graph(x, width_props):
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.hlines(*width_props[1:], color="C3")
    plt.show()