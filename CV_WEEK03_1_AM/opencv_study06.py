import cv2
import numpy as np

image = cv2.imread("images/shape.png")

ori_img = image.copy() ## 복사 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## 이미지의 임계치 사이의 값만 사용 // 30~200 사이에 있는 값만 사용 
## 외곽선을 찾은다음 
edges = cv2.Canny(gray, 30, 200)

## 윤곽선 구함 // 등고선을 찾아내어
contours, hieararchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

## 윤곽에 색을 그림 
cv2.drawContours(image, contours, -1, (0,255,0), 3)

display_image = np.hstack((ori_img, image))

cv2.imshow("image", display_image)
cv2.waitKey(0)