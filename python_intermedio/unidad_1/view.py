from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from model import alta_cliente
from model import borrar_cliente
from model import actualizar_cliente
from model import actualizar_tree


def vista_principal(root):
    root.title("Gestión de Clientes")

    # Creación de variables
    var_nombre = StringVar()
    var_apellido = StringVar()
    var_email = StringVar()
    var_domicilio = StringVar()
    var_dni = StringVar()

    # Creación de Labels
    nombre = Label(root, text="Nombre")
    nombre.grid(row=1, column=0, sticky="w")
    apellido = Label(root, text="Apellido")
    apellido.grid(row=2, column=0, sticky="w")
    email = Label(root, text="Email")
    email.grid(row=3, column=0, sticky="w")
    domicilio = Label(root, text="Domicilio")
    domicilio.grid(row=4, column=0, sticky="w")
    dni = Label(root, text="DNI")
    dni.grid(row=5, column=0, sticky="w")

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
    tree.column("#0", width=30, minwidth=30, anchor="w")
    tree.column("col1", width=100, minwidth=100, anchor="n")
    tree.column("col2", width=100, minwidth=100, anchor="n")
    tree.column("col3", width=100, minwidth=100, anchor="n")
    tree.column("col4", width=120, minwidth=100, anchor="n")
    tree.column("col5", width=100, minwidth=100, anchor="n")
    tree.grid(column=0, row=9, columnspan=4, pady=30, padx=20)
    tree.heading("#0", text="ID")
    tree.heading("col1", text="Nombre")
    tree.heading("col2", text="Apellido")
    tree.heading("col3", text="Domicilio")
    tree.heading("col4", text="Email")
    tree.heading("col5", text="DNI")
    actualizar_tree(tree)  # Actualiza con los datos actuales de la base de datos

    # Creación de botones
    boton_guardar = Button(
        root,
        text="Guardar Cliente",
        command=lambda: alta_cliente(
            tree,
            var_nombre.get(),
            var_apellido.get(),
            var_email.get(),
            var_domicilio.get(),
            var_dni.get(),
        ),
    )
    boton_guardar.grid(row=1, column=2)
    boton_borrar = Button(root, text="Borrar Cliente", command=borrar_cliente(tree))
    boton_borrar.grid(row=3, column=2)
    boton_actualizar = Button(
        root,
        text="Actualizar Cliente",
        command=lambda: actualizar_cliente(
            tree,
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
