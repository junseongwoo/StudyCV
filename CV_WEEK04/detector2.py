import matplotlib.pylab as plt
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255 #(255, ) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

image = cv2.imread("road.jpg")
image = cv2.pyrDown(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    # (width / 2, height /2),
    (width / 2, 0),
    (width, height)
]

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
lines = cv2.HoughLinesP(cropped_image, rho = 6, theta = np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (255, 255, 0), 3)
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)

    return img

image_with_lines = draw_the_lines(image, lines)

# canny_image_crop = cv2.Canny(cropped_image, 100, 200)

# plt.imshow(cropped_image)
# plt.show()

cv2.imshow("gray image", gray_image)
cv2.imshow("canny image", canny_image)
cv2.imshow("cropped image", cropped_image)
cv2.imshow("lined image", image_with_lines)

cv2.waitKey(0)
cv2.destroyAllWindows()