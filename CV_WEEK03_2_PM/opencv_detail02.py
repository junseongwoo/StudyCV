# image filtering 
# 이미지에 존재하는 픽셀을 해당하는 픽셀의 주위에 있는 픽셀에 특정한 함수를 적용한 결과를 기반으로 수정한다라는 개념
#
# 1. mask를 생성
# 2. mask 기준으로 주변 값들을 연산

# cv2.blur 함수
# cv2.blur (image, destination, 커널의 사이즈, [anchor type, bordertype ])

import cv2

img = cv2.imread("paper.jpg")

img_blur7 = cv2.blur(img, (7,7))
img_blur9 = cv2.blur(img, (9,9))

cv2.imshow("ori img", img)
cv2.imshow("blur img", img_blur9)

cv2.waitKey(0)
cv2.destroyAllWindows()