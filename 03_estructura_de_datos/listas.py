# Listas

# >> Crear

#           -5        -4          -3         -2     -1
#            0         1           2          3      4
curso = ['Python', 'Django', 'JavaScript', 'Java', 'C#']


list_one = [1, 2, 3, 4]
list_two = [1, 3.1416, 'Python', True, list_one]
list_cast = list('Hola')

# print(list_one)
# print(list_two)
# print(list_cast)

# print(type(list_one))


# Acceder elementos de una lista
#print(len(list_one))
#print(list_two[len(list_two) - 1])
#print(list_two[-1])

# Listas anidadas [][][]
lista = [1, 2, 3, ['a', 'b', [5, 6, 7]]]
# print(lista[3][2][0]) # 5

# Sublistas <list>[start:end:step]
# print(curso[0:3]) # primero elementos de la lista
# print(curso[2:])
# print(curso[:3])
# print(curso[::-1])



# Actualizar un elemento de la lista
list_two[0] = 10
# print(list_two)


# Añadir elementos a la lista
# append()
list_one.append(5)
#print(list_one)
#print(list_two)

# insert(indice, value)
list_one.insert(0,'A')
list_one.insert(3,'B')

# list_one = ['A', 1, 2, 'B', 3, 4, 5, 6, 7, 8]
other_list = [6, 7, 8]
#list_one.append(other_list)


# >> extends()
# list_one += other_list
list_one.extend(other_list)


# Eliminar elementos de la lista
# del

del list_one[0]
del list_one[2]

# remove(value)
list_one.remove(2)

# pop(indice) default -1
list_one.pop()


# Todos los elementos de la lista
# clear()
list_one.clear()


# del list_one[:]
# print(list_one)


# help(list_one)