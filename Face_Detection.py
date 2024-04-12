import cv2
import numpy as n
import os
import sys


haar = "C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/haarcascade_frontalface_default.xml"
folder = "C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/CV2 Pictures"
subdata = "Aaron"
path = os.path.join(folder,subdata)
if not os.path.isdir(path): #if path isn't there
    os.mkdir(path) #it will make it

(width,height) = (600,800)
face_cascade = cv2.CascadeClassifier(haar)
webcam = cv2.VideoCapture(0) #0 = internal/built in camera
count = 1
while count<30:
    (_,im) = webcam.read()
    cv2.imshow('Faces',im)
    grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = grey[y:y+h,x:x+w]
        faceresize = cv2.resize(face,(width,height))
        cv2.imwrite('% s/% s.png' % (path,count),faceresize)

    count += 1

    cv2.imshow('Faces',im)
    cv2.waitKey(1)




