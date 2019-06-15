# Create a program that asks the user to enter their name and their age.
# Print out a message that will tell them the year that they will turn 95 years old.

import time
name=input("enter your name")
age=int(input("enter your age: "))

years=95-age
print(f"your name is {name} and age {age}, you will turn 95 in year ",time.localtime().tm_year+years)
