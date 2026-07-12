#Escribir un programa que lea por teclado 10 números y muestre en pantalla el más grande, el más pequeño y la media de N los números ingresados. 

contador = 0
suma = 0
mayor = None
menor = None

while contador < 10:
    try:
        numero = float(input(f"Ingrese el número {contador + 1}: "))
        suma += numero

        if contador == 0:
            mayor = numero
            menor = numero
        else:
            if numero > mayor:
                mayor = numero
            if numero < menor:
                menor = numero

        contador += 1
    except ValueError:
        print("Por favor, ingrese un número válido.")

media = suma / 10

print(f"Número más grande: {mayor}")
print(f"Número más pequeño: {menor}")
print(f"Media de los números: {media}")
