#importing cv2 module
import cv2 

print(cv2.__version__)  #prints the version of the openCV library
img=cv2.imread('dog.jpg')  #reads the image provided here

print(img)  #prints the image in 3d array
print(img.shape)
x,y,z=cv2.split(img)    #splits the layers of the image in blue,green and red 
cv2.imshow('imagex',x)    # x,y,z shows the layers of the image
cv2.imshow('imagey',y)     # 'imagex' is the window-name
cv2.imshow('imagez',z)

#cv2.line(img,(0,0),(300,400),(255,255,255)) # draws a line on image
cv2.rectangle(img,(200,15),(384,160),(255,245,255),2)  #draws a rectangle on the image  here 2 is width  -1 to fills the rectangle
cv2.imshow('image',img)  #this shows the image output
 
cv2.imshow('crop',img[0:400,0:500])   #this is used to crop an image 

#wait for window to close
cv2.waitKey(0)   #mili/micro seconds   ---- if given 0 then image wait for infinite time till we stop it
