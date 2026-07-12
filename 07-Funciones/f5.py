# Ejercicio: Función que genera una contraseña de la longitud indicada por el usuario, combinando letras mayúsculas, minúsculas, números y caracteres especiales.


def generarcontraseña(longitud):
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    todos = mayusculas + minusculas + numeros + especiales

    contraseña = ""
    for i in range(longitud):
        indice = (i * 7 + 3) % len(todos)  
        contraseña += todos[indice]

    return contraseña

longitud = int(input("Ingresa la longitud deseada para la contraseña: "))
print("Contraseña generada:", generarcontraseña(longitud))

