# >> IF | ELSE | ELIF

# if <bool>:
#     # ejecutar nuestro


# if True:
# 	print('Esto es un IF')


# numero = 4

# if numero > 5 and numero < 10:
# 	print('La variable cumple con la condicion')
# else:
# 	print('La condicion no se cumple')


# calificacion = 6

# if calificacion == 10:
# 	print('Felicidades, aprobaste con califiacion perfecta!')
# elif calificacion == 9 or calificacion == 8:
# 	print('Felicidades, aprobaste la materia!')
# elif calificacion == 7 or calificacion == 6:
# 	print('Aprobaste la materia!')
# else:
# 	print('Reprobaste la materia')


# >> Operador ternario
# [value] if [conficion] else [value no cumple]


# calificacion = 5
# color = None  # Verde o rojo

# if calificacion >= 7:
# 	color = 'Verde'
# else:
# 	color = 'Rojo'

# color = 'Verde' if calificacion >= 7 else 'Rojo'


# print(calificacion, color)


# Lógico or

listado = []
mensaje = "Listado vacio"


# if listado:
# 	variable = listado
# else:
# 	variable = mensaje

variable = listado or mensaje

print(variable)