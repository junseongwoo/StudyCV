# Edge : 모서리 
# 1. 이미지에서 갑자기 끊겨지는 변화
# 2. 이미지에서 갑자기 물체가 과도하게 변경되는 부분
# 3. 서로 다른 Segmentation과 같은 구분

# Edge Detection을 왜 할까?
# 1. 모양의 정보를 얻고자 할때,
# 2. Feature extration (특성 추출)
# 3. 패턴 인식
# 4. 이미지 형태 변형

# Edge Detection을 하는 방법
# 1. Sobel
# 2. Prwitt
# 3. Laplaian
# 4. Canny

# Canny Edge Detection
# 1. 가장 효과적이고 복잡한 방법
# 2. 과정 
#   1) 필터를 통해서 smooth 노이즈를 제거하거나 매끈하게 만들어준다.
#   2) gradient 연산을 통해서 gradient를 계산
#   3) edge point 모서리 지점
#   4) edge point들을 연결 

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    # Canny Edge Detection - 10 to 100 
    img_edge1 = cv2.Canny(frame, 10, 100)

    # Canny Edge Detection - 50 to 150 
    img_edge2 = cv2.Canny(frame, 50, 150)

    # Canny Edge Detection - 100 to 200 
    img_edge3 = cv2.Canny(frame, 100, 200)

    cv2.imshow("video", frame)
    cv2.imshow("video1", img_edge1)
    cv2.imshow("video2", img_edge2)
    cv2.imshow("video3", img_edge3)


    if cv2.waitKey(5) & 0xFF == ord('q'):
        break