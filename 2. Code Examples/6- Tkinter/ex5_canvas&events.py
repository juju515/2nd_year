from tkinter import *

class Counter(object):
    def __init__(self):
        self._counter = 0

    def getCounter(self):
        return self._counter

    def setCounter(self):
        raise NotImplementedError("Not implemented")

    def increment(self):
        self._counter = self._counter + 1

    counter = property(getCounter)

def addtocounter(event):
    counter.increment()
    global counter2
    counter2 = counter2 + 1
    print(counter)
    print(counter2)

def deleteSquare(event):
    canvas.delete(rectR)

root = Tk()

counter = Counter()
global counter2
counter2 = 0

canvas = Canvas(root, width=400, height=400)
canvas.pack()

rectR = canvas.create_rectangle(100,100,120,120,outline="red",fill="red")
canvas.tag_bind(rectR, "<ButtonPress-1>", deleteSquare)

rectG = canvas.create_rectangle(100,100,120,120,outline="green",fill="green")
canvas.tag_bind(rectG, "<ButtonPress-1>", addtocounter)

root.mainloop()
