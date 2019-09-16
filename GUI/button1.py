from tkinter import *
from tkinter import messagebox

def buttonTap():
  messagebox._show("Message", "You received a message") # new dialog box appears showing a message

root = Tk()  # creates a root window
Button(root, text="Click Here", command= buttonTap).pack() #.pack() method is used to organise the blocks in rows and columns

root.mainloop() #mainloop() is an infinite loop used to run the application
