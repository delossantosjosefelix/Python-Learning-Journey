# Ejercicio: Calculadora con menú de opciones (suma, resta, multiplicación y división) implementada usando funciones.

def Suma(a, b):
    print(f"{a} + {b} = {a + b}")

def Resta(a, b):
    print(f"{a} - {b} = {a - b}")

def Multiplicacion(a, b):
    print(f"{a} x {b} = {a * b}")

def Division(a, b):
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("¡Error! No se puede dividir entre cero.")

def menu():
    print("\n-----------------------------------------------------")
    print("Lista de Operaciones")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")
    print("5- Salir")
    print("-----------------------------------------------------")
    try:
        opcion = int(input("¿Qué operación desea ejecutar?: "))
    except ValueError:
        opcion = 0  # Valor inválido
    print("-----------------------------------------------------\n")
    return opcion

while True:
    vOpcion = menu()

    if vOpcion in [1, 2, 3, 4]:
        try:
            a = float(input("Ingresa el primer valor: "))
            b = float(input("Ingresa el segundo valor: "))
        except ValueError:
            print("¡Error! Debes ingresar números válidos.")
            continue

        if vOpcion == 1:
            Suma(a, b)
        elif vOpcion == 2:
            Resta(a, b)
        elif vOpcion == 3:
            Multiplicacion(a, b)
        elif vOpcion == 4:
            Division(a, b)

    elif vOpcion == 5:
        print("Gracias por participar!!")
        break

    else:
        print("¡Valor inválido!")
