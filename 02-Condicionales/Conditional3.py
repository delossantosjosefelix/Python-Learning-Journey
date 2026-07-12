#Realizar un programa que determine tu categoría de edad donde menor de 18 eres menor de edad; mayor o igual que 18 y menor o igual que 65 eres adulto y mayor de 65 eres adulto mayor.

age= int(input("Ingrese su Edad: "))
if age <18 and age >0:
    print(" ")
    print("Eres Menor de Edad")
elif age >= 18 and age <= 65:
    print(" ")
    print("Eres Mayor de Edad")
elif age <= 0:
    print(" ")
    print("Esa Edad no es Valida")
elif age > 65 and age <= 120:
    print(" ")
    print("Eres un Anciano")
elif age >= 121:
    print(" ")
    print("Firmo con los Yankees")
    
    