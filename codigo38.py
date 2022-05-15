import cv2 as cv
import numpy as np
#import utils as ut

img = cv.imread('./imagem/cidade.jpg', cv.IMREAD_UNCHANGED)

img_edges = cv.Canny(img, 100,200)

cv.imwrite('./imagem/cidade_edges.png', img_edges)