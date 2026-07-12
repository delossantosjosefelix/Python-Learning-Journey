# Realizar un algoritmo que muestre los impares que hay entre 1 y un valor introducido por el teclado. 

number = int(input("Ingrese el numero: ")) 
print(" ")

for i in range(1, number + 1):
    if i % 2 != 0:
        print(i)
        print(" ")