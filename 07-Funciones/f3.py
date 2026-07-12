# Ejercicio: Función que cuenta cuántas veces aparece una letra específica dentro de un texto ingresado por el usuario.


def contarletras(cadena, letra):
    cadena = cadena.lower()
    letra = letra.lower()
    return cadena.count(letra)

texto = input("Ingresa una cadena de texto: ")
letra = input("Ingresa la letra que deseas contar: ")

if len(letra) != 1:
    print("Por favor, ingresa solo una letra.")
else:
    cantidad = contarletras(texto, letra)
    print(f"La letra '{letra}' aparece {cantidad} veces en la cadena.")
