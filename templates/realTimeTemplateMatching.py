import os
import time
import cv2
import numpy as np
from match import match
import png

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('kafa.png',0)

def detect(gray,frame):
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x, y, w, h) in faces:
        rec = cv2.rectangle(frame, (x-int((x*0.3)), y-int((y*0.8))), (x+w+int((x*0.3)), y+h-int((y*0.3))), (0, 255, 255), 6)
    if (len(faces) != 0):
        roi_color_rec = frame[y - int(h * 0.5):y + int(h * 0.5), x - int(w * 0.25):x + w + int(w * 0.25)]
        if roi_color_rec.shape[0] >= img.shape[0]:
            print(roi_color_rec.shape[0])
            print(img.shape[0])
            roi_color_rec = match(roi_color_rec, img)
        else:
            roi_color_rec = roi_color_rec
        return roi_color_rec

    else:
        print("hata")
        return frame

video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()
    if frame.shape[0] != 0:
        time.sleep(0.2)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = detect(gray, frame)
        if canvas.shape[0] == 0:
            print("resim yok")
            print(canvas.shape)
        else:
            cv2.imshow('Video', canvas)
    else:
        print(frame.shape[0], "frame yok")
    if cv2.waitKey(1) & 0xFF == 27:
        break

video_capture.release()
cv2.destroyAllWindows()