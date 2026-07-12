# Ejercicio: Generar los primeros 40 números pares, calcular su suma y promedio, y guardar esos resultados en una segunda lista.



numbers = []
numbers2 = []
contador = 0
numero = 2  

while contador < 40:
    numbers.append(numero)
    numero += 2
    contador += 1

print(" ")
print("Lista de los 40 primeros números pares:")
print(numbers)
print(" ")

suma = 0
for n in numbers:
    suma += n

promedio = suma / len(numbers)

numbers2.append(suma)
numbers2.append(promedio)

print("Suma de los números pares:", suma)
print("Promedio de los números pares:", promedio)
print(" ")
print("Lista numbers2 con suma y promedio:", numbers2)
print(" ")
