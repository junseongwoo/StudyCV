import cv2
import numpy as np

def nothing():
    pass

# cv2.namedWindow("Tracking")

while True:
    frame = cv2.imread("./images/color.jpg")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array([50, 50, 50])
    u_b = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()