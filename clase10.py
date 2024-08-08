# Colección y Procesamiento de Datos en Python

# Listas

to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)

numbers = [1,2,3,4, "cinco"]
print(numbers)
print(type(numbers))

mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)

print(len(mix))

print("primer elemento de la lista mix por medio de la indexacion es:", mix[0])
print("segundo elemento", mix[1])
print("ultimo elemento", mix[-1])

string = "HOLA MUNDO"
print("primer elemento---->", string[0])
print("segundo elemento--->", string[1])
print("tercer elemento---->", string[2])
print("cuarto elemento---->", string[3])

# SLICING

print(mix[0:2])
print(mix[:2])
print(mix[2:])

# AÑADIR EN UN LISTA

mix.append(False)
print(mix)

mix.append(["a","b"])
print(mix)

# INSERTAR

mix.insert(1,["a","b"])
print(mix)
print(len(mix))

print(mix[0])
print(mix[1])
print(mix[2])
print(mix[3])
print(mix[4])
print(mix[5])
print(mix[6])
print(mix[7])

# CONSULTAR

print(mix)
print(mix.index(["a","b"]))
print(mix.index("uno"))
print(mix.index(3.14))

# ELEMENTO MAYO O MENOR

numbers = [1,2,100.01,90.45,3,4,5]
print(numbers)
print("Mayor:", max(numbers))
print("Menor:", min(numbers))

# ELIMINAR ELEMENTOS

del numbers[-1]
print(numbers)

del numbers[:2]
print(numbers)

del numbers
print(numbers)

# esto equivaldrá en SQL a no poner un WHERE cuando queremos borrar registro de una table y si no lo ponemos se nos borra toda la tabla??