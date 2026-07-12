# Realizar un algoritmo que solicite un número y luego genere su tabla de multiplicar desde el 1 hasta el 10. 

number = int(input("Ingrese el Numero que Desea Multiplicar: "))
print(" ")

for i in range(1,11):
    multiplicacion= number * i
    print(f"{number} x {i} = {multiplicacion}")
    print(" ")
    