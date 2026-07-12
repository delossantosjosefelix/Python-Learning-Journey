#Calculadora en Python

print(" ")
print("Bienvenido a esta Calculdora en Python")
print(" ")

#1. Hacer que el Usuario Escoja la Operacion que desea Realizar

print("Escoja la Operacion que Desea Realizar")
print(" ")
print("Presione 1, para Suma")
print("Presione 2, para Resta")
print("Presione 3, para Multiplicacion")
print("Presione 4, para Division")
print(" ")

while True:
    Operacion=int(input("Digite la Opcion Que Desea Escoger: "))
    print(" ")
    if Operacion > 0 and Operacion <= 4:
        break
    else:
        print("Esa Opcion No es Valida, Porfavor Ingrese otra Opcion: ")
        print(" ")

#2. Pedir los Numeros y Decirle al Usuario La Opcion que Ha Elijido

if Operacion == 1:
    print("Has Elejido Sumar")
    print(" ")
    a = float(input("Ingrese el Primer Numero: "))
    print(" ")
    b = float(input("Ingrese el Segundo Numero:"))
    print(" ")
elif Operacion == 2:
    print("Has Elejido Restar")
    print(" ")
    a = float(input("Ingrese el Primer Numero: "))
    print(" ")
    b = float(input("Ingrese el Segundo Numero:"))
    print(" ")
elif Operacion == 3:
    print("Has Elejido Multiplicar")
    print(" ")
    a = float(input("Ingrese el Primer Numero: "))
    print(" ")
    b = float(input("Ingrese el Segundo Numero:"))
    print(" ")
elif Operacion == 4:
    print("Has Elejido Dividir")
    print(" ")
    a = float(input("Ingrese el Primer Numero: "))
    print(" ")
    b = float(input("Ingrese el Segundo Numero:"))
    print(" ")

#3. Realizar la Opcion Elejida por el Usuario

if Operacion == 1:
    Resultado= a + b
    print(f"La Suma de los Numeros es: {a} + {b} = {Resultado}")
elif Operacion == 2:
    Resultado= a - b
    print(f"La Resta de los Numeros es: {a} - {b} = {Resultado}")
elif Operacion == 3:
    Resultado= a * b
    print(f"La Multipliacion de los Numeros es: {a} x {b} = {Resultado}")
elif Operacion == 4:
    if b != 0:
        Resultado= a / b
        print(f"La Division de los Numeros es: {a} / {b} = {Resultado}")
    else:
        print("No se Puede Dividir entre 0")

exit()
    
    




        
    





