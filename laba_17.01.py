from tkinter import *

graf = 480

root = Tk()

def txtw(event):
    txtc.delete('1.0', 'end')
    txtc.insert('1.0', txtn.get('1.0', 'end')+"LOLKEK")
def Return(event):
    settingframe.pack_forget()
    mainframe.pack(fill='both', expand=1)
def Graphics(event):
    txt.delete('1.0', 'end')
    txt.insert('1.0', "Graphics")
def Sound(event):
    txt.delete('1.0', 'end')
    txt.insert('1.0', "Sound")
def Mode(event):
    txt.delete('1.0', 'end')
    txt.insert('1.0', "Mode")
def Subscribe(event):
    sbf.pack(fill='both', expand=1)
    txt.pack_forget()
def Conf(event):
    sbf.pack_forget()
    txt.pack()
    txt.delete('1.0', 'end')
    txt.insert('1.0', "Subscription has been confirmed")
def Settings(event):
    settingframe.pack(fill='both', expand=1)
    mainframe.pack_forget()

mainframe = Frame(root, height=root.winfo_height(), width=root.winfo_width(), bg='gray')
settingframe = Frame(root, height=root.winfo_height(), width=root.winfo_width(), bg='gray')

mainframe.pack(fill='both', expand=1)

btn = Button(mainframe, text="Main", bg="white",fg="black")
# btn.bind("<Button-1>", Main)
btn.pack(fill='both', expand=1)

btn = Button(mainframe, text="Feachers", bg="white",fg="black")
# btn.bind("<Button-1>", Feachers)
btn.pack(fill='both', expand=1)

btn = Button(mainframe, text="Support", bg="white",fg="black")
# btn.bind("<Button-1>", Support)
btn.pack(fill='both', expand=1)

btn = Button(mainframe, text="Settings", bg="white",fg="black")
btn.bind("<Button-1>", Settings)
btn.pack(fill='both', expand=1)

menuFrame = Frame(settingframe, height=50, bg='gray')
bodyFrame = Frame(settingframe, height=300, width=600)

menuFrame.pack(side='top', fill='x')
bodyFrame.pack(side='bottom', fill='both', expand=1)

txt = Text(bodyFrame, font='Arial 14', wrap='word')
txt.pack()

btn = Button(menuFrame, text="Return", bg="white",fg="black")
btn.bind("<Button-1>", Return)
btn.pack(side = 'left')

btn = Button(menuFrame, text="Graphics", bg="white",fg="black")
btn.bind("<Button-1>", Graphics)
btn.pack(side = 'left')

btn = Button(menuFrame, text="Sound", bg="white",fg="black")
btn.bind("<Button-1>", Sound)
btn.pack(side = 'left')

btn = Button(menuFrame, text="Mode", bg="white",fg="black")
btn.bind("<Button-1>", Mode)
btn.pack(side = 'left')

btn = Button(menuFrame, text="Subscribe", bg="white",fg="black")
btn.bind("<Button-1>", Subscribe)
btn.pack(side = 'left')

sbf = Frame(bodyFrame)

name = Label(sbf, text="Write name", bg="white",fg="black")
name.place(x=10, y=30, width=100, height=40)
txtn = Text(sbf, font='Arial 14', wrap='word', bg="gray")
txtn.place(x=120, y=30, width=100, height=40)

nameac = Label(sbf, text="Write nik", bg="white",fg="black")
nameac.place(x=10, y=70, width=100, height=40)
txtc = Text(sbf, font='Arial 14', wrap='word', bg="gray")
txtc.place(x=120, y=70, width=100, height=40)
txtc.bind("<Button-1>", txtw)

btnc = Button(sbf, text="Confirm", bg="white",fg="black")
btnc.bind("<Button-1>", Conf)
btnc.place(x=20, y=150, width=100, height=40)

root.mainloop()