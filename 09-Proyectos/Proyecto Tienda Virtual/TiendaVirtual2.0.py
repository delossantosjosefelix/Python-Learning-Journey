# Proyecto - Tienda Virtual iShop (Version 2.0): sistema con menu para ver productos, agregar al carrito, ver el carrito y finalizar la compra aplicando descuento.


productos = [
    {"id": 1, "nombre": "iPhone 15 📱", "precio": 70000},
    {"id": 2, "nombre": "MacBook Air M2 💻", "precio": 120000},
    {"id": 3, "nombre": "iPad Pro 📱", "precio": 90000},
    {"id": 4, "nombre": "AirPods Pro 🎧", "precio": 15000}
]

carrito = []

def mostrar_menu():
    print("\n" + "-" * 40)
    print("🛍️  Bienvenido/a a la iShop")
    print("-" * 40)
    print("1. Ver productos disponibles")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito")
    print("4. Finalizar compra")
    print("5. Salir")
    print("-" * 40)
    
def mostrar_productos():
    while True:
        print("\n📦 Productos disponibles:")
        print("-" * 40)
        for producto in productos:
            print(f"{producto['id']}. {producto['nombre']} - RD${producto['precio']}")
        
        salir = input("¿Desea salir y volver al menú principal? (s/n): ").strip().lower()
        if salir == "s":
            print(" ")
            print("🔙 Volviendo al menú principal.")
            print(" ")
            break
        elif salir != "n":
            print(" ")
            print("❗ Opción no válida. Intente de nuevo.")
            print(" ")
            
def agregar_al_carrito():
    continuar = True
    while continuar:
        print("\n📦 Productos disponibles:")
        print("-" * 40)
        for producto in productos:
            print(f"{producto['id']}. {producto['nombre']} - RD${producto['precio']}")

        opcion = input("Ingrese el ID del producto que desea agregar: ")
        try:
            producto_id = int(opcion)
            producto = next((p for p in productos if p["id"] == producto_id), None)
            if producto:
                carrito.append(producto)
                print(" ")
                print(f"✅ {producto['nombre']} fue agregado al carrito.")
                print(" ")
                
            else:
                print(" ")
                print("❌ Producto no encontrado.")
                print(" ")
        except ValueError:
            print(" ")
            print("❗ Entrada inválida.")
            print(" ")
        
        respuesta = input("¿Desea agregar otro producto al carrito? (s/n): ").strip().lower()
        if respuesta != "s":
            print(" ")
            print("🔙 Volviendo al menú principal.")
            print(" ")
            continuar = False
            
def ver_carrito():
    while True:
        if not carrito:
            print(" ")
            print("🛒 El carrito está vacío.")
            print(" ")
        else:
            total = 0
            print("\n🧺 Contenido del carrito:")
            print("-" * 40)
            for i, item in enumerate(carrito, 1):
                print(f"{i}. {item['nombre']} - RD${item['precio']}")
                total += item['precio']
            print(f"💰 Total acumulado: RD${total}")
        
        salir = input("¿Desea salir del carrito y volver al menú principal? (s/n): ").strip().lower()
        if salir == "s":
            print(" ")
            print("🔙 Volviendo al menú principal.")
            print(" ")
            break
        elif salir != "n":
            print(" ")
            print("❗ Opción no válida. Intente de nuevo.")
            print(" ")
            
def finalizar_compra():
    if not carrito:
        print(" ")
        print("🛒 El carrito está vacío.")
        print(" ")
        return

    subtotal = sum(item['precio'] for item in carrito)
    descuento = subtotal * 0.10 if subtotal > 1000 else 0
    total = subtotal - descuento

    print("\n🧾 Resumen de compra:")
    print(f"Subtotal: RD${subtotal:.2f}")
    print(f"Descuento: RD${descuento:.2f}")
    print(f"Total a pagar: RD${total:.2f}")
    print("🎉 ¡Gracias por su compra!")
    print(" ")
    
    carrito.clear()
    
def ejecutar_tienda():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            finalizar_compra()
        elif opcion == "5":
            print(" ")
            print("👋 Gracias por visitar la iShop. ¡Hasta la próxima!")
            print("\n                💻 Desarrolladores\n")
            print(" Rowin Alejandro Jimenez Castillo        🆔 2020-1010")
            print(" Fernando Sanchez a Cruz                 🆔 2024-0777")
            print(" Jose Felix De Los Santos                🆔 2024-1135")
            print(" Carlos David Rosario Taveras            🆔 2024-0903")
            print("\n                     📅 Año: 2025")
            print(" ")
            break
        else:
            print("❌ Opción no válida.")

ejecutar_tienda()