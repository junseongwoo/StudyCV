# Image Gradients
# 이미지의 선명도 (sharpness)를 측정
# 이미지가 sharpness가 점점 클수록 더 높은 gradients 가진다라는 표현을 사용

from typing import SupportsComplex
import cv2
import numpy as np

img = cv2.imread("pic2.jpg")
print(img.shape)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sobel gradients 
# Gaussian smoothing 방식
# direction까지 고려된 filtering 방법

img_sob = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
img_sob_gray = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize = 5)
cv2.imshow("sobel image", img_sob)
cv2.imshow("sobel gray image", img_sob_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()