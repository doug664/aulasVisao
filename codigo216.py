# Implementação de operação de limiarização

from cv2 import threshold
import numpy as np
import cv2 as cv
f = cv.imread('./imagem/Inuyasha-007.webp', cv.IMREAD_UNCHANGED)    

threshold = 150

shape_f = np.shape(f)
g = np.zeros(shape_f)
for j in range(0, shape_f[1]):
    for i in range(0, shape_f[0]):
        if(f[i,j]<150):
            g[i,j] = 0
        else:
            g[i,j] = 255

cv.imwrite('./imagem/binary_transf_1.png', g)

g = (f >= threshold)*255
cv.imwrite('./imagem/binary_transf_2.png', g)

