# negative transformation
# 이미지를 반대로 찾는 변환
# 밝은 것을 어두운 것 / 어두운 것을 밝은 것
# color 채널과 관련이 많이 있다.

import cv2 

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)

img_neg = 1-img
img_not = cv2.bitwise_not(img)

cv2.imshow('ori', img)
cv2.imshow('neg', img_neg)
cv2.imshow('not', img_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
