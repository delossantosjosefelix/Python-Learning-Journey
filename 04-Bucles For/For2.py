# Leer la edad de 20 personas, determinando cuántas de las edades están en el intervalo de 18 a 90.

personas = 0

for i in range(1, 21):
    edad = int(input(f"Introduce la edad de la persona {i}: "))
    print(" ")
    if 18 <= edad <=90:
        personas +=1
        
print(f"Cantidad de Personas entre 18 y 19 años: {personas}")

 