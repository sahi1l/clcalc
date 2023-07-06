#/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from calc import calc
import pyperclip as pc
def Calculate(e=None):
    sf = int(sigfig.get())
    ex = (expoQ.get()>0)
    print(f"{ex=}, {sf=}")
    expr = expression.get()
    answer.config(text=calc(expr, exp=ex, sigfig=sf))
    
def CopyInput(e):
    print("copying input")
    pc.copy(expression.get())
def CopyOutput(e):
    print("copying output")
    pc.copy(answer.cget("text"))
    
    

root = Tk()
root.geometry("+500+0")
top = Frame(root)
top.pack()
top.master.title("Type an expression")

prefsF =  Frame(top)
prefsF.grid(row=10,column=0,sticky="w")

expression = ttk.Entry(top,width=50)
expression.grid(row=1,sticky="we")
expression.bind("<Key-Return>", Calculate)
expression.bind("<Command-c>", CopyInput)
expression.bind("<Command-C>", CopyOutput)
expression.focus_set()

answerF = ttk.Frame(top,padding=10)
answerF.grid(row=2,column=0,sticky="we")

#ttk.Label(answerF, text = "Answer:").pack(side="left")
answer = ttk.Label(answerF, text = "--",font="Times 16")
answer.pack(side="left",fill="x")

#exponential or regular
#number of degrees of accuracy
sigfig = ttk.Spinbox(prefsF, from_=0, to=40, width=3, command=Calculate)
#sigfig = Scale(prefsF, from_=0, to=40, orient=HORIZONTAL, showvalue=True)
sigfig.set(3)
sigfig.pack(side="left")
expoQ = IntVar()
expoQ.set(0)
expo = ttk.Checkbutton(prefsF, text="Exponential", variable=expoQ, onvalue=1, offvalue=0, command=Calculate)
expo.pack(side="left")

print(top.winfo_children())


root.mainloop()

