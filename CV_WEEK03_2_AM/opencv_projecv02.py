import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

def face_mask_detector(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60,60), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x,y,w,h) in faces: ## faces 안에 있는 걸 가져와서 마킹 해주는것 
          cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    return frame

input_image = cv2.imread("./mask.jpg")
output_image = face_mask_detector(input_image)
cv2.imshow("face_mask_test",output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
