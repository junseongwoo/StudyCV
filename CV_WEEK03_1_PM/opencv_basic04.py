import cv2
import numpy as np

## cv2의 EVENT 모듈을 다 찾아보는 것
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(type(events))
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x,y), font, 1, (255,255,0), 2)
        cv2.imshow("img", img)

    ## 좌표의 컬러를 찍음 
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + ", " +str(red)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (0,0,0), 2)
        cv2.imshow("img", img)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("images/paper.jpg")
cv2.imshow('img',img)

cv2.setMouseCallback("img", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()