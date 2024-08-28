# Programación Orientada a Objetos en Python

# Fundamentos de Programación Orientada a Objetos en Python

"""
La Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en el uso de **objetos** para diseñar y desarrollar aplicaciones. Este enfoque se centra en crear software que sea modular, reutilizable y más fácil de mantener. Aquí están los fundamentos clave de la POO:

### 1. **Clases y Objetos**

- **Clase:** Una clase es un molde o plantilla que define las propiedades (atributos) y comportamientos (métodos) que tendrán los objetos creados a partir de ella. Por ejemplo, una clase Coche podría tener atributos como color, marca, y modelo, y métodos como arrancar() o frenar().

- **Objeto:** Un objeto es una instancia de una clase. Es un elemento concreto que se crea a partir de una clase, con valores específicos para sus atributos. Por ejemplo, un objeto de la clase Coche podría ser un coche rojo de la marca Toyota y modelo Corolla.

### 2. **Encapsulamiento**

- El encapsulamiento consiste en ocultar los detalles internos de un objeto y exponer sólo lo necesario. Esto se logra mediante el uso de **modificadores de acceso** como private, protected, y public, que controlan qué partes de un objeto pueden ser accedidas o modificadas desde fuera de su clase. Esto protege los datos y asegura que solo se modifiquen de manera controlada.

### 3. **Herencia**

- La herencia permite crear nuevas clases basadas en clases existentes. Una clase que hereda de otra (llamada **subclase** o **clase derivada**) toma los atributos y métodos de la clase base (llamada **superclase** o **clase padre**), y puede añadir o modificar funcionalidades. Esto fomenta la reutilización del código y la creación de jerarquías de clases. Por ejemplo, si tenemos una clase Vehículo, podemos crear una subclase Coche que herede de Vehículo.

### 4. **Polimorfismo**

- El polimorfismo permite que un mismo método o función pueda tener diferentes comportamientos según el objeto que lo invoque. Existen dos tipos principales de polimorfismo:

- **Polimorfismo en tiempo de compilación (sobrecarga):** Permite definir varios métodos con el mismo nombre pero diferentes parámetros.

- **Polimorfismo en tiempo de ejecución (sobreescritura):** Permite que una subclase redefina un método de su superclase para modificar su comportamiento.

### 5. **Abstracción**

- La abstracción consiste en representar conceptos esenciales sin incluir detalles de implementación específicos. Las clases abstractas y las interfaces son herramientas que permiten definir métodos sin implementarlos, dejando que las clases derivadas proporcionen la implementación. Esto facilita la creación de sistemas flexibles y extensibles.

### 6. **Modularidad**

- La POO promueve la división del software en módulos o componentes independientes (objetos), que pueden ser desarrollados, testeados y mantenidos por separado, pero que funcionan juntos como un todo coherente.

### 7. **Relaciones entre Objetos**

- Las clases y objetos pueden relacionarse de varias maneras, como:

- **Asociación:** Una relación donde un objeto utiliza a otro.

- **Agregación:** Una forma más débil de asociación, donde un objeto contiene referencias a otros objetos.

- **Composición:** Una forma más fuerte de agregación, donde un objeto contiene y controla completamente a otros objetos.

### Ventajas de la POO:

- **Reutilización de código:** Las clases pueden reutilizarse en diferentes partes de un programa o en diferentes proyectos.

- **Facilidad de mantenimiento:** El encapsulamiento y la modularidad facilitan la localización y corrección de errores.

- **Facilidad de expansión:** La herencia y la abstracción permiten agregar nuevas funcionalidades sin alterar el código existente.

- **Flexibilidad:** El polimorfismo permite que el código sea más flexible y fácil de extender.

Estos fundamentos hacen de la POO un enfoque poderoso y ampliamente utilizado en el desarrollo de software moderno.
"""

# class Person:
#     def __init__(self, name, age):
#         self.x = name
#         self.age = age

#     def greet(self):
#         print(f"Hola, mi nombre es {self.x} y tengo {self.age}")

# person1 = Person("Ana", 30)
# person2 = Person("Luis", 25)

# person1.greet()
# person2.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}, saldo actual {self.balance}")
        else:
            print("No se puede depositar, Cuenta inactiva")
    
    def withdraw(self, amount):
        if self.active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}, Saldo acutal es {self.balance}")

    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print("La cuenta ha sido activada")
    
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

# Llamada a los métodos

account1.deposit(200)
account2.deposit(100)
account1.deactivate_account()
account1.deposit(50)

account1.activate_account()
account1.deposit(50)



# https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/

# class Perro:
#     def sonido(self):
#         print('Guauuuuu!!!')
# class Gato:
#     def sonido(self):
#         print('Miaaauuuu!!!')        
# class Vaca:
#     def sonido(self):
#         print('Múuuuuuuu!!!')
# def a_cantar(animales):
#     for animal in animales:
#         animal.sonido()
# if __name__ == '__main__':
#     perro = Perro()
#     gato = Gato()
#     gato_2 = Gato()
#     vaca = Vaca()
#     perro_2 = Perro()
#     granja = [perro, gato, vaca, gato_2, perro_2]
#     a_cantar(granja)




# # Enter your date automatic
# class Enter_Date:
#     def __init__(self, name, years):
#         self.DateN = []
#         self.name = name
#         self.years = years
#         self.available = True

#     def list_date(self):
#         if self.available:
#             self.DateN.append(self.name)
#             self.DateN.append(self.years)
#             return self.DateN


# class start:
#     def __init__(self):
#         self.var1 = ""
#         self.var2 = ""

#     def conversation(self):
#         print("Hello today we are going to store data ")
#         print("1.Enter date ")
#         print("2.End ")
#         Enter1 = int(input())
#         if Enter1 == 1:
#             self.var1 = input("Enter your name: ")
#             self.var2 = input("Enter your age: ")
#             return self.var1, self.var2
#         else:
#             print("Coming out")


# income = int(input("Please income how much data going to Enter "))
# all_data = []

# user1 = None
# for i in range(income):
#     person1 = start()
#     person1.conversation()

#     user1 = Enter_Date(person1.var1, person1.var2)
#     all_data.append(user1.list_date())

# print(all_data)


# class Rol_family:
#     def __init__(self, data):
#         self.data = data
#         self.occupation = []

#     def enter_date(self, index):
#         adjusted_index = index - 1
#         if adjusted_index < len(self.data):
#             name, age = self.data[adjusted_index]
#             print(f"Hola {name} a question")
#             occupation_data = input("What is your occupation in the family? ")
#             self.occupation.append(occupation_data)
#             return occupation_data
#         else:
#             return "Index out of range"

#     def result_date(self, index):
#         if index < len(self.occupation):
#             name, age = self.data[index]
#             print(f"{name} of {age} ages your occupation in family is {self.occupation[index]}")
#         else:
#             print("Index out of range")


# start_family = Rol_family(all_data)

# for i in range(len(all_data)):
#     index_to_retrieve = int(input("Enter the index of the data you want to retrieve: "))
#     print(start_family.enter_date(index_to_retrieve))

# print(start_family.occupation)
# one = 0
# while one < len(all_data):
#     start_family.result_date(one)
#     one += 1