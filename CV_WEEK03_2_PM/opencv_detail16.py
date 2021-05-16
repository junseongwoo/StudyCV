# ROI 
# in computer vision : Region of Interest 
# in economics : Return of Investment 

import cv2 

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)

roi = cv2.selectROI(img)

## 파이썬에서 크롭하려면 시작과 끝점을 줘야하는데
## roi에서 점을 4개 주었다 
## print(roi)
## y : y + y축 이동거리 , x : x + x축 이동거리를 나타내는 것이다.
crop = img[int(roi[1]):int(roi[1]+ roi[3]), int(roi[0]):int(roi[0] + roi[2])]


cv2.imshow("image", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()