#Proyecto Algoritmos Estructurados P2 2025

biblioteca = {}  
prestados = {}   
miembros = {}

class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"[{self.id_libro}] '{self.titulo}' por {self.autor}"

class Prestamo:
    def __init__(self, libro, miembro_id):
        self.libro = libro
        self.miembro_id = miembro_id
    
    def __str__(self):
        nombre = miembros.get(self.miembro_id, 'Desconocido')
        return f"[{self.libro.id_libro}] '{self.libro.titulo}' prestado a {nombre} (ID: {self.miembro_id})"

#Agregaar Un Miembro
def agregar_miembro():
    print("\n" + "-" * 40)
    print("AGREGAR NUEVO MIEMBRO")
    print("-" * 40)
    print(" ")
    id_miembro = input("Ingrese el ID del miembro: ").strip()
    print(" ")
    if id_miembro in miembros:
        print("Error: Ya existe un miembro con ese ID.")
        print(" ")
        return
    nombre = input("Ingrese el nombre del miembro: ").strip()
    print(" ")
    if nombre:
        miembros[id_miembro] = nombre
        print("-" * 40)
        print(f"✓ Miembro '{nombre}' agregado exitosamente.")
        print(" ")
    else:
        print("Error: El nombre no puede estar vacío.")
        print(" ")

#Mostrar Miembros
def mostrar_miembros():
    print("\n" + "-" * 40)
    print("LISTA DE MIEMBROS")
    print("-" * 40)
    print(" ")
    if miembros:
        for id_miembro, nombre in miembros.items():
            print(f"[{id_miembro}] {nombre}")
            print(" ")
        print("-" * 40)
    else:
        print("No hay miembros registrados.")
        print(" ")

#Agregar Libro
def agregar_libro():
    print("\n" + "-" * 40)
    print("AGREGAR LIBRO A LA BIBLIOTECA")
    print("-" * 40)
    print(" ")
    id_libro = input("Ingrese el ID del libro: ").strip()
    print(" ")
    if id_libro in biblioteca:
        print("Error: Ya existe un libro con ese ID.")
        return
    titulo = input("Ingrese el título del libro: ").strip()
    print(" ")
    autor = input("Ingrese el autor del libro: ").strip()
    print(" ")
    
    if titulo and autor:
        nuevo_libro = Libro(id_libro, titulo, autor)
        biblioteca[id_libro] = nuevo_libro
        print("-" * 40)
        print(f"✓ Libro '{titulo}' agregado exitosamente.")
        print(" ")
    else:
        print("Error: Título y autor no pueden estar vacíos.")

#Mostrar Libros
def mostrar_libros():
    print("\n" + "-" * 40)
    print("LISTA DE LIBROS EN LA BIBLIOTECA")
    print("-" * 40)
    print(" ")
    if biblioteca:
        for libro in biblioteca.values():
            print(libro)
            print(" ")
        print("-" * 40)
    else:
        print("No hay libros disponibles en la biblioteca.")
        print(" ")

#Prestar Libros
def prestar_libro():
    if not biblioteca:
        print("No hay libros disponibles en la biblioteca.")
        print(" ")
        return
    if not miembros:
        print("No hay miembros registrados. Agregue uno primero.")
        print(" ")
        return

#Libros Disponibles
    print("\n" + "-" * 40)
    print("LIBROS DISPONIBLES")
    print("-" * 40)
    print(" ")
    for libro in biblioteca.values():
        print(libro)
        print(" ")
    print("-" * 40)
    print(" ")
    id_libro = input("Ingrese el ID del libro a prestar: ").strip()
    print(" ")
    if id_libro not in biblioteca:
        print("Error: ID de libro no encontrado.")
        print(" ")
        return

#Miembros Registrados
    print("\n" + "-" * 40)
    print("MIEMBROS REGISTRADOS")
    print("-" * 40)
    print(" ")
    for id_miembro, nombre in miembros.items():
        print(f"[{id_miembro}] {nombre}")
        print(" ")
    print("-" * 40)
    print(" ")

    id_miembro = input("Ingrese el ID del miembro: ").strip()
    print(" ")
    if id_miembro not in miembros:
        print("Error: Miembro no encontrado.")
        print(" ")
        return

    libro_seleccionado = biblioteca[id_libro]
    nuevo_prestamo = Prestamo(libro_seleccionado, id_miembro)
    prestados[id_libro] = nuevo_prestamo
    del biblioteca[id_libro]
    print("-" * 40)
    print(f"✓ Libro '{libro_seleccionado.titulo}' prestado exitosamente a {miembros[id_miembro]}")

#Devolver libros
def devolver_libro():
    if not prestados:
        print("No hay libros prestados actualmente.")
        print(" ")
        return

#Libros Prestados
    print("\n" + "-" * 40)
    print("LIBROS PRESTADOS")
    print("-" * 40)
    print(" ")
    for prestamo in prestados.values():
        print(prestamo)
        print(" ")
        
    print("-" * 40)
    print(" ")
    
    id_libro = input("Ingrese el ID del libro a devolver: ").strip()
    print(" ")
    
    if id_libro in prestados:
        libro = prestados[id_libro].libro
        biblioteca[id_libro] = libro
        del prestados[id_libro]
        print("-" * 40)
        print(f"✓ Libro '{libro.titulo}' devuelto exitosamente.")
        print(" ")
    else:
        print("Error: No hay un préstamo con ese ID.")
        print(" ")

#Mostrar Libros Prestados
def mostrar_libros_prestados():
    print("\n" + "-" * 40)
    print("LISTA DE LIBROS PRESTADOS")
    print("-" * 40)
    if prestados:
        for prestamo in prestados.values():
            print(prestamo)
            print(" ")
    else:
        print("No hay libros prestados actualmente.")
        print(" ")

import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

#Menu 
while True:
    limpiar_pantalla()
    print("╔════════════════════════════════════════════════════════╗")
    print("║             SISTEMA DE GESTIÓN DE BIBLIOTECA           ║")
    print("╠════════════════════════════════════════════════════════╣")
    print("║              Selecciona una opción del menú            ║")
    print("╟────────────────────────────────────────────────────────╢")
    print("║  1. Agregar un libro a la biblioteca                   ║")
    print("║  2. Mostrar la lista de libros                         ║")
    print("║  3. Prestar un libro a un miembro                      ║")
    print("║  4. Devolver un libro prestado                         ║")
    print("║  5. Mostrar la lista de libros prestados               ║")
    print("║  6. Agregar un nuevo miembro                           ║")
    print("║  7. Mostrar lista de miembros                          ║")
    print("║  8. Salir del programa                                 ║")
    print("╚════════════════════════════════════════════════════════╝")
    
    print(" ")
    opcion = input("Ingresa una opción (1-8): ").strip()
    print(" ")
    
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        mostrar_libros()
    elif opcion == "3":
        prestar_libro()
    elif opcion == "4":
        devolver_libro()
    elif opcion == "5":
        mostrar_libros_prestados()
    elif opcion == "6":
        agregar_miembro()
    elif opcion == "7":
        mostrar_miembros()
    elif opcion == "8":
        print(" ")
        print("¡Gracias por Usar el Sistema de Biblioteca!")
        print("\n" + "-" * 51)
        print("DESAROLLADORES 2025")
        print("-" * 51)
        print("Rowin Alejandro Jimenez Castillo         2020-1010")
        print("Fernando Sanchez Cruz                  2024-0777")
        print("Jose Felix De Los Santos                 2024-1135")
        print("Carlos David Rosario Taveras             2024-0903")
        print("-" * 51)
        print(" ")
        break
    else:
        print(" ")
        print("Opción no válida. Intenta de nuevo.")
        print(" ")
    
    print(" ")
    input("Presiona ENTER para continuar...")
    print(" ")

