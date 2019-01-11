import numpy as np
import cv2

cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) # scale input down by 50%
    roi = small[30:700, 240:720]  #[y1:y2, x1:x2], crop sides 
    bw = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    egdes = cv2.Canny(roi, 500, 500)
    cv2.imshow('Cam Egdes', egdes)
    cv2.imshow('Cam Raw', bw)
    if not ret:
        break

    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()