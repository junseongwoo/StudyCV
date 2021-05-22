import matplotlib.pylab as plt
import cv2
import numpy as np

image = cv2.imread("road2.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width / 2, height / 2),
    width, height
]

print(region_of_interest_vertices)

def region_of_interest(img, verices):

plt.imshow(image)
plt.show()