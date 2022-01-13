# Funciones lambda

def centigrados_a_farhenheit(grado):
	return grado * 1.8 + 32


# funcion_grado = centigrados_a_farhenheit   # ciudadano de primera clase

# resultado = funcion_grado(10)

# print(resultado)


# sintaxis >> lambda <arguments> : <expresion>


# funcion_grado = lambda grado : grado * 1.8 + 32

# resultado = funcion_grado(15)

# print(resultado)


suma = lambda num1, num2 : num1 + num2

print(suma(10, 30))

