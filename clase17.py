# Control de Flujo en Python

# Bucles y Control de Iteraciones

numbers = [1,2,3,4,5,6]
for i in numbers:
    print("Aqui i es igual a:", i+1)

# Aqui i es igual a: 2
# Aqui i es igual a: 3
# Aqui i es igual a: 4
# Aqui i es igual a: 5
# Aqui i es igual a: 6
# Aqui i es igual a: 7

for i in range(10):
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(1,11):
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")

# Manzana
# Pera
# Uva
# Naranja
# Naranja encontrada
# Tomate

x = 0
while x<5:
    print(x)
    x += 1

# 0
# 1
# 2
# 3
# 4

x=0
while x<5:
    if x==3:
        break
    print(x)
    x +=1

# 0
# 1
# 2

numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue
    print("Aqui i es igual a:", i)

# Aqui i es igual a: 1
# Aqui i es igual a: 2
# Aqui i es igual a: 4
# Aqui i es igual a: 5
# Aqui i es igual a: 6

numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        break
    print("Aqui i es igual a:", i)

# Aqui i es igual a: 1
# Aqui i es igual a: 2