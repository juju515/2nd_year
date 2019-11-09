from tkinter import *

def updateLabel():
    text = entry.get()
    label['text'] = text

root = Tk()

entry = Entry(root)
entry.grid(row=1, column=1)

button = Button(root, text="Update Label", command=updateLabel)
button.grid(row=2, column=1)

label = Label(root)
label.grid(row=3, column=1)

root.mainloop()
