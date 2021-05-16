# bit 연산 : extraction
#  - masking에 큰 도움
#  - AND, OR ,XOR, NOT을 사용한다.

import cv2

img1 = cv2.imread("paper.jpg")
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.imread("hummingbird.jpg")
img2 = cv2.resize(img2, (400, 400))

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1, img2)



cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)




cv2.waitKey(0)
cv2.destroyAllWindows()