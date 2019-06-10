import os

path=input("Enter the path")
no_of_dir=int(input("Enter no of directories"))
basic_name=input("Enter basic name of Directory")

os.chdir(path)
for i in range(no_of_dir):
    command='mkdir '+basic_name+str(i)
    os.system('mkdir '+basic_name+str(i))
