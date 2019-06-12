import getpass
import pwd
print(getpass.getuser())    #to see current user---uses getpass library
for p in pwd.getpwall():    #to see the 
    print (p[0])
