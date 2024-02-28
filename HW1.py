import cv2
import os

img = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Subway Surfers.jpg',cv2.0)



os.chdir(location)
cv2.imwrite('Grey SubwaySurfers.jpeg',img)

cv2.imshow('Cat')
cv2.waitKey(0)
cv2.destroyAllWindows()