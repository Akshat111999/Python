#! /usr/bin/python3
import time
from search import google
web= input("please enter topic: ")
# print(search(web))
url=[]
for i in search(web, stop=10):
	print(i)
	time.sleep(1)
	url.append(i)

print(url)	
