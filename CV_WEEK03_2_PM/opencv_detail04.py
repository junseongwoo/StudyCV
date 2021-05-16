# 이미지 처리 - Arithmetic 연산
# Image Addition, Image Blending, Image Substraction, Bit Operation 

# Image Blending : 
# - 이미지들의 합
# - 이미지를 겹쳐보이게 하거나, 투명하게 보이게 하는 방법
# y = image1 * (1-특정가중치) + image2 * 특정가중치    : 특정 가중치 : 0~1의 값을 가짐

# substract 
# add or addWeighted 처럼 값을 더하는 것이 아니라 빼는 개념 
# 이미지 간의 크기가 같아야 한다. 



import cv2
## here arrays have the same size and the same number of channels
## 이미지 두개의 크기가 다르면 에러 생김 

img1 = cv2.imread("paper.jpg")
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.imread("hummingbird.jpg")
img2 = cv2.resize(img2, (400, 400))

img_blend = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
img_sub = cv2.subtract(img1, img2)



cv2.imshow("img_blend", img_blend)
cv2.imshow("img_sub", img_sub)



cv2.waitKey(0)
cv2.destroyAllWindows()