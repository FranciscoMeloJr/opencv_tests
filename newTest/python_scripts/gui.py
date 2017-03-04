#this is the GUI interface:

from tkinter import *

def basic():
    root = Tk()
    theLabel = Label(root, text="This is too easy")
    theLabel.pack()
    root.mainloop()

def advanced():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    buttom1 = Button(topFrame, text="Button 1", fg="red")

    buttom1.pack(side=LEFT)

    root.mainloop()

advanced()