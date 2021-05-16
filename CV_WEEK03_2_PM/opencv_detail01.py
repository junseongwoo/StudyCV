# resize 함수 
# 1: 처리할 대상 
# 2: 조정할 이미지의 크기
# 3, 4 : 각각 y축, x축으로 조정할 scale (크기)를 설정
# 5: 보간 (interpolation) -> 이미지의 크기를 조정함에 따라 각 픽셀의 정보 보간법 (줄여들거나, 커졌을때 픽셀간의 
#                            값을 어떻게 채울 것인지? )
# #  - cv2.INTER_AREA : 지역 보간 
# #  - cv2.INTER_CUBIC : cubic 보간 
# #  - cv2.INTER_LINEAR : 선형 보간 (기본 설정)

import cv2

img = cv2.imread("paper.jpg")
print(img.shape)
img_res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

print(img_res.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", img_res)
cv2.waitKey(0)
cv2.destroyAllWindows()
