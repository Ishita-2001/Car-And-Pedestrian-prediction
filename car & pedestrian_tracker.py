import cv2

video=cv2.VideoCapture(r'C:\Users\ISHITA\Desktop\ML project\UEM_PROJECT_COM\pedestrian.mp4')

#pre trained pedestrian and car classifier
car_tracker_file=(r'C:\Users\ISHITA\Desktop\ML project\UEM_PROJECT_COM\car.xml')
pedestrian_tracker_file=(r'C:\Users\ISHITA\Desktop\ML project\UEM_PROJECT_COM\pedestrian.xml')

#create car n pedestrian classifier
car_tracker=cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker=cv2.CascadeClassifier(pedestrian_tracker_file)

#run forever untill car stop
while True:
    
    (read_successful,frame)=video.read()
  
    gr_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   
    #detect cars n pedestrian
    cars=car_tracker.detectMultiScale(gr_frame)
    pedestrians=pedestrian_tracker.detectMultiScale(gr_frame)

    #draw rectangle around cars
    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x+1,y+2),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    #draw rectangle around pedestrian
    for(x,y,w,h) in pedestrians:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    #display
    cv2.imshow('car n pedestrians',frame)
    key = cv2.waitKey(1)
    
    #stopping condition
    if key == 83 or key== 115:
        break

# release the VideoCapture object
video.release()
    
print('Press "s" to stop')

print('Hey!')
