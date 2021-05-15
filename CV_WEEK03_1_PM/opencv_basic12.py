import cv2
import datetime

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_out = cv2.VideoWriter("mycam.avi", fourcc, 30.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "Width: " + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
    datetext = str(datetime.datetime.now())
    frame = cv2.putText(frame, datetext, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("video_out", frame)
    video_out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
video_out.release()
cv2.destroyAllWindows()