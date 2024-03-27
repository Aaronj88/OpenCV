import cv2
import numpy as n

eye = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Eye.jpeg')

blob = cv2.SimpleBlobDetector_Params()
blob.filterByArea = True
blob.minArea = 100
blob.filterByCircularity = True
blob.minCircularity = 0.3
blob.filterByConvexity = True
blob.minConvexity = 0.2
blob.filterByInertia = True
blob.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(blob)
blank = n.zeros((1,1))
blobs = cv2.drawKeypoints(eye,detector.detect(eye),blank,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
num_of_blobs = len(detector.detect(eye))


cv2.imshow('eye Drop',blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()