# Ejercicio 1 - Parcial 1: Calcular la calificación final de un estudiante a partir de las notas de clases, tareas, proyecto final y examen final, aplicando sus respectivos porcentajes.


print("Bienvenido a Esta Calculadora de Notas en Python :)")
print(" ")

clases = 0
homework = 0
pfinal = 0
efinal = 0

while True:
    clases = float(input("Ingrese la nota de Clases: "))
    print(" ")
    if clases > 0 and clases <= 100:
        break
    else:
        print("Esa Nota No es Válida, Por favor Ingrese otra.")
        print(" ")

while True:
    homework = float(input("Ingrese la nota de las Tareas: "))
    print(" ")
    if homework > 0 and homework <= 100:
        break
    else:
        print("Esa Nota No es Válida, Por favor Ingrese otra.")
        print(" ")

while True:
    pfinal = float(input("Ingrese la nota del Proyecto Final: "))
    print(" ")
    if pfinal > 0 and pfinal <= 100:
        break
    else:
        print("Esa Nota No es Válida, Por favor Ingrese otra.")
        print(" ")

while True:
    efinal = float(input("Ingrese la nota del Examen Final: "))
    print(" ")
    if efinal > 0 and efinal <= 100:
        break
    else:
        print("Esa Nota No es Válida, Por favor Ingrese otra.")
        print(" ")

nota_final = (0.35 * clases) + (0.25 * homework) + (0.20 * pfinal) + (0.20 * efinal)
print(" ")
print(f"Tu calificación final es: {nota_final:.2f}")
