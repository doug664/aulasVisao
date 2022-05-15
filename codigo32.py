import cv2 as cv
import numpy as np

im_br = cv.imread('./imagem/Inuyasha-007.webp', cv.IMREAD_UNCHANGED)

mask = np.array([0, 1, 0],[1, -4,  1],[0, 1, 0], np.float32)

im_tr = cv.filter2D(im_br.astype(np.float32), -1, mask)

c=-1
im_agc = im_br + c * im_tr
cv.imwrite('./imagem/inuyasha_sharpened.png', im_agc)

