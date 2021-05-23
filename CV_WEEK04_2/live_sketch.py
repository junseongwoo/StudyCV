import cv2
import numpy as np

def sketup(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur로 이미지의 잡티 제거
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5),0)

    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()


    cv2.imshow("img", sketup(img))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()