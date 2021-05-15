import cv2
import numpy as np

img = cv2.imread("images/gray.jpg", 0)

## 어떤 임계값을 정한 뒤 픽셀 값이 임계값을 넘으면 255, 임계값을 넘지 않으면 0으로 지정하는 방식
ret, thresh = cv2.threshold(img, 50, 80, cv2.THRESH_BINARY)   

cv2.imshow("Gray", img)
cv2.imshow("Threashold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()