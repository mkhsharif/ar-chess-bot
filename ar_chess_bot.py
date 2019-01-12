import numpy as np
import cv2

cam = cv2.VideoCapture(1)


def draw_lines(img, lines):
    try:
        for line in lines:
            coor = line[0]
            cv2.line(img, (coor[0], coor[1]), (coor[2], coor[3]), [255, 0, 0], 2)
    except:
        pass

def process_img(original_img):
    processed_img = cv2.resize(original_img, (0,0), fx=0.5, fy=0.5) # scale input down by 50%
    processed_img = processed_img[30:700, 240:720]  #[y1:y2, x1:x2], roi
    #processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Cam Raw', processed_img)

    processed_img = cv2.Canny(processed_img, 500, 500)   # Canny edge detection
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0) # Blur dectected edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 50, 15) # Hough lines
    draw_lines(processed_img, lines)
    cv2.imshow('Cam Egdes', processed_img)



while True:
    ret, raw_feed = cam.read()
    if not ret:
        break
    process_img(raw_feed)
 

    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()