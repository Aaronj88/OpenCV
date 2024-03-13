import cv2
car = cv2.imread('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/Red Porsche.jpeg')

pos = (0,15)
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 1
color = (0,255,150)
thick = 2
text = cv2.putText(car,'This is a car',pos,font,font_scale,color,thick,cv2.LINE_4)
cv2.imshow('Car with text',text)


'''centerp = (100,100)
radius = 50
color = (30,15,255)
thick = -1
circle = cv2.circle(car,centerp,radius,color,thick)
cv2.imshow('Porsche with a circle',circle)'''


'''startp = (15,15)
endp = (30,200)
color = (0,0,255)
thick = -1
rectangle = cv2.rectangle(car,startp,endp,color,thick)
cv2.imshow('Porsche with a rectangle',rectangle)'''


'''p1 = (100,50)
p2 = (300,40)
color = (30,15,255)
thick = 8
line = cv2.line(car,p1,p2,color,thick)
cv2.imshow('Porsche with a line',line)'''


cv2.waitKey(0)
cv2.destroyAllWindows()