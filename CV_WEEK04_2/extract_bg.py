import cv2
import numpy as np

img = cv2.imread("bg.jpg")
img = cv2.pyrDown(img)

cv2.imshow("pedestrain", img)

bg_mask = cv2.createBackgroundSubtractorMOG2()

appled_mask = bg_mask.apply(img)

cv2.imshow("appled mask", appled_mask)

cv2.waitKey(0)
cv.destroyAllWindows()