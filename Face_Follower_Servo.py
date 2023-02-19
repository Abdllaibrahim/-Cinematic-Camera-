import cv2
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
from SModule import servo

faceCascade = cv2.CascadeClassifier('/home/pi/Desktop/Projects/Face Flollower Robot/DATA/haarcascades/haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 640)
video_capture.set(4, 480)
servoH= servo(18)
servoV= servo(16)


servoV.SetAngle(90)
servoV.SetAngle(90)
ua= 0
da= 0
ra= 0
la= 0
t=0.1 
n=3
while True:
    
   # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 
   
  # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
        z =x+w
        p =y+h
        print(frames.shape)
        cv2.rectangle(frames,(x,y),(z,p),(225,225,225),10)
        
        cv2.line(frames,  (int(w/2+x),0), (int(w/2+x),y), (225,225,225), 10)
        cv2.line(frames, (0,int(h/2+y)), (x,int(h/2+y)), (225,225,225), 10)
        ox=frames.shape[1]
        oy=frames.shape[0]
        cv2.line(frames,  (x+w,int(h/2+y)), (ox,int(h/2+y)), (225,225,225), 10)

        cv2.line(frames,  (int(w/2+x),y+h), (int(w/2+x),oy), (225,225,225), 10)
        lr= ox- z
        lf= x -0
        lt= y-0
        lb= oy- p       
       
        if lr+50 < lf:
            ra= ra+n
            servoV.SetAngle(90-ra)
            sleep(t)
            print('Key Right was pressed')
            #print(90-ra)
            #print("moving right")
        elif lf+50 < lr:
            ra= ra-n
            servoV.SetAngle(90-ra)
            sleep(t)
            print("moving left")
        else:
            print("Horizontal Equalization")   
        if lt+50 < lb:
            ua= ua+n
            servoH.SetAngle(90-ua)
            sleep(t)
            #print('Key UP was pressed')
            #print(90-ua)
            print("moving up")
        elif lb+50 < lt:
            ua= ua-n
            servoH.SetAngle(90-ua)
            sleep (t)
            #print('Key Down was pressed')
            #print(90-ua)
            print("moving down")
        else:
            print("Vertical Equalization")
            
        # Display the resulting frame
    cv2.imshow('Video', frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
