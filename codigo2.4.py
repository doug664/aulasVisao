import cv2 as cv

img = cv.imread('./imagem/foto1.png', cv.IMREAD_UNCHANGED)

print(img.shape)
print(type(img))
print(img.dtype)