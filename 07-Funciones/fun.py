# trabajando con funciones
def hola(pNombre, pApellido):
 print(f"Hola {pNombre} {pApellido}!!")

def menorEdad(pEdad):
 edad = pEdad
 if edad >= 18:
   print("Eres mayor de edad")
 else:
   print("Eres menor de edad")

def tablaMultiplicar(pValor):
 valor = pValor
 for item in range(1,13):
  print(f"{valor} X {item} = {valor * item}")
  
def menu():
 print(" ")
 print("-----------------------------------------------------")
 print("Lista de Tareas")
 print("1- Saludar")
 print("2- Determinar si eres menor o mayor de edad")
 print("3- Tabla de multiplicar")
 print("4- Salir")
 print("-----------------------------------------------------")
 opcion = int(input("Que Tarea Ejecutar: "))
 print("-----------------------------------------------------")
 print(" ")
 return opcion

while True:
 vOpcion = menu()

 if vOpcion == 1:
   vNombre = input("Ingresa tu nombre: ")
   vApellido = input("Ingresa tu apellido: ")
   hola(vNombre, vApellido)
 elif vOpcion == 2:
   vEdad = int(input("Ingresa tu edad: "))
   menorEdad(vEdad)   
 elif vOpcion == 3:
   vValor = int(input("Ingresa un numero: "))
   tablaMultiplicar(vValor)
 elif vOpcion == 4:
   print("Gracias por participar!!")
   break
 else:
   print("Valor invalido!!!")