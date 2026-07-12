# Ejercicio: Función que calcula el factorial de un número entero no negativo ingresado por el usuario.


def calcularfactorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

numero = int(input("Ingresa un número entero no negativo: "))
resultado = calcularfactorial(numero)
print(f"El factorial de {numero} es: {resultado}")
