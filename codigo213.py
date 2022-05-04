import cv2 as cv 
import math
import os

img = cv.imread('./imagem/Inuyasha-007.webp', cv.IMREAD_UNCHANGED)

img_rgb = cv.imread('./imagem/Inusyasha-007.jpg', cv.IMREAD_UNCHANGED)

yc = math.floor(img.shape[0]/2)
xc = math.floor(img.shape[1]/2)

interval = 350

img_sel = img[int(yc-interval/2):int(yc+interval/2), int(xc-interval/2): int(xc+interval/2) ]

cv.imshow('Inuyasha', img)
cv.imshow('Inusyasha2', img_sel)

cv.imwrite('./imagem/doug.png', img)
cv.imwrite('./imagem/doug_selected.png', img_sel)

img_sel_rgb = img_rgb[0:10,0:10,[0,2]]
print(img_sel_rgb.shape)
cv.waitKey(0)
cv.destroyAllWindows()
