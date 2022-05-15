import cv2  as cv 
import numpy as np
from matplotlib import pyplot as plt

im = cv.imread('./imagem/Inuyasha-007.webp', cv.IMREAD_UNCHANGED)
mask = np.ones((3,3), np.float32)/9
im_br =- cv.filter2D(im.astype(np.float32), -1, mask)

c=2.5
im_tr = im - im_br
im_nit = im + c * im_tr

fig_tr = plt.figure()
plt.imshow(im, cmap='gray', vmin=0)
ax1 = plt.gca()
ax1.axes.xaxis.set_visible(False)
ax1.axes.yaxis.set_visible(False)
plt.show(block=False)

fig_tr = plt.figure()
plt.imshow(im_tr, cmap='gray', vmin=0)
ax1 = plt.gca()
ax1.axes.xaxis.set_visible(False)
ax1.axes.yaxis.set_visible(False)
plt.show(block=False)

fig_nit = plt.figure()
plt.imshow(im_nit, cmap='gray')
ax2 = plt.gca()
ax2.axes.xaxis.set_visible(False)
ax2.axes.yaxis.set_visible(False)
plt.show(block=False)

