# Ejercicio: Simular una cesta de la compra donde se ingresan artículos y precios hasta escribir 'fin', y luego mostrar un resumen con el total a pagar.


cesta = {}

print(" ")
print("Bienvenido a la cesta de la compra.")
print(" ")
print("Introduce los artículos y sus precios. Escribe 'fin' para terminar.\n")
print(" ")

while True:
    print(" ")
    articulo = input("Artículo: ")
    print(" ")
    if articulo.lower() == 'fin':
        break

    precio = input("Precio: ")
    print(" ")
    try:
        precio = float(precio)
        cesta[articulo] = precio
    except ValueError:
        print(" ")
        print("Por favor, introduce un precio válido (número).")
        print(" ")

print("\nLista de la compra")
print(" ")
print("{:<20} {:>10}".format("Artículo", "Precio"))
print("-" * 30)


total = 0
for articulo, precio in cesta.items():
    print("{:<20} {:>10.2f}$".format(articulo, precio))
    total += precio

print("-" * 30)
print("{:<20} {:>10.2f}$".format("Total", total))
