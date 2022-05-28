
import numpy as np
import cv2 as cv

cap = cv.VideoCapture('./imagem/video.mp4')

__, frame = cap.read()

tck_win = cv.selectROI(frame, False)

p1 = (int(tck_win[0]), int(tck_win[1]))
p2 = (int(tck_win[0] + tck_win[2]), int(tck_win[1] + tck_win[3]))
roi = frame[p1[0]:p2[0], p1[1]:p2[1]]

hsv_roi = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
hmin = 0.
h_max = 25.
s_min = 80.
v_min = 80.

mask = cv.inRange(hsv_roi, np.array((hmin, s_min, v_min,)), np.array((h_max, 255, 255)))

roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

fourcc = cv.VideoWriter_fourcc(*'XVID')
vid_shape = (frame.shape[1], frame.shape[0])
video_out = cv.VideoWriter('./imagem/robot.avi', fourcc, 30.0, vid_shape)

while True:
    ret_cam, frame = cap.read()
    if not ret_cam:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

    ret, tck_win = cv.CamShift(dst, tck_win, term_crit)

    pts = cv.boxPoints(ret)
    pts = np.int0(pts)
    cv.imshow("Tracking", frame)

    video_out.write(frame)

    k = cv.waitKey(60) & 0xff
    if k == 27 : break

cap.release()
video_out.release()
cv.destroyAllWindows()

