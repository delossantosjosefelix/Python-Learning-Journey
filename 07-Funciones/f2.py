# Ejercicio: Función que determina si una palabra o frase ingresada es un palíndromo.


def espalindromo(cadena):
    cadena = cadena.lower().replace(" ", "")

    return cadena == cadena[::-1]

texto = input("Ingresa una palabra o frase: ")
if espalindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
