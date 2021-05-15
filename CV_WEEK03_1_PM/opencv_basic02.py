## 비디오 캡쳐 사용하기 
import cv2

## 숫자는 카메라 번호! 
cap = cv2.VideoCapture(0)

## 카메라의 해상도를 확인 할 수 있다.
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

## isOpened : 열려진 상태라면 무한 루프 돌아라 
while (cap.isOpened()):
    ret, frame = cap.read() # 프레임 당 리턴 값을 계속 돌려줘 

    if ret == True : # 프레임이 정상 값이라면 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)  ## gray = 그레이 스케일, frame = 원래 비디오 스케일 

        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()
