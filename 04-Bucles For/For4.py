#4- Un algoritmo que permita ingresar N datos correspondientes al género de N, número de personas y determine el porcentaje de hombres y mujeres que hay. 

N = int(input("¿Cuántas personas vas a ingresar? "))

h = 0
m = 0

for i in range(1, N + 1):
    genero = input(f"Introduce el género de la persona {i} (M para mujer, H para hombre): ") 
    if genero == "H":
        h += 1
    elif genero == "M":
        m += 1

ph = (h/N) * 100
pm = (m/N) * 100 

print(f"El Porcentaje de Hombres es: {ph}%")
print(f"El Porcentaje de Mujeres es: {pm}%")



    
    