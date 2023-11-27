#/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from calc import calc
import pyperclip as pc
def Calculate(e=None):
    sf = int(sigfig.get())
    ex = (expoQ.get()>0)
    expr = expression.get()
    answer.config(text=calc(expr, exp=ex, sigfig=sf))
    
def CopyInput(e):
    pc.copy(expression.get())
def CopyOutput(e):
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
sigfigL = ttk.Label(prefsF, text="Significant Digits:")
sigfig = ttk.Spinbox(prefsF, from_=0, to=40, width=3, command=Calculate)
#sigfig = Scale(prefsF, from_=0, to=40, orient=HORIZONTAL, showvalue=True)
sigfig.set(3)
sigfigL.pack(side="left")
sigfig.pack(side="left")
expoQ = IntVar()
expoQ.set(0)
expo = ttk.Checkbutton(prefsF, text="Scientific Notation", variable=expoQ, onvalue=1, offvalue=0, command=Calculate)
expo.pack(side="left",padx=20)
help1 = ttk.Label(prefsF, text=" ⌘C\n⇧⌘C",justify="right",foreground="#888")
help2 = ttk.Label(prefsF, text=" copy input\ncopy output",justify="left",foreground="#888")
help1.pack(side="left",anchor="e")
help2.pack(side="left",anchor="w")


root.mainloop()

