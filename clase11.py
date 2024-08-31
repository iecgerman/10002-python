# Colección y Procesamiento de Datos en Python

# Método slice 

a = [1,2,3,4,5]
b = a
print(a)
print(b)

del a[0]
print(a)
print(b)

"""Resultado:

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[2, 3, 4, 5]

esto sucede porque apuntan al mismo espacio en memoria"""

print(id(a))
print(id(b))

"""Resultado:

2320109852928
2320109852928

para que no pase esto debemos usar slicing"""

c = a[:]

print(id(a))
print(id(b))
print(id(c))

"""Resultado:

2630577543424
2630577543424
2630577863232"""

a.append(6)

print(a)
print(b)
print(c)

"""Resultado:

[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6]
[2, 3, 4, 5]

En otros lenguajes de programación no puedes almacenar diferentes clases dentro de una colección"""