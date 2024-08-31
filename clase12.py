# Colección y Procesamiento de Datos en Python

# Listas de más dimensiones y Tuplas 

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9,]]
print(matrix)
print(matrix[2][1]) #fila 2 columna 8

# Resultado: 8

numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[0])

# Resultado:

# (1, 2, 3, 4, 5)
# <class 'tuple'>
# 1

#numbers[0] = 'unos'

#     numbers[0] = 'unos'
#     ~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment  

# las tuplas son inmutables

numbers2 = 6,7,8,9 #es opcionale poner parentesis, python ya te los reconoce como tuplas

print(numbers2)
print(type(numbers2))

# (6, 7, 8, 9)
# <class 'tuple'>

"""
puedes añadir, eliminar o modificar datos de una lista dentro de una tupla. En sí, puedes aplicar todas estas operaciones a los tipos de datos compuestos:

Listas
Diccionarios
Conjuntos
Objetos
Con los que no es posible son con las tuplas y los tipos de datos primitivo:

Booleano
String
Entero
Flotante
Complejo

Las listas multidimensionales sirven como matrices para organizar datos en filas y columnas. Las tuplas son inmutables y pueden usarse donde se requieren datos que no cambien.
"""

