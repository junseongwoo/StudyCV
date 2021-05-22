## Image Thresholding 하는 이유
# 1. 시각적 데이터를 단순화 시키기 위해
# 2. 이미지 세그멘테이션이 가능하게 해준다 (Image Segmentation)
#   - 외곽선, 디텍션이 잘 된다.
# 3. 이미지를 구성하는 픽셀에 2가지 수준을 할당한다라는 개념
#   - 할당은 특정한 threshold 값을 기준으로 한다.
#   - above & below 
# 4. 특정한 픽셀의 값이 threshold보다 높으면 white 을 할당 
#    픽셀의 값이 threshold보다 낮으면 black을 할당

import cv2

img = cv2.imread("hummingbird.jpg")
print(img.shape)
img = cv2.pyrDown(img)
print(img.shape)

# cv2.imshow("img", img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", img_gray)

#simple image thresholding                       
# 시작값 : 임계치 
# 100을 넘는 애들은 255로 보여주겠다. 
ret, simple_thresholding = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
#ret, simple_thresholding = cv2.threshold(img_gray, 100, 255,cv2.THRESH_TOZERO_INV)

# CV2.THRESH_BINARY : 픽셀의 값이 threshold 보다 크면 최대값을 할당 아니면 0을 할당
# CV2.THRESH_BINARY_INV : 픽셀의 값이 threshold 보다 크면 0으로 할당  ## 임계치를 정해넣고 반전 = 인버터 
# CV2.THRESH_TRUNC : 픽셀의 값이 threshold 보다 크면 값을 버림
# CV2.THRESH_TOZERO : 픽셀의 값이 threshold 보다 낮으면 0으로 할당
# CV2.THRESH_TOZERO_INV : 픽셀의 값이 threshold 보다 낮으면 1으로 할당

cv2.imshow("image_thresholding", simple_thresholding)

cv2.waitKey(0)
cv2.destroyAllWindows()