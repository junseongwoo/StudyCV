# Blur : 이미지를 단순화 하면서도 노이즈 제거 역할
# noise : 이미지에 존재하는 원래의 예상하는 픽셀 값이 아닌 밝거나 색의 변종
# 이미지의 노이즈! 생길수밖에 없다! -> 이유
# 1. 이미지라는 것은 전기적으로 전송  디카로 사진 찍고, 네트워크를 통해서 전송..
# 2. 센서의 문제가 생기거나 조정이 일어날때 
# 3. 빛의 강도 ISO Factor

import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

kernel = np.ones((3,3), np.uint8)
print(kernel)

# erosion technique ## 뭉개고 어두워짐 
img_err = cv2.erode(img, kernel, iterations = 5 )

# dilation technique ## 뭉개고 밝아짐
img_dil = cv2.dilate(img, kernel, iterations = 5)

# morphological opening technique
img_opn = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#  morphological colosing technique
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# cv2.MORPH_GRADIENT
img_grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# cv2.MORPH_TOPHAT
img_tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# cv2.MORPH_BLACKHAT
img_blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


cv2.imshow("ori img", img)
#cv2.imshow("err img", img_err)
#cv2.imshow("dil img", img_dil)
cv2.imshow("morp OPEN", img_opn)
cv2.imshow("morp COLOSE", img_close)
cv2.imshow("morp GRAD", img_grad)
cv2.imshow("morp TOPHAT", img_tophat)
cv2.imshow("morp BLACKHAT", img_blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()