# 3- Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. 

frutas = {'PLATANO': '1.35', 'MANZANA': '0.80', 'PERA': '0.85', 'NARANJA': '0.70',}

print(" ")
fruta = input("Introduce una fruta (Platano, Manzana, Pera, Naranja): ")

fruta = fruta.upper()

if fruta in frutas:
    print(" ")
    print(f"El Kilo de {fruta} es {frutas[fruta]}$")
    print(" ")
    compra = input("¿Cuantos Kilos, Desea Comprar?: ")
    print(" ")
    
    try:
        precio_unitario = float(frutas[fruta])
        kilos = float(compra)
        precio = precio_unitario * kilos

        print(f"El precio a pagar por {kilos} kilos de {fruta} es: {precio:.2f}$")
        print(" ")

    except ValueError:
        print("Por favor, introduzca un número válido para los kilos.")


else:
    print(" ")
    print("No Tenemos esa Fruta.")
    print(" ")
    