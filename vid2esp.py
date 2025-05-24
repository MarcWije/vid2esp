import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import os

os.chdir("H:/vid2esp")

img = cv.imread('rocket-raccoon.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
height, width = img.shape
print(int(height/2), int(width/2))
img = cv.resize(img, (int(width/2), int(height/2)))
edge_full = cv.Canny(img,100,200)


x_start = int(width/2) - 64
x_end = int(width/2) + 63
y_start = int(height/2) - 32
y_end = int(height/2) + 31

edge = edge_full[y_start:y_end, x_start:x_end]

edges = cv.resize(edge, (128,64))

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cv.imwrite("conv.jpg", edges)



plt.show()