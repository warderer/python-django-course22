

curso = 'Python'		# Variable global

def imprimir_curso():
	global curso

	curso = 'Django'

	#curso = 'Java'		# Variable local
	print(curso)


imprimir_curso()

print(curso)