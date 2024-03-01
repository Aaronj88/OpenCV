import cv2
import numpy as n

'''img = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Red Porsche.jpeg')
img_resized = cv2.resize(img,(1000,700))
img2 = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Kitten.jpeg')
img2_resized = cv2.resize(img2,(1000,700))

added_img = cv2.addWeighted(img_resized,.6,img2_resized,.8,0) #Blending two images

cv2.imshow('Blended',added_img)



circle = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Dot.png')
star = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Star.png')
subtracted_img = cv2.subtract(star,circle) #subtracting images from each other

kernel = n.ones((50,50),n.uint8)
eroded = cv2.erode(star,kernel) #Trimming (eroding the edges of) an image
print(kernel)

cv2.imshow('Subtracted',subtracted_img)
cv2.imshow('Eroded',eroded)'''

img = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Subway Surfers.jpg')
bordered_image = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=1) #Top, Bottom, Left, Right

cv2.imshow('Subway Surfers',bordered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()





