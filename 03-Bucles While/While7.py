#Escriba un programa que simule administrar una cuenta de banco, usando la siguiente nomenclatura para las transacciones: a. D – Débito – Suma  b. C – Crédito – Resta c. El programa finaliza cuando se digite la letra S al capturar la descripción de la actividad a realizar. 

saldo = 0.0

print("Bienvenido al sistema de cuenta bancaria.")
print("Ingrese 'D' para Débito (sumar), 'C' para Crédito (restar), o 'S' para salir.\n")

while True:
    operacion = input("Ingrese el tipo de operación (D/C/S): ").upper()

    if operacion == "S":
        print("\nOperación finalizada.")
        break
    elif operacion == "D":
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            saldo += monto
            print(f"Depósito realizado. Saldo actual: {saldo:.2f}\n")
        except ValueError:
            print("Monto inválido. Intente de nuevo.\n")
    elif operacion == "C":
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            saldo -= monto
            print(f"Retiro realizado. Saldo actual: {saldo:.2f}\n")
        except ValueError:
            print("Monto inválido. Intente de nuevo.\n")
    else:
        print("Opción no válida. Intente con D, C o S.\n")

print(f"Saldo final en la cuenta: {saldo:.2f}")
