
# Proyecto Final - Tienda Virtual
# Autor: Fernando Sánchez
# Profesor: Harold Tejada
# Asignatura: Algoritmos Estructurados

# Lista de productos disponibles
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 35000},
    {"id": 2, "nombre": "Mouse", "precio": 500},
    {"id": 3, "nombre": "Teclado", "precio": 1200},
    {"id": 4, "nombre": "Monitor", "precio": 15000},
    {"id": 5, "nombre": "Memoria USB", "precio": 800},
]

# Carrito de compras
carrito = []

# Mostrar productos
def mostrar_productos():
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"ID: {producto['id']} - {producto['nombre']} - RD${producto['precio']}")

# Agregar producto al carrito
def agregar_al_carrito():
    mostrar_productos()
    try:
        id_producto = int(input("\nIngresa el ID del producto que deseas agregar: "))
        producto_encontrado = next((p for p in productos if p["id"] == id_producto), None)
        if producto_encontrado:
            carrito.append(producto_encontrado)
            print(f"{producto_encontrado['nombre']} ha sido agregado al carrito.")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("Entrada no válida. Ingresa un número.")

# Ver contenido del carrito
def ver_carrito():
    if not carrito:
        print("\nEl carrito está vacío.")
        return
    print("\nContenido del carrito:")
    total = 0
    for item in carrito:
        print(f"{item['nombre']} - RD${item['precio']}")
        total += item['precio']
    print(f"Total acumulado: RD${total}")

# Finalizar compra
def finalizar_compra():
    if not carrito:
        print("\nEl carrito está vacío.")
        return
    subtotal = sum(item['precio'] for item in carrito)
    descuento = 0
    if subtotal > 1000:
        descuento = subtotal * 0.10
    total = subtotal - descuento
    print("\nResumen de la compra:")
    print(f"Subtotal: RD${subtotal}")
    print(f"Descuento: RD${descuento}")
    print(f"Total a pagar: RD${total}")
    carrito.clear()

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ TIENDA VIRTUAL ---")
        print("1. Mostrar productos")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            finalizar_compra()
        elif opcion == "5":
            print("Gracias por usar la Tienda Virtual.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
menu()
