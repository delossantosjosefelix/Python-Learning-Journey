# Ejercicio: Leer 10 números ingresados por el usuario y determinar el valor máximo y el mínimo, junto con su posición en la lista.


numbers = []
contador = 0

while contador < 10:
    num = int(input("Ingrese un número: "))
    numbers.append(num)
    contador += 1

maximo = max(numbers)
minimo = min(numbers)

pos_max = numbers.index(maximo)
pos_min = numbers.index(minimo)

print(" ")
print("Lista:", numbers)
print("Máximo:", maximo, "en posición", pos_max)
print("Mínimo:", minimo, "en posición", pos_min)
print(" ")
