import cv2

img = cv2.imread("./images/paper.jpg")
img2 = cv2.imread("./images/color.jpg")

print(img.shape)
print(img2.shape)

img = cv2.resize(img, (640, 420))
img2 = cv2.resize(img2, (640, 420))

print(img.shape)
print(img2.shape)

## 이미지를 겹침 ( 더함 )
added_img = cv2.add(img, img2)

## 이미지에 가중치를 줘서 겹침 ( 더함 )
added_img2 = cv2.addWeighted(img, .8, img2, .2, 1) 


#textoftheimage = img[109:331, 94:475]
# img[59:281, 44:425] = textoftheimage

cv2.imshow("img", added_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()