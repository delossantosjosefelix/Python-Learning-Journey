# Ejercicio: Dada una lista de números, calcular por separado la suma de los valores positivos y la suma de los valores negativos.


numbers = [-3, 6, 7, -8, 11, 16, -3]
positivos = 0
negativos = 0

for n in numbers:
    if n >= 0:
        positivos += n
    else:
        negativos += n

print(" ")
print("Lista:", numbers)
print("Suma de positivos:", positivos)
print("Suma de negativos:", negativos)
print(" ")

