#Realizar un programa que rellene una lista de 20 elementos con los números comprendidos entre 20 y 39 y copie en otro array esos números multiplicados por 0.18. \
    
numbers = []
numbers2 = []
multiply = 0.18

for i in range(20, 40):
    numbers.append(i)
    
print(" ")
print("Lista Original:", numbers)
print(" ")

numbers2.extend(numbers)

for n in numbers:
    numbers2.append(n * multiply)
    
print(" ")
print("Lista multiplicada por 0.18:", numbers2)
print(" ")

