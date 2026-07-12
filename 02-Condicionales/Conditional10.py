#- Escribir un programa que indique si una persona tiene sobrepeso (observar la imagen de ejemplo como parámetros a utilizar) Los datos deben ser positivos. 

# Diccionario con rangos de peso ideal según altura (en metros)
rangos_peso_ideal = {
    1.50: (43.0, 56.0),
    1.55: (45.0, 59.0),
    1.60: (47.0, 63.0),
    1.65: (49.0, 68.0),
    1.70: (52.0, 72.0),
    1.75: (55.0, 76.0),
    1.80: (58.0, 81.0),
    1.85: (61.0, 86.0),
    1.90: (65.0, 91.0)
}

# Solicitar datos al usuario
altura = float(input("Ingrese su altura en metros (ej. 1.70): "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Verificar que los datos sean positivos
if altura <= 0 or peso <= 0:
    print("❌ Error: La altura y el peso deben ser valores positivos.")
else:
    # Buscar el rango de peso ideal más cercano a la altura ingresada
    alturas_disponibles = sorted(rangos_peso_ideal.keys(), key=lambda x: abs(x - altura))
    altura_mas_cercana = alturas_disponibles[0]
    peso_min, peso_max = rangos_peso_ideal[altura_mas_cercana]

    print(f"\n📏 Altura más cercana en tabla: {altura_mas_cercana} m")
    print(f"🔍 Rango de peso ideal: {peso_min} kg - {peso_max} kg")

    # Evaluar el estado del peso
    if peso < peso_min:
        print("📉 Resultado: Bajo peso.")
    elif peso > peso_max:
        print("📈 Resultado: Sobrepeso.")
    else:
        print("✅ Resultado: Peso ideal.")
