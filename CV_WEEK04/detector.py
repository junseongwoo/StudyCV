import matplotlib.pylab as plt
import cv2
import numpy as np

# 관심 있는 부분만 마스킹 하겠다
def region_of_interest(img, vertices):
    ## 마스크라는 이미지를 그려줌 
    mask = np.zeros_like(img)
    ##cv2.imshow("ori mask", mask)
    channel_count = img.shape[2]
    ## 흰색 부분을 만들어준다.
    match_mask_color = (255, ) * channel_count
    ## 관심 있는 이미지에 색을 채운다.
    cv2.fillPoly(mask, vertices, match_mask_color)
    ##cv2.imshow("mask 2", mask)
    ## 비트와이즈 연산으로 img 와 mask 해서 1인 부분을 만듦 
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


# 원근법을 적용하여 이미지를 처리하게 했다.

image = cv2.imread("road.jpg")
image = cv2.pyrDown(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

## 도로만 신경 써서 만들겠다 
region_of_interest_vertices = [
    (0, height),
    #(width / 2, height /2),
    (width / 2, 0),
    (width, height)
]


cropped_image = region_of_interest(image, np.array([region_of_interest_vertices], np.int32))
gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
canny_cropped_image = cv2.Canny(cropped_image, 100, 200)


#cv2.imshow("ori img", image)
cv2.imshow("crop img", cropped_image)
cv2.imshow("gray img", gray_image)
cv2.imshow("gray_canny img", canny_image)
cv2.imshow("cropped_canny img", canny_cropped_image)




cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(cropped_image)
# plt.show()