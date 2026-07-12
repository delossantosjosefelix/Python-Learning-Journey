#Promedio de 4 Calificaiones

print(" ")
print("Bienvenido a esta Calculdor de Promedio en Python")
print(" ")

print("Porfavor Ingrese las 4 Calificaciones")
print(" ")
while True:
    numero1= float(input("Ingrese Su Primera Calificacion: "))
    print(" ")
    if numero1 >= 0 and numero1 <= 100:
        break
    else:
        print("Esa Calificacion no es Valida, Porfavor Ingrese otra")
        print(" ")
while True:
    numero2= float(input("Ingrese Su Segunda Calificacion: "))
    print(" ")
    if numero2 >= 0 and numero2 <= 100:
        break
    else:
        print("Esa Calificacion no es Valida, Porfavor Ingrese otra")
        print(" ")
while True:
    numero3= float(input("Ingrese Su Tercera Calificacion: "))
    print(" ")
    if numero3 >= 0 and numero3 <= 100:
        break
    else:
        print("Esa Calificacion no es Valida, Porfavor Ingrese otra")
        print(" ")
while True:
    numero4= float(input("Ingrese Su Primera Calificacion: "))
    print(" ")
    if numero4 >= 0 and numero4 <= 100:
        break
    else:
        print("Esa Calificacion no es Valida, Porfavor Ingrese otra")
        print(" ")
    
print("Las 4 Calificaciones, Fueron Ingresadas Exitosamente")
promedio= (numero1 + numero2 + numero3 + numero4) / 4
print(" ")
print(f"El promedio de las 4 calificaciones es: {promedio}")
print(" ")
        