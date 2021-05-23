import cv2

# Transfer Learning : 전이 학습 ( 기존에 잘 만들어놓은 모델에 자신만의 데이터 셋을 적용하여 모델을 학습시키는 방법)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    smiles = smile_cascade.detectMultiScale(gray, 2, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),3)

        ## 눈을 찾기 위해 관심 있는 부분을 줄여두는 것 
        ## 얼굴만 범위로 둔다.
        roi_gray = gray[y:y:h, x:x+w]
        roi_color = img[y:y:h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes :
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255),3)
    
    cv2.imshow("img",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()