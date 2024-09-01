# Colección y Procesamiento de Datos en Python

# Comprehensions Lists en Python

# squares = [x**2 for x in range(1,101)]
# print("Cuadrados", squares)

# Transformar Grados Celcius a Fahrenheit

# celsius = [0,10,20,30,40]
# fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
# print("Temperatura en F:", fahrenheit)

# Numeros pares

# evens = [x for x in range(1,21) if x%2 ==0]
# print(evens)

# Números impares

# evens = [x for x in range(1,21) if x%2 !=0]
# print(evens)

# Resultado:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Transposed

matrix = [[1,2,3,],
          [4,5,6],
          [7,8,9]]

print(matrix)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# print(transposed)

# este es el código sin usar Comprehensions Lists

transposed = []
for i in range(len(matrix[0])):
    print(i)
    transposed_row = []
    for row in matrix:
        print(transposed_row)
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    print(transposed_row)

print(transposed)

# Resultado:

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
0
[]
[1]
[1, 4]
[1, 4, 7]
1
[]
[2]
[2, 5]
[2, 5, 8]
2
[]
[3]
[3, 6]
[3, 6, 9]
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]