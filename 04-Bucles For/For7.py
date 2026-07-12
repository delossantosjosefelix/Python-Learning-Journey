# Elabora un algoritmo que solicite la edad de 20 personas y que muestre cuantos son mayores y menores de edad. 

mayores = 0
menores = 0

for i in range(1, 21):
    edad = int(input(f"Introduce la edad de la persona {i}: "))
    print(" ")
    if edad <18:
        menores +=1
    else:
        mayores +=1
        
print(f"La Cantidad de Mayores de Edad es de: {mayores}")
print(" ")
print(f"La Cantidad de Menores de Edad es de: {menores}")
