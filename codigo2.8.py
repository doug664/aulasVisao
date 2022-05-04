import cv2 as cv

img = cv.imread('./imagem/Inuyasha-008.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('Inuyasha (Channel R)', img[:,:,2])
cv.waitKey(0)
cv.destroyAllWindows()


