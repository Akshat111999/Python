import datetime
user_name=input("Enter your name:")

now=datetime.datetime.now().hour

if now < 12:
      print("Good Morning...{}".format(user_name))
elif 12<= now <16 :
      print("Good Afternoon...{}".format(user_name))
elif 16<= now  < 19:
      print("Good Evening...{}".format(user_name))
else :
      print("Good Night...{}".format(user_name))
