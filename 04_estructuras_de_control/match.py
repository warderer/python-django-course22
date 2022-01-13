# No existía un Switch


# numero = 3


# if numero == 1:
# 	print('El numero es %s' % numero)
# elif numero == 2:
# 	print('El numero es %s' % numero)
# elif numero == 3:
# 	print('El numero es %s' % numero)
# elif numero == 4:
# 	print('El numero es %s' % numero)
# else:
# 	print('El numero no es 1, 2, 3, 4')


# numero = 3

# tabla_numeros = {
# 	1: 'El numero es 1',
# 	2: 'El numero es 2',
# 	3: 'El numero es 3',
# 	4: 'El numero es 4',
# }

# print(tabla_numeros.get(numero, 'NA'))


# >> Structural Pattern Matching (Condicionales de Patrones estructurales)

# keywords match y case


numero = 5

match numero:
	case 1:
		print('El numero es 1')
	case 2:
		print('El numero es 2')
	case 3:
		print('El numero es 3')
	case 4:
		print('El numero es 4')
	case _:
		print('El numero no es 1, 2, 3, 4')