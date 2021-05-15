import cv2

img = cv2.imread("images\paper.jpg", -1)

# IMREAD_FLAGS
# cv2.IMREAD_COLOR : 1 컬러 이미지로 불러오기
# cv2.IMREAD_GRAYSCALE : 0 grayscale로 이미지 불러오기
# cv2.IMREAD_UNCHANGED : -1 alpha channel 유지하면서 이미지 불러오기

#print(img)

cv2.imshow("img", img)
key_value = cv2.waitKey(5000) & 0xFF

if key_value == 27:
    cv2.destroyAllWindows()
elif key_value == ord('s'):
    print(ord('s'))
    cv2.imwrite("output_paper.png",img)