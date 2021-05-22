import cv2
import numpy as np

img = cv2.imread("sudoku.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apertureSize : 커널 크기 , 기본 크기는 3 
edges = cv2.Canny(img_gray, 50, 150) #, apertureSize=3)

# 선들의 시작점과 끝점을 알려주는 것 
# Hough 변환 : 자율주행 관련된 쪽에서 자주 볼 수 있다. - 선과 관련된 곳 
#      이미지, 선을 구분하기 위한 거리, 세타(각도), threshold
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# 허프변환으로 선을 찾아내면 극좌표로 찾아냄 - 어떤 각도로 부터 얼마나 떨어져있는지 찾아냄
# 그래서 다시 x, y 좌표로 만들어줘야함

## Todo - 공식 다시 이해 하기
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow("Image by Hough", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print(lines.shape)