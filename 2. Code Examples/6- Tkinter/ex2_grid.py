from tkinter import *

root = Tk()

but1 = Button(root, text="AAAAAAAAAAA")
but2 = Button(root, text="BBBBBBBBBBB")
but3 = Button(root, text="CCCCCCCCCCC")
but4 = Button(root, text="DDDDDDDDDDD")

but1.grid(row=1, column=1)
but2.grid(row=1, column=2)
but3.grid(row=2, column=1)
but4.grid(row=2, column=2)

root.mainloop()
