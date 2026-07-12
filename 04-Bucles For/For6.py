# - Elabora un algoritmo que permita mostrar el sueldo promedio de un grupo de empleados. 

N = int(input("¿Cuántos empleados hay? "))

suma_sueldos = 0

for i in range(1, N + 1):
    sueldo = float(input(f"Introduce el sueldo del empleado {i}: "))
    suma_sueldos += sueldo

promedio = suma_sueldos / N

print(f"El sueldo promedio es: {promedio:.2f}")
