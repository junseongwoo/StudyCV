import numpy  as np
import cv2
import math

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    l = []
    lf = []
    i = 1

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

        s = str(i)
        cv2.putText(img, s, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        i += 1
        l.append(x)
        l.append(y)
        lf.append(l)

    close_person=""
    for i in range(len(lf)):
        for j in range(i+1,len(lf)):
            d=math.sqrt( ((lf[j][1]-lf[i][1])**2)+((lf[j][0]-lf[i][0])**2) )
            print("P",i+1,"- P",j+1,"=",d)

            if d<150:
                close_person+="Person "+str(i+1)+" and Person "+str(j+1)+" ; "
                cv2.line(img, (lf[i][0],lf[i][1]), (lf[j][0],lf[j][1]),(0, 0, 255),2)

                close_person+=" are not following social distancing "
                cv2.putText(img, close_person, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()