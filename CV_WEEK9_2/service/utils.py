import cv2
import pickle

haar = cv2.CascadeClassifier("./model/haarcascade_frontalface_default.xml")
mean = pickle.load(open("./model/mean_preprocess.pickle", "rb"))
# model_svm = pickle.load(open("./model/model_svm.pickle", "rb"))
# model_pca = pickle.load(open("./model/pca_50.pickle", "rb"))

gender_pre = ["Male", "Female"]
font = cv2.FONT_HERSHEY_SIMPLEX

print("모델이 정상적으로 불러와졌습니다.")

def pipeline_model(path, filename, color="bgr"):
    # step 1 : 이미지 불러오기
    img = cv2.imread(path)

    # step 2 : 이미지를 gray scale로 변환
    if color == "bgr":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # step 3 : 얼굴 부분을 추려냅니다. (haar cascade classifier를 이용)
    faces = haar.detectMultiScale(gray, 1.5, 3)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi = gray[y:y+h, x:x+w]

        # step 4 : (0 ~ 1의 값으로) normalization 
        # roi = roi /255.0
    
    cv2.imwrite("./static/detection/{}".format(filename), img)

