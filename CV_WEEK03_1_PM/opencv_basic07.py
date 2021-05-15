import cv2

img = cv2.imread("images/paper.jpg")
img2 = cv2.imread("images/color.jpg")

print(img.shape)
print(img.shape[0])
print(img.shape[0] * img.shape[1] * img.shape[2])
# 817920 = width * height * channel = img.shape[0] * img.shape[1] * img.shape[2] 
print(img.size)

print(img.dtype)

b, g, r = cv2.split(img)
b2, g2, r2 = cv2.split(img2)
print(b)

img = cv2.merge((b2,g2,b2))

cv2.imshow("imshow", img)
cv2.waitKey(0)
cv2.destroyAllWindows()