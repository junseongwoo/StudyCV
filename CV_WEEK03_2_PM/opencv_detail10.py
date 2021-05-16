import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
height, width, _ = img.shape

## 점 4개로 이미지 움직이기
mat1 = np.float32([ [110, 600], [200, 500], [300, 230], [500, 400] ])
mat2 = np.float32([ [0, 200], [200, 250], [0, 0] , [650, 500] ])

## 최소한 점 4개 이상 있어야 prespective matrix 만들어짐
prespective_matrix = cv2.getPerspectiveTransform(mat1, mat2)
print(prespective_matrix)

prespective_img = cv2.warpPerspective(img, prespective_matrix, (width, height))

cv2.imshow('ori', img)
cv2.imshow('affin', prespective_img)

cv2.waitKey(0)
cv2.destroyAllWindows()