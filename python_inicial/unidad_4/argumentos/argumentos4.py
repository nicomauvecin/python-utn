def f(a, *args):
    for arg in args:
        print(arg)


f(0, 1, 2, 3, 4, 5, 6)


def f2(**kwargs):
    if kwargs is not None:
        for clave, valor in kwargs.items():
            print(clave, valor)


f2(nombre="Anna", edad=49)
