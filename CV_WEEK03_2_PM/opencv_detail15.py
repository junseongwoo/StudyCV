# image segmentation 기법 
# image classification -> image object detection -> image segmentation 

## 4주차에 설명 

import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR -> RGB 

img_res = img_rgb.reshape((-1, 3))
vec = np.float32(img_res)
crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1000, 0.2)

k = 3 
attemps = 10

ret, labels, center = cv2.kmeans(vec, k, None, crit, attemps, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)

img_seg = center[labels.flatten()]
img_seg = img_seg.reshape((img.shape))

cv2.imshow('ori', img)
cv2.imshow('seg_img', img_seg)

cv2.waitKey(0)
cv2.destroyAllWindows()