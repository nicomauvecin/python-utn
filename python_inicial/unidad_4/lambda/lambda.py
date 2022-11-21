def normal(a, b):
    return a + b


print(normal(1, 2))


b = lambda a, b: a + b
print(b(2, 3))


numero = lambda num: num % 2 != 0

print(numero(4))
print(numero(5))
