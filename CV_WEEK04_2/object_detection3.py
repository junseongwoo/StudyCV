import cv2
import time
import numpy as np

car_calssifier = cv2.CascadeClassifier("haarcascade_car.xml")

cap = cv2.VideoCapture("cars.avi")

while cap.isOpened():
    time.sleep(0.05)
    ret, frame = cap.read()
 
    # todo ret이 무엇인지 확인하기 
    if ret == True : 
         
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cars = car_calssifier.detectMultiScale(gray, 1.4, 2)

        for (x,y,w,h) in cars:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
            cv2.imshow("car", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else :
        break
cap.release()
cv2.destroyAllWindows()

