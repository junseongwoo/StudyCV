import cv2
import numpy as np

img = cv2.imread("images/paper.jpg", 0)

## 외곽선을 따는 Canny 함수 
edges = cv2.Canny(img, 30, 70)      
edges1 = cv2.Canny(img, 50, 100)         

display_image = np.hstack((img, edges, edges1))  ## hstack 가로로 이미지를 연결해서 보여줌 
#display_image = np.vstack((img, edges, edges1))  ## vstack 세로로 이미지 연결 
cv2.imshow("Edge Image", display_image)

cv2.waitKey(0)
cv2.destroyAllWindows()