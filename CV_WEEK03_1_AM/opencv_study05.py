# erosion and dilation 
# 이미지를 뭉개는것 
import cv2
import numpy as np

img = cv2.imread("images/paper.jpg", 0)
kernel = np.ones((5,5), np.uint8) 
ret, thresh = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
erosion = cv2.erode(thresh, kernel)
dilation = cv2.dilate(thresh, kernel)

img2 = cv2.resize(img, (300, 300))
display_image = np.hstack((thresh, erosion, dilation))

cv2.imshow("erosion and dilation", display_image)

edges = cv2.Canny(img, 30, 70)
erosion = cv2.erode(edges, kernel)
dilation = cv2.dilate(edges, erosion, dilation)
#display_image = np.hstack((edges, erosion, dilation))

cv2.imshow("Canny Erosion & Dilation Image", display_image)

cv2.waitKey(0)