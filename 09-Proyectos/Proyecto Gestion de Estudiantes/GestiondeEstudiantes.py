# Proyecto de Gestion de Estudiantes, Algoritmos Estructurados 2025

print(" ")
print("Bienvenidos a 'EduGestor', un Programa Dedicado a la Gestion de Estudiantes")
print(" ")

estudiantes = []

def mostrar_menu():
    print("\n" + "-" * 40)
    print("Bienvenido/a a 'EduGestor'")
    print("-" * 40)
    print("1. Registrar Estudiantes")
    print("2. Ver Estudiantes Registrados")
    print("3. Salir")
    print("-" * 40)

def registrar_estudiantes():
    while True:
        try:
            print(" ")
            matricula = int(input("Ingrese la Matrícula del Estudiante (Solo Números): "))
            print(" ")
            break
        except ValueError:
            print(" ")
            print("Error: La Matrícula Debe ser un Número Entero. Intente de nuevo.")
            print(" ")

    nombre = input("Ingrese el Nombre del Estudiante: ")
    print(" ")
    apellido= input("Ingrese el Apellido del Estudiante: ")
    print(" ")
    
    estudiante = {
        "matricula": matricula,
        "nombre": nombre,
        "apellido": apellido
    }
    estudiantes.append(estudiante)
    
    print(" ")
    print(f"Estudiante {nombre} {apellido} registrado con éxito.")
    print(" ")
    
while True:
    registrar_estudiantes()
    
    continuar = input("¿Desea registrar otro estudiante? (s/n): ").lower()
    print(" ")
    if continuar != 's':
        break

def  mostrar_estudiantes()
    if not estudiantes:
        print(" ")
        print("No hay estudiantes registrados aún.")
        print(" ")
    else:
        print(" ")
        print("Lista de Estudiantes Registrados:")
        print(" ")
        
        for estudiante in estudiantes:
            print(f"Matrícula: {estudiante['matricula']} | Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        print(" ")

def ejecutar_proyecto():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_estudiantes()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            print(" ")
            print("Gracias por visitar la iShop. ¡Hasta la próxima!")
            print("\n                Desarrolladores \n")
            print(" Rowin Alejandro Jimenez Castillo         2020-1010")
            print(" Fernando Sanchez a Cruz                  2024-0777")
            print(" Jose Felix De Los Santos                 2024-1135")
            print(" Carlos David Rosario Taveras             2024-0903")
            print("\n                   Año: 2025")
            print(" ")
            break
        else:
            print("Opción no válida.")

ejecutar_proyecto()