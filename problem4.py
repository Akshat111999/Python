import os
import crypt
print("Username should contain only letters or combination of letters and numbers")
user=input("Enter username: ")
if( user.isdigit()):
    print("User input is Number ")
elif "." in user:
    print("User input is a number")
else:
    #print("User input is string ")
    password ="hello" + user
    encpass=crypt.crypt(password,'123')
    os.system('sudo useradd -p '+ encpass +' '+user)
    print("user created " + user)
