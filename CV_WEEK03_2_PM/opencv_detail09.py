import cv2 
import numpy as np

img = cv2.imread("hummingbird.jpg")

img = cv2.pyrDown(img)
height, width, _ = img.shape

## 점 세개 가지고 돌리는것 
mat1 = np.float32([ [50, 50], [200, 50], [50, 200] ])   # 이미지의 현재 3개의 점 
mat2 = np.float32([ [10, 100], [200, 50], [100, 250] ])   # 이미지의 지정한 3개의 점으로 이동하려 한다.

aff_matrix = cv2.getAffineTransform(mat1, mat2)

aff_img = cv2.warpAffine(img, aff_matrix, (width, height))

cv2.imshow("ori_img", img)
cv2.imshow("aff_img", aff_img)

cv2.waitKey(0)
cv2.destroyAllWindows()