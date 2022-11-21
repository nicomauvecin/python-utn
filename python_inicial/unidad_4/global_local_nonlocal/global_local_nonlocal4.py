a = 5


def nopisa():
    global a
    a = 10
    print(a)


nopisa()
print(a)
