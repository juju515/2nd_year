from tkinter import *

def cb1():
    print("Wow!")

root = Tk()
but = Button(root, text="Press me", command=cb1)
but.pack()
root.mainloop()
