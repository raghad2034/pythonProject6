from tkinter import *
from tkinter import messagebox
class calcform:
    def __init__(self):
        self.win1=Tk()

        Label(self.win1,text="X")
        self.x2=Entry(self.win1, width=30, bd=2)
        self.x2.pack()
        Label(self.win1,text="Y")
        self.x4=Entry(self.win1)
        self.x6=Label(self.win1)
        self.cb=Button(self.win1,text="calculate ",command= self.calcop)

        self.x4.pack()
        self.x6.pack()
        self.cb.pack()

    def calcop(self):
        num1=int(self.x2.get())
        num2=int(self.x4.get())
        res=num1+num2
        messagebox.showerror("result ",res)

    def open(self):
        self.win1.mainloop()

    def close(self):
        self.win1.destroy()
f1=calcform()
f1=open()

