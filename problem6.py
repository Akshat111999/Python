#!/usr/bin/python3


options='''
press 1 to single file view (to view the contents of a file)
press 2 to cat -n view (to show line numbers)  
press 3 to cat -e view (adds $ sign at the end of the line)
press 4 to multiple file view ()
'''

print(options)
op=input("Enter your choice")
if (op==1):
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	print(data)
	f.close()
	
if (op==2):	
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	a=data.split('\n')
	line_no=1
	for i in a:
		print(str(line_no)+" "+i)
		line_no=line_no+1

if (op==3):
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	a=data.split('\n')
	for i in a:
		print(i+"$")	

if (op==4):		
	noOfFiles=int(input('Enter no. of files :'))
	filenames=[]
	print("Press enter after writing a file name")
	print('Enter name of files :')
	for i in range(noOfFiles):
		name=input() 
		filenames.append(name)

	for i in filenames:
		f=open(i,'r')
		print(f.read())
		f.close()	
	
	
	
	
