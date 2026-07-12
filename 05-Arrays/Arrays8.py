# Ejercicio: Leer 6 números ingresados por el usuario y determinar el valor máximo y su posición en la lista.


numbers = []
contador = 0

while contador < 6:
    num = int(input("Ingrese un número: "))
    numbers.append(num)
    contador += 1

maximo = max(numbers)
posicion = numbers.index(maximo)

print(" ")
print("Números ingresados:", numbers)
print("Máximo valor:", maximo)
print("Posición del máximo valor:", posicion)
print(" ")
