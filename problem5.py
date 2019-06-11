import datetime
user_name=input("Enter your name:")

now=datetime.datetime.now()
this_time=now.hour

if this_time in range(6,12):
      print("Good Morning...{}".format(user_name))
elif this_time in range(12,16):
      print("Good Afternoon...{}".format(user_name))
elif this_time in range(16,20):
      print("Good Evening...{}".format(user_name))
else :
      print("Good Night...{}".format(user_name))
