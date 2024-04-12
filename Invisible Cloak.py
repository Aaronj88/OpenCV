import cv2
import numpy as np
import time


original_vid = cv2.VideoCapture("C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Video_for_Cloak.mp4")
time.sleep(1)
count = 0
bg = 0

for i in range(60):
    returnvalue,bg = original_vid.read()
    if returnvalue == False:
        continue
bg = np.flip(bg,axis=1)

while original_vid.isOpened():
    returnvalue,img = original_vid.read()
    if returnvalue == False:
        break
    count = count+1
    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerred = np.array([100,40,40])
    upperred = np.array([180,255,255])
    mask1 = cv2.inRange(hsv,lowerred,upperred)
    lowerred = np.array([155,40,40])
    upperred = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lowerred,upperred)
    mask = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(bg,bg,mask = mask1)
    result2 = cv2.bitwise_and(img,img,mask = mask2)

    final = cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow('Invisible Cloak',final)
    wait = cv2.waitKey(10)
    if wait == 27:
        break



