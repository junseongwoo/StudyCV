import cv2
import numpy as np

image = cv2.imread("blobs.jpg")

# 기본 설정으로 물방울 초기화
detector = cv2.SimpleBlobDetector_create()

# 이제 찾아라! 
find_blobs = detector.detect(image)

black = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, find_blobs, black, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(find_blobs)
text = "Total Number of Blobs" + str(number_of_blobs)
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1 ,( 100, 0 , 255) , 2)

cv2.imshow("detect blobs", blobs)

## 세부 설정을 가진 detector 생성
params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True
params.minCircularity = 0.7

params.filterByConvexity = False # 오목, 볼록 찾는 것 
params.minConvexity = 0.2

params.filterByInertia =True
params.minInertiaRatio = 0.01

## 세부 설정을 추가한 물방울 detector
detector = cv2.SimpleBlobDetector_create(params)
find_blobs = detector.detect(image)
black = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, find_blobs, black, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("params blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 허프 변환으로는 타원형을 잡기가 힘들다
# output = img.copy()

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray, 7)

# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2= 30, minRadius=0, maxRadius=50)
# detected_circles = np.uint16(np.around(circles))

# print(circles.shape)
# print(detected_circles.shape)

# for (x,y,r) in detected_circles[0, :]:
#     cv2.circle(output, (x,y), r, (0,255,255),3)
#     cv2.circle(output, (x,y), 2, (0,255,255,),3)

# cv2.imshow("output", output)
# cv2.imshow("median blur", gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()