import  socket 
recv_ip="127.0.0.1"
recv_port=4444      

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # to create udp socket

#  sending  data  to target  
s.sendto("hello",(recv_ip,recv_port))  # sendto used to send data to receiver end 
