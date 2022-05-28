import cv2 as cv
face_cascade = cv.CascadeClassifier('models/haarcascade_frontface_default.xml')

img = cv.imread('./imagem/faces.jpg', cv.IMREAD_UNCHANGED)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 5)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

    cv.imwrite('imagem/img_faces.png', img)