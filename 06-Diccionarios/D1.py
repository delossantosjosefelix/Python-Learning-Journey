#1- Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {'EURO':'€', 'DOLLAR':'$', 'YEN':'¥'}

print(" ")
divisa = input("Introduce una divisa (Euro, Dollar, Yen): ")

divisa = divisa.upper()

if divisa in divisas:
    print(" ")
    print(f"El símbolo de {divisa} es {divisas[divisa]}")
    print(" ")
else:
    print(" ")
    print("La divisa no está en el diccionario.")
    print(" ")
    