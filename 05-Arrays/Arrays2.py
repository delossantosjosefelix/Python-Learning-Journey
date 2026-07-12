# realizar un programa que rellene una lista con los números pares comprendidos entre 1 y 20. 

numbers = []

for i in range(1, 21):
    if i % 2 == 0:
        numbers.append(i)
    
print(" ")
print("Lista de Numeros Pares 1 al 20:", numbers)
print(" ")
