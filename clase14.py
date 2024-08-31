# Colección y Procesamiento de Datos en Python

# Diccionarios 

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)
print(numbers[2])

# {1: 'uno', 2: 'dos', 3: 'tres'}
# dos

information = {
    "Nombre":   "Carla",
    "Apellido": "Florida",
    "Altura":   "1.60",
    "Edad":     "29"
    }

print(information)
del information["Edad"]
print(information)

# {'Nombre': 'Carla', 'Apellido': 'Florida', 'Altura': '1.60', 'Edad': '29'}
# {'Nombre': 'Carla', 'Apellido': 'Florida', 'Altura': '1.60'}

# podemos preguntarle las claves

claves = information.keys()
print(claves)
print(type(claves))

# dict_keys(['Nombre', 'Apellido', 'Altura'])
# <class 'dict_keys'>

# tambien podemos imprimir solo los valores

valores = information.values()
print(valores)

# dict_values(['Carla', 'Florida', '1.60'])

# tambien nos da los pares

pares = information.items()
print(pares)

# dict_items([('Nombre', 'Carla'), ('Apellido', 'Florida'), ('Altura', '1.60')])

# Tambien podemos hacer un diccionario de diccionarios

contacts = {
    "Carla": 
            {
                "Apellido": "Florida",
                "Altura":   "1.60",
                "Edad":     "29"
            },
    "Diego":
            {
                "Apellido": "Antezana",
                "Altura":   "1.80",
                "Edad":     "32"
            }
}

print(contacts)

# {'Carla': {'Apellido': 'Florida', 'Altura': '1.60', 'Edad': '29'}, 'Diego': {'Apellido': 'Antezana', 'Altura': '1.80', 'Edad': '32'}}

print(contacts["Carla"])

# {'Apellido': 'Florida', 'Altura': '1.60', 'Edad': '29'}