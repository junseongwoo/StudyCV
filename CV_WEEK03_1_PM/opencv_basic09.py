import cv2
import numpy as np

img = np.zeros((352,352,3), np.uint8)
img = cv2.rectangle(img, (200,0), (300,100), (255,255,255), -1)
img2 = cv2.imread("./images/gray.jpg")

## 1 & 1 = 1 
#bitAnd = cv2.bitwise_and(img, img2)  

bitOr = cv2.bitwise_or(img, img2)

bitXOR = cv2.bitwise_xor(img, img2)
cv2.imshow("img1", img)
cv2.imshow("img2", img2)
#cv2.imshow("bitAnd", bitAnd)
#cv2.imshow("bitOr", bitOr)
cv2.imshow("bitXOr", bitXOR)



cv2.waitKey(0)
cv2.destroyAllWindows()
