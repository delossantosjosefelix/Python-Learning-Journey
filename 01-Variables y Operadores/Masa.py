#Masa

print(" ")
print("Bienvenido a esta Calculdora de Masa Corporal en Python")
print(" ")


peso = float(input("Ingrese su Peso en kilogramos: "))
print(" ")

altura = float(input("Ingrese su Altura en Metros: "))
print(" ")

imc = peso / (altura ** 2)

print(f"Su Índice de Masa Corporal es: {imc}")
