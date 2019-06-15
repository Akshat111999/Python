#Receiver's end
#!/usr/bin/python

import socket as s
ip="127.0.0.1"
port=4444

sk=s.socket(s.AF_INET,s.SOCK_DGRAM)
sk.bind((ip,port))
cont=1
while cont==1:
	data=sk.recvfrom(100)
	print(data[0])
	msg=raw_input("enter your msg :")
	sk.sendto(msg,data[1])

	cont=input("Press 1 for continue and 0 for end : ")
  
