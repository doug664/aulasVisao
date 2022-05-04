import cv2 as cv
img = cv.imread('./imagem/Inuyasha-008.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('Inuyasha', img)

print(img.shape)
print(type(img))
print(img.dtype)

cv.waitKey(0)
cv.destroyAllWindows()