#Realiza un algoritmo que permita identificar si un año es bisiesto.


year=int(input("Ingrese el Año que Desea Verificar: "))
print(" ")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(f"El año {year} es Bisiesto")
        else:
            print(f"El año {year}  No es Bisiesto")
    else:
        print(f"El año {year} es Bisiesto")
else:
    print(f"El año {year}  No es Bisiesto")



