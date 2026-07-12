#Realizar un programa que indique cuál es el mayor de cuatro números enteros ingresados por el teclado. 

Num1=int(input("Ingrese el Primer Numero: "))
print(" ")

Num2=int(input("Ingrese el Segundo Numero: "))
print(" ")

Num3=int(input("Ingrese el Tercer Numero: "))
print(" ")

Num4=int(input("Ingrese el Cuarto Numero: "))
print(" ")

if Num1 > Num2 and Num1 > Num3 and Num1 > Num4:
    print(f"El Primer Numero ({Num1}) es el Mayor.")
    print(" ")
elif  Num2 > Num1 and Num2 > Num3 and Num2 > Num4:
    print(f"El Segundo Numero ({Num2}) es el Mayor.")
    print(" ")
elif  Num3 > Num1 and Num3 > Num2 and Num3 > Num4:
    print(f"El Tercer Numero ({Num3}) es el Mayor.")
    print(" ")
elif  Num4 > Num1 and Num4 > Num2 and Num4 > Num3:
    print(f"El Cuarto Numero ({Num4}) es el Mayor.")
    print(" ")
