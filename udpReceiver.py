#!/usr/bin/python

import  socket 
recv_ip="127.0.0.1"
recv_port=4444    

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # to create UDP socket

s.bind((recv_ip,recv_port))  # binding or combinig ip and port to make socket

data=s.recvfrom(100)  

print(data)   # print received message 
