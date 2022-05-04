import cv2 as cv
from matplotlib import pyplot as plt

img_rgb = cv.imread('./imagem/inuyasha-008.jpg', cv.IMREAD_UNCHANGED)
img_hsv = cv.cvtColor(img_rgb, cv.COLOR_BGR2HSV)
img_rgb = cv.cvtColor(img_rgb, cv.COLOR_BGR2RGB)

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img_rgb)
ax2 = fig.add_subplot(1,2,2)
ax2.imshow(img_hsv)

plt.show()