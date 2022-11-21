import sqlite3
from tkinter import messagebox
from tkinter import ttk
import re


def crear_base():
    con = sqlite3.connect("database.db")
    return con


def crear_tabla():
    con = crear_base()

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


def alta_cliente(tree, nombre, apellido, email, domicilio, dni):
    con = crear_base()

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
        actualizar_tree(tree)
        messagebox.showinfo("Alta Cliente", "Se agregó el cliente correctamente.")
    else:
        messagebox.showerror("Alta Cliente", "Error en el email.")


def borrar_cliente(tree):
    con = crear_base()

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
    actualizar_tree(tree)
    messagebox.showinfo("Baja Cliente", "Se eliminó el cliente correctamente.")


def actualizar_cliente(tree, nombre, apellido, email, domicilio, dni):
    con = crear_base()

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
    actualizar_tree(tree)
    messagebox.showinfo(
        "Actualización Cliente", "Se actualizó el cliente correctamente."
    )


def actualizar_tree(tree):
    con = crear_base()

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
