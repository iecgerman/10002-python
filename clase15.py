# Control de Flujo en Python

# Estructuras condicionales

# x = 5

# if x > 5:
#     print("X es mayor que 5")
# elif x==5:
#     print("x es iugal que 5")
# else:
#     print("X es menor que 5")
# print("afuera")

# x = 1
# y = 26

# if x>10 and y>25:
#     print("X es mayor que 10 y Y es mayor que 15")

# if x>10 or y>25:
#     print("X es mayor que 10 o Y es mayor que 25")

# if not x>10:
#     print("X no es mayor que 10")

is_member = True
age = 11
if is_member:
    if age>= 15:
        print("tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
    print("no eres miembro y NO TIENE ACCESO")