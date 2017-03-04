#this is the GUI interface:

from tkinter import *

#this will create a little window
def basic():
    root = Tk()
    theLabel = Label(root, text="This is too easy")
    theLabel.pack()
    root.mainloop()

#this will create a buttom
def advanced():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    buttom1 = Button(topFrame, text="Button 1", fg="red")

    buttom1.pack(side=LEFT)

    root.mainloop()

#this will create a buttom + label
def advanced2():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()

    one = Label(root, text="Mazel Tov", bg="red", fg="white")
    one.pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    buttom1 = Button(topFrame, text="Button 1", fg="red")

    buttom1.pack()

    root.mainloop()

advanced2()