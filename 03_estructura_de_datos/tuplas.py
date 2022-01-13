# >> Tuplas (Se puede considerar como una Constante)
# tupla = ()

#              0       1     2      3        4
mi_tupla = ('Python', 10, 3.1416, True, (1, 2, 3))


# >> Acceder a un elemento

# print(mi_tupla[10])

# tupla de un solo elemento

# tupla = (1,)
# print(tupla)


## tupla anidadas

#                0          1
tupla_ani = ((1, 2, 3), (4, 5, 6))

# print(tupla_ani[1][1])


## subtuplas
## tuple[start:end]
courses = ('Python', 'Django', 'Flask', 'JavaScript', 'React')

# print(courses[1:4])
# print(courses[2:])
# print(courses[:2])


# Modificar una tupla (Inmutable)

# courses[0] = 'C#'


# courses = (1, 2, 3, 4)
# print(courses)

# GENERO = (('F', 'Femenino'), ('M', 'Masculino'), ('I', 'Indefinido'))

# ESTADOS = (('AGS', 'Aguascaliente'), (), ())


# Tuplas, solo tiene 2 métodos, count(), index()