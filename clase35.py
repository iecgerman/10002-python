# Biblioteca estándar en Python

# Librería Os, Math y Random

# import os

# Obtener el directorio actual
"""cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)"""

# Directorio de trabajo actual C:\Users\info\10002-python

# Listar los archivos
"""txt_files = [f for f in os.listdir('./clase30') if f.endswith('.txt')]
print("Archivos txt: ", txt_files) # Archivos txt:  ['caperucita.txt']"""

# Renombrar archivo
"""os.rename('clase30/caperucita.txt', 'clase30/cuento.txt')
print('Archivo renombrado')"""

"""txt_files = [f for f in os.listdir('./clase30') if f.endswith('txt')]
print("Archivos txt: ", txt_files) # Archivos txt:  ['cuento.txt']"""

import math

# Hallar el area y permetro de un circulo
"""radius = 5
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
print(area)
print(perimeter)"""

# 78.53981633974483
# 31.41592653589793

import random

# Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

# Elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)

# BArajar una lista de cartas
cards = ['As', 'Rey', 'Queen', 'Joto', '10','9','8','7','6','5','4','3','2']
random.shuffle(cards)
print(cards)