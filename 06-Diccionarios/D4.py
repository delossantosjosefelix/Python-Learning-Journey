# 4- Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario. 

persona = {}

print(" ")
nombre = input("Introduce tu nombre: ")
print(" ")
persona['Nombre'] = nombre
print("Diccionario actualizado:", persona)
print(" ")

print(" ")
apellido = input("Introduce tu apellido: ")
print(" ")
persona['Apellido'] = apellido
print("Diccionario actualizado:", persona)
print(" ")

print(" ")
edad = input("Introduce tu edad: ")
print(" ")
persona['Edad'] = edad
print("Diccionario actualizado:", persona)
print(" ")

print(" ")
sexo = input("Introduce tu sexo: ")
print(" ")
persona['Sexo'] = sexo
print("Diccionario actualizado:", persona)
print(" ")

print(" ")
telefono = input("Introduce tu número de teléfono: ")
print(" ")
persona['Teléfono'] = telefono
print("Diccionario actualizado:", persona)
print(" ")

print(" ")
correo = input("Introduce tu correo electrónico: ")
print(" ")
persona['Correo'] = correo
print("Diccionario actualizado:", persona)
print(" ")
