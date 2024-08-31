# Fundamentos de Programación y Python

# Manipulación de Cadenas de Texto en Python

"""
Manipulación de Cadenas de Texto en Python

Algunos métodos para cadenas son:

.count() 
.capitalize()
.title() 
.swapcase() 
.replace(,) 
.split() 
.strip() 
.lstrip() 
.rstrip() 
.find()
.index() 
eval()	#Este y el siguiente son super métodos
exec()

#Capitaliza la primera letra.

texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"

#title()
#Capitaliza la primera letra de cada palabra.
texto = "hola mundo"
print(texto.title())  # "Hola Mundo"

#strip()
#Elimina los espacios en blanco al inicio y al final.
texto = "  hola  "
print(texto.strip())  # "hola"

#replace(old, new)
#Reemplaza partes de la cadena.
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # "hola Python"

#split(sep)
#Divide la cadena en una lista según el separador.
texto = "hola,mundo,Python"
print(texto.split(","))  # ['hola', 'mundo', 'Python']

#join(iterable)
#Une elementos de un iterable en una sola cadena.
lista = ["hola", "mundo"]
print(" ".join(lista))  # "hola mundo"

#find(sub)
#Busca una subcadena y devuelve el índice de su primera aparición.
texto = "hola mundo"
print(texto.find("mundo"))  # 5

#startswith(prefix) y endswith(suffix)
#Verifica si la cadena empieza o termina con una subcadena.
texto = "hola mundo"
print(texto.startswith("hola"))  # True
print(texto.endswith("mundo"))  # True

#Ejemplo Completo:
frase = "  Bienvenido a Python!  "
frase = frase.strip().replace("Python", "el mundo de Python").upper()
print(frase)  # "BIENVENIDO A EL MUNDO DE PYTHON!"

"""

name = "German"
print(type(name))

caracter = "c"
print ("caracter")

name = 'German'
print(type(name))

name = 'German'
print(name)

name = '''QUE NO ERA PARA PONER COMENTARIOS


SALTOS DE LINEA
'''
print(name)


name = 'German Garcia'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

'''Usando SHIFT + ALT Y FLECHITA ABAJO PODEMOS DUPLICAR CODIGO'''

# PARA COMENTAR RAPIDO EN PYTHON CON VISUAL STUDIO CODE ES CON CTRL + C Y PARA DESHACER ES CON CTRL + U

# print(name[20]) 

print(name[-2])

name = 'German'
lastname = "Garcia"
print(name)
print(lastname)
print(name + lastname)
print(name + " " + lastname)

# Es de buenas practicas usar siempre el mismo tipo de comillas

name = 'G e R   m A n'
lastname = 'Ga Rc I a'
print(name)
print(lastname)
print(name + lastname)
print(name + ' ' + lastname)

print(name * 5)
print(5 * name)

print(len(name))
print(len(lastname))

print(name.lower())
print(name.upper())
print(lastname.strip())
print(name.strip())

ciudad = 'Monte rrey Guadalajara'
print(ciudad.strip())


#split(sep)
#Divide la cadena en una lista según el separador.
texto = "hola,mundo,Python"
print(texto.split(","))  # ['hola', 'mundo', 'Python']

correos = "info@correo.com, ventas@correo.com, compras@correo.com"

print(correos.split(", "))

lista_correos = (correos.split(", "))

print(lista_correos)

# imaginate que tienes miles de correos y tu ocupas saber cuantos correos son para no crear spam para poder enviar 50 correos por hora para no crear spam

print(len(lista_correos))