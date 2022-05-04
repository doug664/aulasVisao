#Implementação da operação de computo de um histograma e sua utilização
import cv2 as cv
from matplotlib import pyplot as plt
import os
import numpy as np

def da_hist(img, L=256):
    shape_img = np.shape(img)
    h = np.zeros(L)

    for j in range(0, shape_img[1]):
        for i in range(0, shape_img[0]):
            if(img[i,j] !=0):
                h[img[i,j]] = h[img[i,j]] + 1

    p = np.divide(h , shape_img[0] * shape_img[1])
    return p

f = cv.imread('./imagem/Inuyasha-007.webp', cv.IMREAD_UNCHANGED)

L = 256
fk = range(0, L)
p = da_hist(f, L)

fig = plt.figure()
plt.bar(fk, p)

plt.ylabel("Ocorrencias", fontsize=14)
plt.xlabel('Niveisa de Intensidade', fontsize=14)

fig.savefig('imagem/histogram.png', dpi=300, bbox_inches='tight')

