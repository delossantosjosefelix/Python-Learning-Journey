# Ejercicio 2 - Parcial 1: Leer 10 números ingresados por el usuario y contar cuántos son mayores, menores o iguales a cero.


greater = 0
less = 0
same = 0

for i in range(10):
    try:
        number=int(input(f"Ingrese el numero {i + 1}: "))
        print(" ")
        if number > 0:
            greater += 1
        elif number < 0:
            less += 1
        else:
            same += 1
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        continue

print(" ")
print("Resultados:")
print(f"Números Mayores que Cero: {greater}")
print(f"Números Menores que Cero: {less}")
print(f"Números iguales a cero: {same}")