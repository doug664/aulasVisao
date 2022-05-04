# Implementação da operação de alargamento de contraste 

import numpy as np
import cv2 as cv

f = cv.imread('.imagem/Inuyasha-007.webp', cv.IMREAD_UNCHANGED)

f1 = 100
g1 = 50
f2 = 150
g2 = 200
L = 256
shape_f = np.shape(f)
g = np.zeros(shape_f)
for j in range(0, shape_f[1]):
    for i in range(0, shape_f[0]):
        if(f[i,j]<=f1):
            g[i,j]=f[i,j]*g1/f1
        elif(f[i,j]>f1 and f[i,j]<=f2):
            g[i,j]=(f[i,j]-f1)*(g2-g1)/(f2-f1)+g1
        elif(f[i,j]>f2):
            g[i,j]=f(f[i,j]-f2)*((L-1)-g2)/((L-1)-f2)+g2

cv.imwrite('./imagem/inuyasha_stretching.png', g)