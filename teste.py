import cv2 as cv
imagem = cv.imread("./imagem/foto1.png")
cv.imshow("Imagem", imagem)
cv.waitKey(0)
cv.destroyAllWindows()