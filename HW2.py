import cv2

Kitty = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Kitten.jpeg')
Car = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Red Porsche.jpeg')


Bilateral_Car = cv2.bilateralFilter(Car,8,75,75)
cv2.imshow('Open CV Bilateral Blur/Filter',Bilateral_Car)
cv2.waitKey(0)
cv2.destroyAllWindows()

Median_Kitten = cv2.medianBlur(Kitty,15)
cv2.imshow('Open CV Median Blur',Median_Kitten)
cv2.waitKey(0)
cv2.destroyAllWindows()

Gaussian_Car = cv2.GaussianBlur(Car,(15,15),0)
cv2.imshow('Open CV Gaussian Blur',Gaussian_Car)
cv2.waitKey(0)
cv2.destroyAllWindows()

Kitten_Bordered = cv2.copyMakeBorder(Kitty,100,100,100,100,cv2.BORDER_REFLECT,value=1)
cv2.imshow('Open CV Bordered',Kitten_Bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()

Car_Outlined = cv2.Canny(Car,200,400)
cv2.imshow('Open CV Canny',Car_Outlined)
cv2.waitKey(0)
cv2.destroyAllWindows()

(r,c) = Kitty.shape[:2]
x = cv2.getRotationMatrix2D((c/2,r/2),180 ,1)
Kitten_Rotated = cv2.warpAffine(Kitty,x,(c,r))
cv2.imshow('Kitten Rotated',Kitten_Rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()





