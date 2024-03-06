import cv2

img = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/OpenCV.jpg')
img2 = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Red Porsche.jpeg')
m = cv2.Canny(img2,200,400) #lower and higher threshold based on the intesity of each pixel
cv2.imshow('Open CV Canny',m)

#y = cv2.cvtColord(img,cv2.COLOR_BGR2HSV)
#cv2.imshow('Open CV Changed',y)


'''(r,c) = img.shape[:2]  #Gives the rows and columns(in terms of pixels) of the picture/shape
x = cv2.getRotationMatrix2D((c/2,r/2),45,1) #c/2 and r/2 is to find the centre of rotation of the image, 45 is rotation amount and 1 is the scale
final = cv2.warpAffine(img,x,(c,r))
cv2.imshow('Open CV Rotated',final)
#print(r,c)'''


#img_bilateral = cv2.bilateralFilter(img,8,75,75) #Bilateral Filter/Blur makes it sharp
#cv2.imshow('Open CV Bilateral Blur/Filter',img_bilateral)


#img_median = cv2.medianBlur(img,15) #Essentially makes it softer, gives it a more even tone
#cv2.imshow('Open CV Median Blur',img_median)


#img_gaussian = cv2.GaussianBlur(img,(15,15),0) #cv2.GaussianBlur blurs the image
#cv2.imshow('Open CV Gaussian Blur',img_gaussian)


#img_bordered = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REFLECT,value=1) # BORDER_REFLECT repeats background
#cv2.imshow('Open CV Bordered',img_bordered)

cv2.waitKey(0)
cv2.destroyAllWindows()