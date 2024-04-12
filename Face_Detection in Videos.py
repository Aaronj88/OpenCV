import cv2
import sys
import numpy as n
import os


folder = "C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/CV2 Pictures"
haar = "C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/haarcascade_frontalface_default.xml"


(imgs,labels,names,id) = ([],[],{},0)
for (subdir,dir,files) in os.walk(folder):
    for s in dir:
        names[id] = s
        sbjtpath = os.path.join(folder,s)
        for file in os.listdir(sbjtpath):
            path = sbjtpath + "/" + file
            label = id
            imgs.append(cv2.imread(path,0))
            labels.append(int(label))
        id += 1

(imgs,labels) = [n.array(lis) for lis in [imgs,labels]]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(imgs,labels)

(width,height) = (600,800)
face_cascade = cv2.CascadeClassifier(haar)
webcam = cv2.VideoCapture(0)

while True:
    (_,im) = webcam.read()
    grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = grey[y:y+h,x:x+w]
        resized_face = cv2.resize(face,(width,height))
        prediction = model.predict(resized_face)
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,10,100),2)
        if prediction[1]<500:
            cv2.putText(im,"% s - %.0f" %(names[prediction[0]],prediction[1]), (x-10, y-100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,10,100))
        else:
            cv2.putText(im,"Not Recognised", (x-10, y-100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,10,100))
        
        cv2.imshow("Face",im)
        cv2.waitKey(1)






