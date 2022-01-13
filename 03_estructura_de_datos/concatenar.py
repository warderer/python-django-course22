# concatenar

nombre = 'Azalia'
apellido = 'Escalante'
edad = 28
casada = False

# metodo concatenar
# print('Hola, mi nombre completo es: ' + nombre + ' ' + apellido)
# print('Mi edad es: ' + str(edad) + ' y estado es: ' + str(casada))

# %s
# print('Hola, mi nombre completo es: %s %s' % (nombre, apellido))
# print('Mi edad es: %s y estado es: %s' % (edad, casada))

# format()
# print('Hola, mi nombre completo es: {last_name} {name}'.format(
# 	name=nombre, last_name=apellido))


# fString
print(f'Hola, mi nombre completo es: {nombre} {apellido}')
print(f'Edad: {edad}, y estado: {casada}')