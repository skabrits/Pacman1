import math
from tkinter import *


root = Tk()

c = Canvas(root, width=500, height=500)
c.pack()

def screen(c):
    return (c[0]+10)/20*500, (10-c[1])/20*500
def shestriyg (event):
    R = 6
    points = [(R * math.cos(x * 3.14159265359 / 3), R * math.sin(x * 3.14159265359 / 3)) for x in range(6)]
    for i in range(5):
        c.create_line(screen(points[i])[0], screen(points[i])[1], screen(points[i+1])[0], screen(points[i+1])[1])
    c.create_line(screen(points[5])[0], screen(points[5])[1], screen(points[0])[0], screen(points[0])[1])
def sindr (event):
    xy = []
    for x in range(10000):
        xy.append(screen((x/5000*3.14159265359, x))[0])
        xy.append(screen((x, math.sin(x/5000*3.14159265359)))[1])

    c.create_line(xy, fill='blue', smooth=True)
def circ (event):
    c.create_oval([screen((-6,-6)) + screen((6,6))])
def oval (event):
    c.create_oval([screen((-3,-3)) + screen((1,5))])
def hyper (event):
    xy = []
    for x in range(1, 10000):
        xy.append(screen((x/1000, x))[0])
        xy.append(screen((x, 1/(x/1000)))[1])

    c.create_line(xy, fill='blue', smooth=True)

    xy = []
    for x in range(-100000, -1):
        xy.append(screen((x/1000, x))[0])
        xy.append(screen((x, 1/(x/1000)))[1])

    c.create_line(xy, fill='blue', smooth=True)
def Clr ():
    c.delete("all")

b1 = Button(root, text='New sixangle')
b1.bind("<Button-1>", shestriyg)
b1.pack()
b2 = Button(root, text='New sin')
b2.bind("<Button-1>", sindr)
b2.pack()
b2 = Button(root, text='New circle')
b2.bind("<Button-1>", circ)
b2.pack()
b2 = Button(root, text='New oval')
b2.bind("<Button-1>", oval)
b2.pack()
b2 = Button(root, text='New hyperbola')
b2.bind("<Button-1>", hyper)
b2.pack()
b3 = Button(root, text='Clear', command=Clr)
b3.pack()

x1, y1 = screen((0, 0))
x2, y2 = screen((1, 1))

root.mainloop()