#Escribir un programa que verifica si un dato ingresado por teclado corresponde a la contraseña 123456 y no deje de preguntar por la contraseña hasta que la misma sea la correcta.

password = "123456"
intento = "" 

while intento != password:
    intento=input("Ingrese la Clave: ")
    print(" ")
    if intento == password:
        print("La Clave es Correcta")
        print(" ")
        break
    else:
        print("La Clave es Incorrecta, Porfavor Intente de Nuevo")
        print(" ")
        
    
