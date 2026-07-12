#Escribir un programa que indica cuantos valores positivos, negativos o 0 fueron ingresados por el teclado de un conjunto de 10 datos (utilizar estructura se control for). 

positivos = 0
negativos = 0
ceros = 0

for i in range(10):
    try:
        numero = float(input(f"Ingrese el número {i + 1}: "))
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        continue

print(" ")
print("Resultados:")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números iguales a cero: {ceros}")
