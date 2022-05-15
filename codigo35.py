import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('imagem/videogame.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_bin = img_gray < 100
fig = plt.figure()
plt.imshow(img, cmap='gray', vmin=0)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.show(block=False)

fig_gray = plt.figure()
plt.imshow(img_gray, cmap='gray', vmin=0)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.show(block=False)

fig_bin = plt.figure()
plt.imshow(img_gray, cmap='gray', vmin=0)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.show()










