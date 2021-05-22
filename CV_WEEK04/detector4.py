import cv2
import numpy as np

## 스도쿠의 격자 찾기 

img = cv2.imread("sudoku.jpg")
cv2.imshow("img", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
print(gray) # 0 ~ 255
gray = np.float32(gray)
print(gray) # 0.0 ~ 255.0
##               이미지, 블록사이즈, 커널사이즈, 표시할 크기
dst = cv2.cornerHarris(gray, 2, 3, 0.1)
dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow("corner detect", img)

cv2.waitKey(0)
cv2.destroyAllWindows()