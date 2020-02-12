from tkinter import *

from laba_502 import mol1, mol2, mol3, mol4

class Window(Toplevel):
    def __init__(self, title, start, update, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        start(self)
        self.update = update
        self.c = Canvas(self, width=500, height=500)
        self.c.pack()
        self.after(20, self.draw)
    def draw(self):
        self.update(self)
        self.c.delete(ALL)
        for x, y, vx, vy in self.points:
            self.c.create_oval(x-2, y-2, x+3, y+3, fill='red')
        self.after(20, self.draw)

root = Tk()
Window('mol1', mol1.start, mol1.update, master=root)
Window('mol2', mol2.start, mol2.update, master=root)
Window('mol3', mol3.start, mol3.update, master=root)
Window('mol4', mol4.start, mol4.update, master=root)
Button(root, text='Exit', command=root.quit).pack()
root.mainloop()

