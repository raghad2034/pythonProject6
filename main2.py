from tkinter import *
from tkinter import messagebox
import re

def calcop():
    np=re.compile(r"\d{1,6}$")
    if np.match(x2.get()) and np.match(x4.get()):
        num1=int(x2.get())
        num2=int(x4.get())
        res=num1+num2
        messagebox.showerror("result ", res)
    else:
        messagebox.showerror("error", "num are invalid ")
#    messagebox.showerror("result ",res)

win1=Tk()
Label(win1,text="X").pack()
x2=Entry(win1, width=30, bd=2)
x2.pack()
Label(win1,text="Y").pack()
x4=Entry(win1)
x6=Label(win1)
cb=Button(win1,text="calculate",command=calcop)
x4.pack()
x6.pack()
cb.pack()

win1.mainloop()
fh=open("result.txt","at")
fh.write(f"{num1}+{num2}={res}")


