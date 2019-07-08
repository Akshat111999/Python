import cv2
#starting camera
img=cv2.imread('human.jpeg')
#calling classifier
casclf=cv2.CascadeClassifier('facedata.xml')
#here add eye data in casclf2  for detecting eyes 

#loading face data
#cap=cv2.VideoCapture(0)
#first camera

        
#while cap.isOpened():
##h=cv2.imread(img)
#now we can apply classifier in live frame
face=casclf.detectMultiScale(img,1.5,5)  #classifier tuning parameter
    #print(face)
for x,y,h,w in face:
        cv2.rectangle(img,(x,y),(x+h,y+w),(0,0,255),2)

cv2.imshow('image', img)
cv2.waitKey(0)
#cv.destroyWindow('live')  #destroy particular window
cv2.destroyAllWindows()  #destroy all windows

#to close camera
#cap.release()
