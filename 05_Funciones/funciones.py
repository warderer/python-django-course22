# >> Funciones
# los nombres deben ser en minusculas y usar el snake_case

# def nombre_funcion(params_opcionales):
# 	return some_value

# mutables e inmutables

# def suma(num1, num2):	
# 	return num1 + num2, '2do valor'


# numero_1 = 5
# numero_2 = 10

# # unpack o desempaquetar
# resultado, texto = suma(numero_1, numero_2)

# print(resultado)
# print(texto)


# >> Parametros opcionales


def calcular_area_circulo(radio, msj, otro_radio, pi=3.141592):
	return pi * (radio ** 2)


resultado = calcular_area_circulo(5, 'mensaje', 8)


print(resultado)