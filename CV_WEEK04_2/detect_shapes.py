import numpy as np
import cv2

image = cv2.imread("someshapes.jpg")
image = cv2.pyrDown(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("ori img", image)

_, thresholdvalue = cv2.threshold(gray, 127, 255, 1)

contours, _ = cv2.findContours(thresholdvalue.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


## TODO approxPolyDP 함수 확인
##      moments 함수 확인 
for cnt in contours:
    #print(cnt.shape)
    ## 외곽선 수 구하기
    ##           외곽선을 단순화 하는 함수
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

    # 리스트의 길이가 3일때 = 삼각형일 때 
    if len(approx) == 3 :
        shape_name = "Triangle"
        cv2.drawContours(image, [cnt], 0, (0,255,0), -1)

        m = cv2.moments(cnt)
        print(m)
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])
        print(cx)
        print(cy)
        cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        # 모양에서 끝점을 알려주는 함수 
        m = cv2.moments(cnt)
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])

        if abs(w-h) <= 3: ## 높이와 너비의 차이가 3픽셀 차이보다 작다면 
            shape_name = "Square"  ## 정사각형이라 한다.

            cv2.drawContours(image, [cnt], 0, (0,125,255),-1)
            cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

        else : 
            shape_name = "Rectangle"  
            cv2.drawContours(image, [cnt], 0, (0,0,255),-1) ## 폐곡선 안을 채워주는 함수 
            cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

    elif len(approx) == 10 :
        shape_name = "Star"  
        cv2.drawContours(image, [cnt], 0, (255,0,255),-1) ## 폐곡선 안을 채워주는 함수 
        # 모양에서 끝점을 알려주는 함수 
        m = cv2.moments(cnt)
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])
        cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

    elif len(approx) >= 15 :
        shape_name = "Circle"  
        cv2.drawContours(image, [cnt], 0, (0,255,255),-1) ## 폐곡선 안을 채워주는 함수 
        # 모양에서 끝점을 알려주는 함수 
        m = cv2.moments(cnt)
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])
        cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
