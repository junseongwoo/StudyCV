import cv2
import pickle

haar = cv2.CascadeClassifier("./model/haarcascade_frontalface_default.xml")
## pickle 파일 형태 : 파이썬에서 파일을 불러올 때 효율적으로 가져오기 위한것 
mean = pickle.load(open("./model/mean_preprocess.pickle", "rb")) # rb : 바이너리로 읽어 오는것 
model_svm = pickle.load(open("./model/model.svm.pickle", "rb"))
model_pca = pickle.load(open("./model/pca_50.pickle", "rb"))

gender_pre = ["Male", "Female"]
font = cv2.FONT_HERSHEY_SIMPLEX 

print("모델이 적상적으로 불러와졌습니다.")


def pipeline_model(path, filename, color = "bgr"):
    # step_1 : 이미지 불러오기 
    img = cv2.imread(path)

    # step_2 : 이미지를 gray scale로 변환 
    if color == "bgr":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else: # bgr이 아니라도 gray로 만듬 -> 확실하게 하기 위해 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # step_3 : 얼굴 부분을 검출 (haar cascade classifier를 이용)
    faces = haar.detectMultiScale(gray, 1.5, 3)
    for x,y,w,h in faces: 
        # print(x,y,w,h)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
        roi = gray[y:y+h, x:x+W]

    # step_4 : (0~1 의 값으로 만듬) normalization
    # roi = roi/255.0

    cv2.imwrite("./static/detection.html")


        
