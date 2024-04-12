import cv2

Car = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Red Porsche.jpeg')
(r,c) = Car.shape[:2]

Car_Smol = cv2.resize(Car,(c-100,r-100))
Car_BgBlur = cv2.copyMakeBorder(Car_Smol,50,50,50,50,cv2.BORDER_REFLECT, value = 1)
Car_Blurry = cv2.GaussianBlur(Car,(15,15),0)
Car_Outlined = cv2.Canny(Car,200,400)
Car_Very_Blurry = cv2.bilateralFilter(Car,8 ,1000,1000)
Car_Sharp = cv2.bilateralFilter(Car,8, 75, 75)



cv2.imshow('Porsche 911 GT2 RS', Car)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('Porsche 911 GT2 RS', Car_BgBlur)
cv2.waitKey(100)
cv2.destroyAllWindows()


cv2.imshow('Porsche 911 GT2 RS', Car_Blurry)
cv2.waitKey(400)
cv2.destroyAllWindows()


cv2.imshow('Porsche 911 GT2 RS',Car_Outlined)
cv2.waitKey(750)
cv2.destroyAllWindows()


cv2.imshow('Porsche 911 GT2 RS',Car_Very_Blurry)
cv2.waitKey(650)
cv2.destroyAllWindows()

cv2.imshow('Porsche 911 GT2 RS',Car_Sharp)
cv2.waitKey(800)
cv2.destroyAllWindows()

cv2.imshow('Porsche 911 GT2 RS', Car)
cv2.waitKey(0)
cv2.destroyAllWindows()