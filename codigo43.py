
import cv2 as cv
import imutils as imu
from imutils.object_detection import non_max_suppression

import numpy as np

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

img = cv.imread('./imagem/pedestre.jpg')

#img = imu.resize(img, width=min(400, img.shape[1]))

(rects, weights) = hog.detectMultiScale(img, winStride=(4, 4), padding=(4, 4), scale=1.05)

rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
rects_nms = non_max_suppression(rects, probs=None, overlapThresh=0.65)

for (x_a, y_a, x_b, y_b) in rects_nms:
    cv.rectangle(img, (x_a, y_a), (x_b, y_b), (0, 0, 255), 2)

cv.imwrite('./imagem/img_ped.png', img)