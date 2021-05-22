import cv2
import numpy as np


img = cv2.imread("sudoku.jpg")
cv2.imshow("img", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# 가장 중요한 코너를 찾아주는 함수 
# shi Tomasi Corner Detector
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow("corner detect", img)

cv2.waitKey(0)
cv2.destroyAllWindows()