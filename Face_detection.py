#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 01:48:15 2018

@author: himanshu
"""
#Importing the libraries
import cv2
#Loading Cascades
face_cascades=cv2.CascadeClassfier('haarcascade_frontalface_default.xml')
eye_cascades=cv2.CascadeClassfier('haarcascade_eye.xml')
#Defining a function that will do detection
def detect(gray,frame):
    faces=face_cacades.detectMultiscale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiscale(roi_gray,1.1,3)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame
#Doing Face Recognition with webcam
video_captur=cv2.VideoCapture(1) 
while True:
    _,frame=video_capture.read()
    gray=cv2.cvtocolor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitkey(1)&0xFF==ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()    

       