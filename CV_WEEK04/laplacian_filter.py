import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

img_laplacian = cv2.Laplacian(img, cv2.CV_16U)
cv2.imshow("laplacian img", img_laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()