#Realizar un programa que permita identificar si un numero es par o impar. 

while True:
    number= int(input("Ingrese un Numero Entero: "))
    print(" ")

    if number >= 0:
        break
    else:
        print("Ingrese un Numero Positivo Porfavor")
        print(" ")

if number % 2 == 0:
    print(" ")
    print("El Numero es Par")
else:
    print(" ")
    print("El Numero es Impar")

        