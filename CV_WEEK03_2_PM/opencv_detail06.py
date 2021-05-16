# translation 
# 이미지의 객체나 이미지 위치를 옮기는데 사용
# 옮기는 방향은 (x, y) 방향이다! -> 옮겨진 장소 (tx, ty)
# 
# transformation matrix M = [[ 1 0 tx] [0 1 ty]] // 2행 3열짜리 행렬 

import cv2
import numpy as np 

img = cv2.imread("hummingbird.jpg")

img = cv2.pyrDown(img)
## img,shape 값이 튜플로 3개가 나오기 때문에 , _ 까지 넣어줘야함 
## _ 은 위치 값은 넣어주면서 값은 받아오지 않음
height, width, _ = img.shape  
print(img.shape)

## transformation matrix 만들어줌 -> 옮길 방향 설정
## float32 비트 형의 행렬 
flt_var = np.float32([[1,0,-100], [0, 1, -150]])
#print(flt_var)

img_trans = cv2.warpAffine(img, flt_var, (width, height))

cv2.imshow("ori_img", img)
cv2.imshow("trans_img", img_trans)

cv2.waitKey(0)
cv2.destroyAllWindows()

