import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8) ## 512x512 크기의 검은색 도화지 

## OPENCV는 BGR 순서로 된다.
cv2.circle(img, (100,100), 50, (0,255,0), 10)
cv2.rectangle(img, (200,200),(400,500), (255,0,0), 1)
cv2.line(img, (160,160), (352, 29), (0,0,255), 5)
cv2.putText(img, "Korea", (280,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255),1)

cv2.imshow("My figure", img)
cv2.waitKey(0)
cv2.destroyAllWindows()