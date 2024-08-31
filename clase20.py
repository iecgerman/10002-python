# Funciones y Manejo de Excepciones en Python

# Funciones Lambda y Programación Funcional en Python

sumando = lambda a,b: a + b
print(sumando(10,4))

multiplicando = lambda a,b: a * b
print(multiplicando(80,5))

# Obtener el cuadrado de cada numero

numbers = range(11)

numeros_cuadrados = list(map(lambda x: x**2, numbers))
print("Numeros del 1 al 10 al cuadrado:\n", numeros_cuadrados)

# Obtener los números pares

even_numbers = list(filter(lambda x: x%2 ==0, numbers))
print("Pares:", even_numbers)