import cv2
import os

location = 'C:/Users/aaron/OneDrive/Pictures/Coding Images'
img = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Subway Surfers.jpg',cv2.IMREAD_COLOR) #1
#img = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Subway Surfers.jpg',cv2.IMREAD_UNCHANGED) #-1
#img = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Subway Surfers.jpg',cv2.IMREAD_GRAYSCALE) #0

b,g,r = cv2.split(img)

cv2.imshow('Cat',b)
#os.chdir(location)
#cv2.imwrite('Grey SubwaySurfers.jpeg',img)

cv2.waitKey(0)
cv2.imshow('Cat',g)
cv2.waitKey(0)
cv2.imshow('Cat',r)
cv2.waitKey(0)
cv2.destroyAllWindows()




