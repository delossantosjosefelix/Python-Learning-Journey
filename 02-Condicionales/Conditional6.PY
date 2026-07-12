#Realiza un programa que permita clasificar triángulos dependiendo la medida de sus lados. Los triángulos que clasificar son: El triángulo es equilátero; El triángulo es isósceles; El triángulo es escaleno.

lado1 = float(input("Ingresa el primer lado del triángulo: "))
lado2 = float(input("Ingresa el segundo lado del triángulo: "))
lado3 = float(input("Ingresa el tercer lado del triángulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero (todos los lados son iguales).")
        print(" ")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles (dos lados son iguales).")
        print(" ")
    else:
        print("El triángulo es escaleno (todos los lados son diferentes).")
        print(" ")
else:
    print("Las medidas no forman un triángulo válido.")
    print(" ")
