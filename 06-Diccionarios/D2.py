# 2- Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>

usuario = {}

print(" ")
nombre = input("Ingrese su Nombre: ")
print(" ")
edad = input("Ingrese su Edad: ")
print(" ")
direccion = input("Ingrese su Dirección: ")
print(" ")
telefono = input("Ingrese su Número de Teléfono: ")
print(" ")

usuario['Nombre'] = nombre
usuario['Edad'] = edad
usuario['Direccion'] = direccion
usuario['Telefono'] = telefono

print(f"{usuario['Nombre']} tiene {usuario['Edad']} años, vive en {usuario['Direccion']} y su número de teléfono es {usuario['Telefono']}.")
print(" ")

