import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def faceDetector(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)
    return img

input_image = cv2.imread("./face_test3.jpg")
output_image = faceDetector(input_image)
cv2.imshow("face_test",output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()