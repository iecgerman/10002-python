# Control de Flujo en Python

# Generadores e Iteradores 

# Ejemplo de iterador

# Crear una lista

my_list = [1,2,3,4]

# Obtener el iterador

my_iter = iter(my_list)

# Usar el iterador
# print(next(my_iter))

#1

# print(next(my_iter))
# print(next(my_iter))

#1
#2

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# 1
# 2
# 3
# 4

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))

# Traceback (most recent call last):
#   File "c:\Users\info\10002-python\clase17.py", line 40, in <module>
#     print(next(my_iter))
#           ^^^^^^^^^^^^^
# StopIteration


# Iterar en cadenas
# Creando la cadena
text = "Hola mundo"
# Creando el iterador
iter_text = iter(text)

# Iterar en la cadena
for char in iter_text:
    print(char)

# H
# o
# l
# a

# m
# u
# n
# d
# o

# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter =  iter(range(1,limit+1,2))

# Usar el iterador
for num in odd_itter:
    print(num)

# 1
# 3
# 5
# 7
# 9

# Numeros pares
odd_itter =  iter(range(0,limit+1,2))

# Usar el iterador
for num in odd_itter:
    print(num)

# 0
# 2
# 4
# 6
# 8
# 10

# GENERADOR

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# 1
# 2
# 3

# SERIE DE FIBONACCI

#  1 1 2 3 5 8 13 21 . . .

def fibonacci(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a,b = b, a+b

for num in fibonacci(10):
    print(num)

# 0
# 1
# 1
# 2
# 3
# 5
# 8

print("***** RETO IMPARES ******")

def odd_generator(limit):
    odd_num = 1
    while odd_num < limit:
        yield odd_num
        odd_num += 2
for result in odd_generator(10):
    print(result)

# ***** RETO IMPARES ******
# 1
# 3
# 5
# 7
# 9


print("***** RETO PARES ******")

def odd_generator(limit):
    pair_num = 0
    while pair_num < limit:
        yield pair_num
        pair_num += 2
for result in odd_generator(10):
    print(result)

# ***** RETO PARES ******
# 0
# 2
# 4
# 6
# 8