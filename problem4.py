import os
user=input()
if( user.isdigit()):
    print("User input is Number ")
elif "." in user:
    print("number")
else:
    print("User input is string ")
    os.system("useradd -p "+ user)
    password ="hello" + user 

print("user created " + user)
