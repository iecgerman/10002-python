# Lectura y escritura de archivos

# Manejo de Archivos .txt

"""
En Python, la función strip() elimina los espacios en blanco y otros caracteres que se encuentran al inicio y al final de una cadena. Es una herramienta útil para manipular cadenas, una tarea común y esencial en la programación. 
 
La función strip() puede aceptar un argumento que especifique los caracteres que se eliminarán de la cadena original. Si no se especifica ningún argumento, se eliminarán todos los espacios en blanco. 
 
Por ejemplo, si se ingresa "Jorge Alejandro", la función strip() devolverá “Jorge Alejandro” sin el espacio en blanco inicial
"""

# Leer un archivo linea por linea
# with open('clase30/caperucita.txt', 'r') as file:
#     for lineas in file:
#         print(lineas.strip())


# with open('clase30/caperucita.txt', 'r') as file:
#     for lineas in file:
#         print(lineas)

# Resultado con muchos espacios entre lineas:

# "Grandma, what big eyes you have!" she said.



# "All the better to see you with, my dear," replied the wolf.

# Leer todas las lineas en una lista
# with open('clase30/caperucita.txt', 'r') as file:
#     lines =  file.readlines()
#     print(lines)

# Resultado

"""
['Little Red Riding Hood\n', '\n', 'Once upon a time... Little Red Riding Hood learned an important lesson: always listen to your mother and never talk to strangers.\n', '\n']
"""

# Añadir texto con 'a'
# with open('clase30/caperucita.txt', 'a') as file:  # 'a' <-- significa append
#     file.write("\n\nBy: ChatGPT")

# Sobreescribir el texto
# with open('clase30/caperucita.txt', 'w') as file:
#           file.write("\n\nCUIDADO AL USAR 'w' PORQUE TE BORRA TODO")

# RETO conteo de las lineas del cuento de caperucita
with open ("clase30/caperucita.txt", "r") as file:
    lines = file.readlines()
    print(len(lines)) # 63