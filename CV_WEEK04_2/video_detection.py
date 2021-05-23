import numpy as np 
import cv2

cap = cv2.VideoCapture("slow_traffic_small.mp4")

while(1):
    ret, img = cap.read()

    roi = img[200:250, 300:400]
    cv2.imshow("roi video", roi)
    

    if ret == True :
        roi_hist = cv2
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        cv2.imshow("traffic video", img)

        ## 프레임 속도를 조절 하는것 
        key_value = cv2.waitKey(30) & 0xFF

        if key_value == 27:
            break

    else:
        break
