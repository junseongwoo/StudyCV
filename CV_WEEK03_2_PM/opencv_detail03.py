# 피라미드 기법 (pryamid)
# Level 0 : Original Size
# Level 1 : up의 경우 x2 / down의 경우 1/2 

# pryUp 
# - 원래 이미지의 크기를 2배 늘린다.
# - 이미지를 샘플링 크게 하고 blur 처리

# pryDown 
# - 원래 이미지의 크기를 1/2로 줄인다.
# - 이미지를 샘플링을 작게하고 blur 처리 

## pry 장점 
# 1. 낮은 해상도
# 2. 다양한 크기의 이미지를 얻을 수 있다 -> 루프를 돌려서 쉽게 얻음 
# 3. 쉽게 이미지 처리를 얻을 수 있다.
# 4. edge를 쉽게 찾을 수 있다. 

import cv2

img = cv2.imread("paper.jpg")

#img = cv2.resize(img, (300,300))
print(img.shape)
# img = cv2.pyrUp(img)
# print(img.shape)
# img = cv2.pyrUp(img)
# print(img.shape)
# cv2.imshow("pryUp1", img)
# cv2.imshow("pryUp2", img)

img = cv2.pyrDown(img)
print(img.shape)
img = cv2.pyrDown(img)
print(img.shape)
cv2.imshow("pryDown1", img)
cv2.imshow("pryDown2", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
