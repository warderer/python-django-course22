# Casting, casteo de datos en Python

# Implicita

a = 10
b = 1.5

c = a + b
#print(c)
#print(type(c))

# Explicita
# float(), str(), int(), bool(), list(), tuple()
# hex(), oct(), bin()

numero = 10.10
num_int = int(numero)

#print(num_int)
#print(type(num_int))

# convertir de float -> int
# convertir de float -> string
# convertir de string -> float
# convertir de string -> int
# convertir de int -> string
# convertir de int -> float
# convertir boolean

# False
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))

# Verdadero
print(bool(25))
print(bool(25.25))
print(bool("hola"))
print(bool([1, 2, 3]))
