import cv2

cars = cv2.VideoCapture('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/cars.mp4')
car_cascade = cv2.CascadeClassifier('C:/Users/aaron/OneDrive/Documents/Coding/Jetlearn/Open CV/cars.xml')

while True:
    ret,frame = cars.read()
    grey_cars = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    num_cars = car_cascade.detectMultiScale(grey_cars,1.1,1)

    for (x,y,w,h) in num_cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    
    cv2.imshow('Video of Cars',frame)
    if cv2.waitKey(33) == 27:
        break
cv2.destroyAllWindows()