#!/usr/bin/python3

import  socket 
recv_ip="127.0.0.1" # don't shoq your actual ip in code
recv_port=8888  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 >  3  :
    msg=input("plz  enter your message :   ")
    #  converting  str  to bytes-like object 
    nmsg=msg.encode('ascii')
#  sending  data  to target  
    s.sendto(nmsg,(recv_ip,recv_port)) 
    #  recv data  from  recv  
    print(s.recvfrom(10))
s.close()
