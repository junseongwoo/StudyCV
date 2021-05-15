import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(points)
        cv2.circle(img, (x,y), 3, (0,0,255), -1) ## 점을 찍고
        points.append((x,y))                     ## 그 좌표를 추가한다. 

        if len(points) >= 2:                     ## 포인트가 두개 이상이면 
                       ## 시작점    ,  끝점
            cv2.line(img, points[-1], points[-2], (255, 255,0), 5)

        cv2.imshow("img", img)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("images/paper.jpg")
cv2.imshow('img',img)
points = []
cv2.setMouseCallback("img", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()