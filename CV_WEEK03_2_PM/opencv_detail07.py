# image rotation = rotation transformation  
# 이미지의 축을 변경
# 변경할 각도를 지정해줘야한다
# transformation matrix M = [[cos - sin] [sin cos]] 2x2 행렬 
# opencv는 scale rotation 

import cv2 

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)

height, width, _ = img.shape  

## 높이에서 1/2, 넓이 에서 1/2 == 중심을 기준으로 회전 하겠다
##               cv2.getRotationMatrix2D(center, angle, scale)
rotaion_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)

rot_img = cv2.warpAffine(img, rotaion_matrix, (width, height))

cv2.imshow("ori_img", img)
cv2.imshow("rot_img", rot_img)

cv2.waitKey(0)
cv2.destroyAllWindows()