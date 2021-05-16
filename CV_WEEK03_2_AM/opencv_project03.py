import cv2
import numpy as np
from numpy.matrixlib import defmatrix
import pytesseract
def rectify(h):
    h = h.reshape((4, 2))
    hnew = np.zeros((4, 2), dtype=np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h, axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew

def resize_image(image, width, height):
    image= cv2.resize(image, (width, height))
    return image

def gray_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image

def canny_edge_detection(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(blurred_image, 0, 50)
    return edges

def find_contours(image):
    (contours, _) = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for c in contours:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)

        if len(approx) == 4:
            target = approx
            break
    
    return target

def draw_contours(orig_image, image, target):
    approx = rectify(target)
    pts2 = np.float32([[0,0], [800, 0], [800, 800], [0, 800]])

    M = cv2.getPerspectiveTransform(approx, pts2)
    result = cv2.warpPerspective(image, M, (800, 800))

    cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    return result

image = cv2.imread("aaa.png")         # OCR 할 이미지를 불러왔고
image = resize_image(image, 1500, 800)  # 그 이미지를 잘 OCR할 수 있도록 크기를 크게 하고
orig = image.copy()                     
gray = gray_image(orig)                 # 처리량을 줄일 수 있도록 컬러이미지를 Gray로 변환
edges = canny_edge_detection(gray)      # 그 이미지에서 외곽선을 확인

target = find_contours(edges)
output = draw_contours(orig, image, target)
text = pytesseract.image_to_string(output)
print("찾아진 문자들은 : " + text)

cv2.imshow("edges", edges)
cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()