#importing cv2 module
import cv2 

img=cv2.imread('720p1.jpg')

#lower_reso = cv2.pyrDown(img)
lower_reso = cv2.pyrUp(img)
cv2.imshow('1',lower_reso)

#wait for window to close
cv2.waitKey(0)   #mili/micro seconds   ---- if given 0 then image wait for infinite time till we stop it
