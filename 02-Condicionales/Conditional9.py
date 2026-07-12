#Realice un programa que indique si la suma de dos valores es positiva, negativa o cero.


valor1 = float(input("Ingrese el primer valor: "))
print(" ")
valor2 = float(input("Ingrese el segundo valor: "))
print(" ")

suma = valor1 + valor2


if suma > 0:
    print(f"La suma es {suma}, que es un número positivo.")
elif suma < 0:
    print(f"La suma es {suma}, que es un número negativo.")
else:
    print("La suma es 0.")

