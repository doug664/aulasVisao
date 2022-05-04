import numpy as doug

import cv2 as cv

img = cv.imread('./imagem/Inuyasha-007.webp', cv.IMREAD_UNCHANGED)

output_size = img.shape
img_rsz_x0_1 = cv.resize(img, dsize=None, fx=0.1, fy=0.1, interpolation= cv.INTER_NEAREST)

img_srz_x10 = cv.resize(img, dsize=None, fx=10, fy=10, interpolation=cv.INTER_NEAREST)

cv.imwrite('./imagem/resize01.png', img_rsz_x0_1)

cv.imwrite('./imagem/resize1.png', img)
cv.imwrite('./imagem/resize10.png', img_srz_x10)
