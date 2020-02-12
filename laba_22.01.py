from tkinter import *
from tkinter.ttk import *
import random

random.seed()

def Oval (event):
    radx = random.randint(1, 499)
    rady = random.randint(1, 499)
    corx = random.randint(radx, 499)
    cory = random.randint(rady, 499)
    col = random.sample(str, 1)
    c.create_oval(corx, cory, radx, rady, fill = col[0], outline =col[0])
def Rect (event):
    radx = random.randint(1, 499)
    rady = random.randint(1, 499)
    corx = random.randint(radx, 499)
    cory = random.randint(rady, 499)
    col = random.sample(str, 1)
    c.create_rectangle(corx, cory, radx, rady, fill = col[0], outline =col[0])
def Clr (event):
    c.delete("all")


str = ["red", "blue", "green", "yellow", "black", "gray", "orange", "purple"]
root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()
b1 = Button(root, text='New oval')
b1.bind("<Button-1>", Oval)
b1.pack()
b2 = Button(root, text='New rectangle')
b2.bind("<Button-1>", Rect)
b2.pack()
b2 = Button(root, text='Clear', command=Clr)
b2.bind("<Button-1>", Clr)
b2.pack()

root.mainloop()