#Nomina Semanal

print(" ")
print("Bienvenido a esta Calculdora de Nominas en Python")
print(" ")


horastrabajadas=float(input("Ingrese el Total de Horas Trabajadas en la Semana: "))
print(" ")
tarifa=float(input("Ingrese la Tarifa por Hora: "))
print(" ")
nomina= horastrabajadas * tarifa

print(f"La Nomina Semanal del Empleado es: {nomina}")
