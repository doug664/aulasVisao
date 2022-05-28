import cv2 as cv
import sys

tracker = cv.TrackerKCF_create()

cap = cv.VideoCapture('./imagem/video.mp4')

__, frame = cap.read()

bbox = cv.selectROI(frame, False)

tracker.init(frame, bbox)

fourcc = cv.VideoWriter_fourcc(*'XVID')
vid_shape = (frame.shape[1], frame.shape[0])
video_out = cv.VideoWriter('./imagem/robot.avi', fourcc, 30.0, vid_shape)

while True:
    ret_cam, frame = cap.read()
    if not ret_cam:
        break

    ret_tckr, bbox = tracker.update(frame)

    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

    cv.imshow("Tracking", frame)

    video_out.write(frame)

    k = cv.waitKey(1) & 0xff
    if k == 27 : break

cap.release()
video_out.release()
cv.destroyAllWindows()

