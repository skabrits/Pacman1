from tkinter import *
from random import randint
import math
import json

RADIUS = 2.5
SPEED = 75
MAX_VALUE = 40
stop = False
FS = 5

class point:
    def __init__(self, x, y, vx, vy, col, in_colis):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.col = col
        self.in_colis = in_colis
    def draw(self):
        if (self.in_colis > 0):
            self.in_colis -= 1
        else:
            self.col = 'yellow'
        c.create_oval(self.x - RADIUS, self.y - RADIUS, self.x + RADIUS, self.y + RADIUS, fill=self.col)
    def colision(self, point1):
        if (math.hypot(self.x - point1.x, self.y - point1.y) <= 2*RADIUS):
            (point1.vx, self.vx) = (self.vx, point1.vx)
            (point1.vy, self.vy) = (self.vy, point1.vy)
            self.col = 'red'
            point1.col = 'red'
            point1.in_colis = 4
            self.in_colis = 4
    def wallcol(self):
        if (self.x <= RADIUS+3 or 500 - self.x <= RADIUS):
            self.vx = -self.vx
            self.col = 'red'
            self.in_colis = 4
        if (self.y <= RADIUS+3 or 500 - self.y <= RADIUS):
            self.vy = -self.vy
            self.col = 'red'
            self.in_colis = 4
points = [point(randint(100,400), randint(100,400), randint(-SPEED,SPEED), randint(-SPEED,SPEED), 'yellow', 2) for _ in range(randint(1,MAX_VALUE))]

root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

def paint(points):
    for i in points:
        i.x += i.vx/30
        i.y += i.vy/30
        i.wallcol()
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            points[i].colision(points[j])
    c.delete('all')
    drawWalls()
    for i in points:
        i.draw()
        global stop
    if (not(stop)):
        root.after(FS, paint, points)
def drawWalls():
    c.create_rectangle(3, 3, 500, 500, outline='black')
def stp(e):
    global stop
    stop = True
def strt(e):
    global stop
    stop = False
    root.after(FS, paint, points)
def save(e):
    global stop
    stop = True
    file = open('Molecula_Info', 'w')
    json.dump([(i.x, i.y, i.vx, i.vy, i.col, i.in_colis) for i in points], file)
    file.close()
def load(e):
    global stop
    stop = True
    myFile = open('Molecula_Info', 'r')
    global  points
    points = [point(x, y, vx, vy, col, in_colis) for (x, y, vx, vy, col, in_colis) in json.load(myFile)]
    myFile.close()
    root.after(FS, paint, points)
    stop = True



b1 = Button(root, text='Start')
b1.bind("<Button-1>", strt)
b1.pack()
b2 = Button(root, text='Stop')
b2.bind("<Button-1>", stp)
b2.pack()
b1 = Button(root, text='Save')
b1.bind("<Button-1>", save)
b1.pack()
b2 = Button(root, text='Load')
b2.bind("<Button-1>", load)
b2.pack()

drawWalls()
# root.after(5, paint, points)
root.mainloop()