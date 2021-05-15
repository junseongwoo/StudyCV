import cv2

image = cv2.imread("images/color.jpg")

print(image.shape)

cv2.imshow("image show", image)
cv2.waitKey(0) ## 기다리는 초(ms) == ex) 1000이면 1초 이후 꺼짐 