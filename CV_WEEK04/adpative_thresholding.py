# Threshold의 종류
# 1. Simple Thresholding
# 2. Adaptive Thresholding

# Adaptive (조정의, 적응의) Thresholding
# 이미지의 특정 부분의 색을 보정
# 다른 부분에 다른 방법을 적용 - 알고리즘이 threshold를 계산 -> 각기 다른 임계치를 적용


import cv2

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# median filter 
img_med = cv2.medianBlur(img_gray, 3) # 홀수 단위로 들어감 
apt_thresh1 = cv2.adaptiveThreshold(img_med, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
apt_thresh2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY, 11, 2)


# cv2.ADAPTIVE_THRESH_MEAN_C 
# 픽셀들의 mean 값을 계산해서 threshold을 계산 
# mean 값을 곱하고 c를 빼는 식 

# cv2.ADAPTIVE_THRESH_GAUSSIAN_C 
# 주변 값을 합으로 부터 가중치를 계산하고 c를 빼서 threshold를 계산

cv2.imshow("ori img", img_gray)
cv2.imshow("med img", img_med)
cv2.imshow("adaptive img", apt_thresh1)
cv2.imshow("adaptive img", apt_thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()