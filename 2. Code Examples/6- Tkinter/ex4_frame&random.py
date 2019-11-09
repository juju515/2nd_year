from tkinter import *
import random

def cb1():
    xpos = random.randint(1,400)
    ypos = random.randint(1,400)
    can.create_line(xpos, ypos, xpos+40, ypos+40, fill="red")

def cb2():
    xpos = random.randint(1,400)
    ypos = random.randint(1,400)
    can.create_polygon(xpos, ypos, xpos+40, ypos, xpos+40, ypos+40, xpos, ypos+40, fill="blue")

def cb3():
    xpos = random.randint(1,400)
    ypos = random.randint(1,400)
    can.create_oval(xpos, ypos, xpos+40, ypos+40, fill="green")

root = Tk()

can = Canvas(root, width=400, height=400)
can.pack(side=TOP)

frame = Frame(root)

but1 = Button(frame, text="line", command=cb1)
but1.grid(row=1, column=1)

but2 = Button(frame, text="Square", command=cb2)
but2.grid(row=1, column=2)

but3 = Button(frame, text="circle", command=cb3)
but3.grid(row=1, column=3)

frame.pack(side=BOTTOM)

root.mainloop()
