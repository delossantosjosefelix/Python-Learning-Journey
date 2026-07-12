#Examen 

print(" ")
print("Bienvenido a esta Calculdora de Resultados en Python")
print(" ")


        
while True:
    correctas=float(input("Ingrese la Cantidad de Respuestas Correctas: "))
    print(" ")
    if correctas >= 0 and correctas <= 10:
        break
    else:
        print("El Valor Ingresado No es Valido")
        print(" ")    
            
while True:
    incorrectas=float(input("Ingrese la Cantidad de Respuestas Incorrectas: "))
    print(" ")
    if incorrectas >= 0 and incorrectas <= 10:
        break
    else:
        print("El Valor Ingresado No es Valido")
        print(" ")

if correctas + incorrectas > 10:
    print("Error: El Total del Resultado no Puede ser Mayor a 10.")

else:
    resultado= correctas * 10
    print(f"El Resultado del Examen es: {resultado}%")
