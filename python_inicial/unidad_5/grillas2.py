from tkinter import *

root = Tk()

el_id = Label(root, text="id")
el_id.grid(row=0, column=0, sticky=W)

nombre = Label(root, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)

entry_id = Entry(root)
entry_id.grid(row=0, column=1)

entry_nombre = Entry(root)
entry_nombre.grid(row=1, column=1)


def funcion():
    print("Hola")


boton = Button(root, text="Guardar", command=funcion)
boton.grid(row=2, column=1)


root.mainloop()
