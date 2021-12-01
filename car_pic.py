import cv2

#load some pre-trained data
car_tracker=cv2.CascadeClassifier(r'C:\Users\ISHITA\Desktop\ML project\UEM_PROJECT_COM\car.xml')

#read a chosen image
img=cv2.imread(r'C:\Users\ISHITA\Desktop\ML project\UEM_PROJECT_COM\car.jpg')

#grey-scaling the image
gr_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting Cars in Multiscale
cars=car_tracker.detectMultiScale(gr_img)
print(cars)

#Marking the cars with a rectangle
(x,y,w,h)=cars[1]
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#display the image
cv2.imshow('car',img)
cv2.waitKey()
print('Hey!')
