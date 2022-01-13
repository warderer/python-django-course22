# *args, n cantidad de argumentos


# def promedio(*args):
# 	return sum(args) / len(args)


# resultado = promedio(5, 20, 5, 9, 10)

# print(resultado)


# def combinacion(p1, p2, *args, p4=500):
# 	print(p1)
# 	print(p2)
# 	print(args)
# 	print(p4)


# combinacion(10, 20, 1, 2, 3, 4, 5, p4=1000)


# **kwargs


# def usuarios(pd=500, **kwargs):
# 	print(kwargs['tamayo'])
# 	print(kwargs['patricio'])
# 	print(pd)


# usuarios(pd=1200, tamayo=[10, 8, 7], patricio=[9, 8, 7])


def combinacion(p1, p2, *args, p3=500, **kwargs):
	print(p1, p2)
	print(args)
	print(kwargs)
	print(p3)


combinacion('hola', 3.14, 1, 2, 3, curso1='Python', curso2='Django')