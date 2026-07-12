#Realizar un programa que simule una calculadora de descuentos donde si el monto comprado es mayor de 1000 aplique un 10% de descuento, de lo contrario se cobra el monto original.


monto = float(input("Ingresa el monto de tu compra: "))

if monto > 1000:
    descuento = monto * 0.10
    total = monto - descuento
    print(f"¡Tienes un 10% de descuento! Total a pagar: ${total:.2f}")
    print(" ")
else:
    print(f"No se aplica descuento. Total a pagar: ${monto:.2f}")
    print(" ")

