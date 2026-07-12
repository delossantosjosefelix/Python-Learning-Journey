#  Realiza un programa dado la opción elegida en un menú calcule (1) velocidad promedio de un vehículo; (2) la distancia recorrida; (3) Tiempo y (4) aceleración promedio. Se entiende que los datos introducidos están en las medidas de metros y segundos.  

print("Menú de opciones:")
print("1. Calcular velocidad promedio (v = d / t)")
print("2. Calcular distancia recorrida (d = v * t)")
print("3. Calcular tiempo (t = d / v)")
print("4. Calcular aceleración promedio (a = (vf - vi) / t)")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    distancia = float(input("Ingrese la distancia (en metros): "))
    tiempo = float(input("Ingrese el tiempo (en segundos): "))
    if tiempo != 0:
        velocidad = distancia / tiempo
        print("La velocidad promedio es:", velocidad, "m/s")
    else:
        print("El tiempo no puede ser cero.")

elif opcion == 2:
    velocidad = float(input("Ingrese la velocidad (en m/s): "))
    tiempo = float(input("Ingrese el tiempo (en segundos): "))
    distancia = velocidad * tiempo
    print("La distancia recorrida es:", distancia, "metros")

elif opcion == 3:
    distancia = float(input("Ingrese la distancia (en metros): "))
    velocidad = float(input("Ingrese la velocidad (en m/s): "))
    if velocidad != 0:
        tiempo = distancia / velocidad
        print("El tiempo es:", tiempo, "segundos")
    else:
        print("La velocidad no puede ser cero.")

elif opcion == 4:
    vi = float(input("Ingrese la velocidad inicial (en m/s): "))
    vf = float(input("Ingrese la velocidad final (en m/s): "))
    tiempo = float(input("Ingrese el tiempo (en segundos): "))
    if tiempo != 0:
        aceleracion = (vf - vi) / tiempo
        print("La aceleración promedio es:", aceleracion, "m/s²")
    else:
        print("El tiempo no puede ser cero.")

else:
    print("Opción no válida.")
