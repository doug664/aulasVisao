import cv2 as cv
from cv2 import COLOR_BGR2HSV
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./imagem/paisagem.jpg', cv.IMREAD_UNCHANGED)

img_hsv = cv.cvtColor(img, COLOR_BGR2HSV)

shape_f = np.shape(img_hsv)
img_bin = np.zeros(shape_f [0:2])
for j in range(0, shape_f[1]):
    for i in range(0, shape_f[0]):
        if(img_hsv[i,j,0]>102 
        and img_hsv[i,j,0]<138 and img_hsv[i,j,1]>50 and img_hsv[i,j,2]>50):
            img_bin[i,j] = 1
        else:
            img_bin[i,j] = 0

ig = plt.figure()

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_rgb, cmap='gray', vmin=0)

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.tight_layout()
plt.show(block=False)

fig_bin = plt.figure()
plt.imshow(img_bin, cmap='gray', vmin=0)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.tight_layout()
plt.show()


