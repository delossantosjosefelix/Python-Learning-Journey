# Realizar un programa que rellene una lista con 10 números enteros consecutivos y haga una copia de ese array en otro. 

b=1
numbers = []
numbers2 = []

print(" ")
a= int(input("Ingrese un Numero Entero: "))
numbers.append(a)

while b <= 10:
    a += 1 
    numbers.append(a)
    b += 1
    
print(" ")
print("Lista de Numeros Consecutivos 1:", numbers)
print(" ")

numbers2.extend(numbers)

print(" ")
print("Lista de Numeros Consecutivos 2:", numbers2)
print(" ")

