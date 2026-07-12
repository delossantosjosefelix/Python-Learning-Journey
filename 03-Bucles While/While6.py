#Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas. 

print("Ingrese líneas de texto (presione Enter sin escribir nada para finalizar):\n")

while True:
    linea = input()
    if linea == "":
        break
    print(linea.upper())
