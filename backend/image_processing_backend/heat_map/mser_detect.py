import cv2

img = cv2.imread("/home/kanish/Documents/ICR_advanced_forms/Advanced handwritting samples/scan/soumya_1.jpg")
mser = cv2.MSER_create(_min_area=60, _max_variation=5.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()

regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))

cv2.imwrite("mser_region.png", vis)
