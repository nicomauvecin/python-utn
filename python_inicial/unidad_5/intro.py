from cgitb import text
from tkinter import *

root = Tk()
e = Entry(root)
e.pack()

a = 4
b = 5
c = a + b
d = "Mi resultado"

var = StringVar()
e.config(textvariable=var)
var.set(d)

root.mainloop()
