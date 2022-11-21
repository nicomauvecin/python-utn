"""
Alumno: Medina Mauvecin, Esteban Nicolás
DNI: 40275979

La aplicación tiene las siguientes funcionalidades:
    - Guardar clientes nuevos sobre una base SQLite.
    - Eliminar un cliente seleccionado en el Treeview.
    - Actualizar un cliente seleccionado en el Treeview (previamente se debe llenar sus datos). 


La expresión regular que se utilizó es para controlar que el formato del email sea correcto, la misma se encuentra en la función: alta_cliente.
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import sqlite3


def crear_base():
    con = sqlite3.connect("database.db")
    return con


def crear_tabla():
    cursor = con.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS clientes
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            nombre text,
            apellido text,
            email text,
            domicilio,
            dni text
        )
    """
    cursor.execute(sql)
    con.commit()


def alta_cliente(nombre, apellido, email, domicilio, dni):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.match(regex, email):
        cursor = con.cursor()
        data = (nombre, apellido, email, domicilio, dni)
        sql = """
            INSERT INTO clientes(
                nombre,
                apellido,
                email,
                domicilio,
                dni
            ) VALUES (
                ?,
                ?,
                ?,
                ?,
                ?
            )
        """
        cursor.execute(sql, data)
        con.commit()
        actualizar_tree()
        messagebox.showinfo("Alta Cliente", "Se agregó el cliente correctamente.")
    else:
        messagebox.showerror("Alta Cliente", "Error en el email.")


def borrar_cliente():
    item = tree.focus()

    id = tree.item(item)["text"]

    cursor = con.cursor()
    data = (id,)
    sql = """
        DELETE FROM clientes
        WHERE id = ?
    """

    cursor.execute(sql, data)
    con.commit()
    actualizar_tree()
    messagebox.showinfo("Baja Cliente", "Se eliminó el cliente correctamente.")


def actualizar_cliente(nombre, apellido, email, domicilio, dni):
    item = tree.focus()
    id = tree.item(item)["text"]
    cursor = con.cursor()
    data = (nombre, apellido, email, domicilio, dni, id)
    sql = """
        UPDATE clientes
        SET nombre = ?, 
            apellido = ?, 
            email = ?, 
            domicilio = ?, 
            dni = ?
        WHERE id = ?
    """

    cursor.execute(sql, data)
    con.commit()
    actualizar_tree()
    messagebox.showinfo(
        "Actualización Cliente", "Se actualizó el cliente correctamente."
    )


def actualizar_tree():
    rec = tree.get_children()
    for elementos in rec:
        tree.delete(elementos)
    sql = """
        SELECT
            id,
            nombre,
            apellido,
            domicilio,
            email,
            dni
        FROM clientes
        ORDER BY id DESC
    """
    cursor = con.cursor()
    datos = cursor.execute(sql)
    resultado = datos.fetchall()
    for fila in resultado:
        tree.insert(
            "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5])
        )


# Inicia SQLite
con = crear_base()
crear_tabla()

# Inicia TKinter
root = Tk()
root.title("Gestión de Clientes")

# Creación de variables
var_nombre = StringVar()
var_apellido = StringVar()
var_email = StringVar()
var_domicilio = StringVar()
var_dni = StringVar()

# Creación de Labels
nombre = Label(root, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)
apellido = Label(root, text="Apellido")
apellido.grid(row=2, column=0, sticky=W)
email = Label(root, text="Email")
email.grid(row=3, column=0, sticky=W)
domicilio = Label(root, text="Domicilio")
domicilio.grid(row=4, column=0, sticky=W)
dni = Label(root, text="DNI")
dni.grid(row=5, column=0, sticky=W)

# Creacion de Entrys
entry_nombre = Entry(root, textvariable=var_nombre, width=25)
entry_nombre.grid(row=1, column=1)
entry_apellido = Entry(root, textvariable=var_apellido, width=25)
entry_apellido.grid(row=2, column=1)
entry_email = Entry(root, textvariable=var_email, width=25)
entry_email.grid(row=3, column=1)
entry_domicilio = Entry(root, textvariable=var_domicilio, width=25)
entry_domicilio.grid(row=4, column=1)
entry_dni = Entry(root, textvariable=var_dni, width=25)
entry_dni.grid(row=5, column=1)

# Creacion de Treeview
tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=30, minwidth=30, anchor=W)
tree.column("col1", width=100, minwidth=100, anchor=N)
tree.column("col2", width=100, minwidth=100, anchor=N)
tree.column("col3", width=100, minwidth=100, anchor=N)
tree.column("col4", width=120, minwidth=100, anchor=N)
tree.column("col5", width=100, minwidth=100, anchor=N)
tree.grid(column=0, row=9, columnspan=4, pady=30, padx=20)
tree.heading("#0", text="ID")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Apellido")
tree.heading("col3", text="Domicilio")
tree.heading("col4", text="Email")
tree.heading("col5", text="DNI")
actualizar_tree()  # Actualiza con los datos actuales de la base de datos


# Creación de botones
boton_guardar = Button(
    root,
    text="Guardar Cliente",
    command=lambda: alta_cliente(
        var_nombre.get(),
        var_apellido.get(),
        var_email.get(),
        var_domicilio.get(),
        var_dni.get(),
    ),
)
boton_guardar.grid(row=1, column=2)
boton_borrar = Button(root, text="Borrar Cliente", command=borrar_cliente)
boton_borrar.grid(row=3, column=2)
boton_actualizar = Button(
    root,
    text="Actualizar Cliente",
    command=lambda: actualizar_cliente(
        var_nombre.get(),
        var_apellido.get(),
        var_email.get(),
        var_domicilio.get(),
        var_dni.get(),
    ),
)
boton_actualizar.grid(row=5, column=2)
boton_salir = Button(root, text="Salir del programa", command=root.quit)
boton_salir.grid(row=10, column=3, padx=10, pady=10)

root.mainloop()
