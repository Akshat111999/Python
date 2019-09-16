from tkinter import *
import webbrowser

def openBrowser():
  webbrowser.open_new_tab("https://www.google.com")  # opens a new tab in the browser

root = Tk()  // creates a root window
Button(root, text="Open Browser", command= openBrowser).pack() #.pack() method is used to organise the blocks in rows and columns

root.mainloop() # mainloop() is an infinite loop used to run the application
