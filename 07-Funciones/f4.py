# Ejercicio: Función que convierte una temperatura de grados Celsius a Fahrenheit.


def celsius_a_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit}°F")
