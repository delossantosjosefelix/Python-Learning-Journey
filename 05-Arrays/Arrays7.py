# Ejercicio: Leer 10 números ingresados por el usuario y calcular su suma y promedio.


numbers = []
suma = 0
contador = 0

while contador < 10:
    num = int(input("Ingrese un número: "))
    numbers.append(num)
    suma += num
    contador += 1

promedio = suma / len(numbers)

print(" ")
print("Números ingresados:", numbers)
print("Suma:", suma)
print("Promedio:", promedio)
print(" ")

