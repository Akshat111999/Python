import os

path=input("Enter the path")
no_of_dir=int(input("Enter no of directories"))
basic_name=input("Enter basic name of Directory")

os.chdir(path)
if len(basic_name)<1:
    basic_name=" "
    print("Directory name is small")
else:    
    for i in range(no_of_dir):
        command='mkdir '+basic_name+str(i)
        os.system('mkdir '+basic_name+str(i))
print ("Directories created")      


