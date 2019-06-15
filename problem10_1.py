#Sender's end
#!/usr/bin/python

import socket as s
ip="127.0.0.1"
port=4444

sks=s.socket(s.AF_INET,s.SOCK_DGRAM)
cont=1

while cont==1:
	msg=raw_input("enter message")
  sks.sendto(msg,(ip,port))
	data=sks.recvfrom(100)
	print(data[0])   # n data[0] message is written and on data[1] socket(ip+port) is written
	cont=input("Press 1 for continue and 0 for end : ")
