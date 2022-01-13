# >> For
# for <value> in <iterable>:
# 	print(value)


# lista = [0, 1, 2, 3, 4]

# for num in lista:
# 	print(num)


# >> function range()
# [start:end:step]

# for num in range(10, 30, 2):
# 	print(num)

# palabra = 'parangaricurimicuaro'

# for letra in palabra:
# 	print(letra)


# dicc = {'nombre': 'Azalia', 'apellido': 'Escalante'}
# # <dict>.keys()
# # <dict>.values()
# # <dict>.items()

# # unpack = desempaquetado

# for key, value in dicc.items():
# 	#print(key, value)
# 	if key == 'nombre':
# 		print(value)


# >> function enumerate()   ['josue', 'tamayo']


# numeros = [10, 20, 30, 40, 50]

# # pos = 0

# # for numero in numeros:
# # 	print(pos, numero)
# # 	pos += 1

# for indice, numero in enumerate(numeros):
# 	print(indice, numero)


# >> listas anidadas


lista_anidada = [[1, 2, 3], [12, 4, 5], [9, 4, 3]]

for lista in lista_anidada:
	for numero in lista:
		print(numero)