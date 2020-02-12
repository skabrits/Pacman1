from tkinter import *
from random import uniform, sample
from itertools import combinations
import math

str = ["red", "blue", "green", "yellow", "black", "gray", "orange", "purple"]

points = [(uniform(100,400), uniform(100,400), uniform(-3,3), uniform(-3,3), sample(str, 1)[0]) for _ in range(20)]
points = dict(zip(points, points))

root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

def paint(points):
    points = {p:p for p in points.values()}
    for p1, p2 in combinations(points, 2):
        x1,y1,vx1,vy1, col1 = points[p1]
        x2,y2,vx2,vy2, col2 = points[p2]
        if math.hypot(x1-x2, y1-y2) < 20:
            points[p1] = (x1,y1,vx2,vy2, col1)
            points[p2] = (x2,y2,vx1,vy1, col2)
    for old, new in points.items():
        x,y,vx,vy, col = new
        c.create_line(x,y, x+vx, y+vy, fill = col)
        x+=vx
        y+=vy
        if not 0<=x<500:
            vx = -vx
        if not 0<=y<500:
            vy = -vy
        points[old] = x,y,vx,vy, col
    c.delete('kaka')
    for x, y, vx, vy, col in points.values():
        c.create_oval(x - 10.5, y - 10.5, x + 10.5, y + 10.5, fill=col, tags='kaka')
    root.after(20, paint, points)


root.after(20, paint, points)
root.mainloop()