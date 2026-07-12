# Realizar un programa que permita tomar la decisión de concesión de préstamos, tomando en cuenta las siguientes políticas el ingreso mensual debe ser mayor de 1000 y el monto solicitado debe ser menor o igual que el ingreso mensual por 5 

Ingreso=int(input("Ingrese su Ingreso Mensual: "))
print(" ")

Monto=int(input("Ingrese el Prestamo Deseado: "))
print(" ")

if Ingreso >1000:
    print("Su Ingreso Mensual Califica, para el Prestamo.")
    print(" ")
    
    if Monto <= Ingreso*5:
        print("Su Prestamo fue Aprovado Exitosamente.")
        print(" ")
    else:
        print("Lo Sentimos, pero No Califica para el Prestamo.")
        print(" ")
    
else:
    print("lo Sentimos, Su Ingreso Mensual no Califica.")
    print(" ")
