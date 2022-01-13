# Diccionarios
# <dict> = {}


# diccionario = {'nombre': 'Josue Tamayo'}

#print(diccionario)
#print(type(diccionario))


# >> Añadir nuevos elementos

# En los diccionarios no puede haber llaves repetidas
# elementos = {'a': 1, 'b': 2, 'c':3, 'a': 3} 

# elementos['nombre'] = 'Josue Tamayo'   	# Crea la llave con el valor
# elementos['nombre'] = 'Fulanito'		# Actualiza el valor de la llave


# >> La forma de acceder a los valores mediante sus llaves
# elementos = {'a': 1, 'b': 2, 'c':3, 'd': 4}

# print(elementos['z'])


# Operador de membresía   in

# print('z' in elementos)

# >>  <dict>.get(<key>, <obj>)
# valor = elementos.get('d', 'La llave no existe en el diccionario')  # False

# print(valor)


# >> setdefault(<key>, <value>)
# si no existe la llave, nos añade la nueva llave al diccionario con el valor

# valor = elementos.setdefault('e', 5)
# print(valor)
# print(elementos)


# >> keys(), values(), items()

# elementos = {'a': 1, 'b': 2, 'c':3, 'd': 4}

# llaves = elementos.keys()

# print(tuple(llaves))
# print(type(llaves))


# values = elementos.values()

# print(tuple(values))

# items = elementos.items()

# print(items)


## >> Eliminar elementos del diccionario
## keyword 'del'


elementos = {'a': 1, 'b': 2, 'c':3, 'd': 4}

# del elementos['z']

# print(elementos)


## función pop(<key>) -> return el item eliminado

# valor_eliminado = elementos.pop('b')

# print(valor_eliminado)
# print(elementos)


# >> eliminar todos los elementos  <dict>.clear()

elementos.clear()
print(elementos)