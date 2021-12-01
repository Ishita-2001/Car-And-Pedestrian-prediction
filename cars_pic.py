import cv2
from random import randrange

# Load the pre-trained data
trained_data= r'C:\Users\ISHITA\Desktop\ML project\UEM_PROJECT_COM\car.xml'
car_tracker= cv2.CascadeClassifier(trained_data)

# read the given image
img = cv2.imread(r'C:\Users\ISHITA\Desktop\ML project\UEM_PROJECT_COM\car1.jpg')

# grey-scaling the image
gr_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detecing co-ordinates of the cars
cars= car_tracker.detectMultiScale(gr_img)
print(cars)

# Marking the cars with rectangles
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),4)

# Displaying the image
cv2.imshow('cars',img)
cv2.waitKey()

print('Hey!')
