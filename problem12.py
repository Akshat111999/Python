#! /usr/bin/python3
import os
import time
import pyqrcode
from pyqrcode import QRCode
from googlesearch import search
web= input("please enter topic: ")
# print(search(web))
url=[]
u=0
for i in search(web, stop=3):
	print(i)
	time.sleep(1)
	url.append(i)

print(url)

for i in range(3):
    qr= pyqrcode.create(url[u])
    qr.svg("url"+str(i)+".png", scale=8)
    u+=1
    print(qr.terminal()) 
	
	
os.system('mkdir 
	
os.system('mv *.png /var/www/html/qr')
