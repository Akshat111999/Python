#! /usr/bin/python3
import os
import time
import pyqrcode
from pyqrcode import QRCode
from googlesearch import search
web= input("please enter topic: ")
# print(search(web))
url=[]
for i in search(web, stop=3):
	print(i)
	time.sleep(1)
	url.append(i)

print(url)
#img_size= int(input("enter image size, eg: 16x16 --> " ))
#img_name=input("enter image name--> " )
#os.system('qrencode -s '+ img_size + ' -o ' + img_name )
for i in range(3):
    qr= pyqrcode.create(url[i])
    qr.svg("url"+str(i)+".png", scale=8)
