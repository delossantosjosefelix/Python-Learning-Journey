#Edad

print(" ")
print("Bienvenido a esta Calculdora de Edad en Python")
print(" ")

year=(input("Ingrese el Año de Nacimiento: "))
print(" ")

if len(year) == 4:
    year= 2025 - int(year)
    print(f"Su Edad es de {year} años")
    print(" ")
else:
    print("Error: Porfavor Ingrese un Año de 4 Digitos.")
    print(" ")
    