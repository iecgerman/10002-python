# Programación Orientada a Objetos en Python

# Herencia en POO con Python

"""La herencia, junto con la encapsulación y el polimorfismo, es una de las tres características principales de la programación orientada a objetos. La herencia permite crear clases que reutilizan, extienden y modifican el comportamiento definido en otras clases. La clase cuyos miembros se heredan se denomina clase base o padre y la clase que hereda esos miembros se denomina clase derivada o clase hija. Una clase hija solo puede tener una clase padre directa, pero la herencia es transitiva. Si ClassC se deriva de ClassB y ClassB se deriva de ClassA, ClassC hereda los miembros declarados en ClassB y ClassA.

Un ejemplo sencillo de herencia que nos permite conceptualizarlo:"""

class Mamifero:
    def __init__(self):
        pass
    
    def features(self):
        print('Tiene pelaje y glandulas mamarias')

class Perro(Mamifero):
    def __init__(self):
        pass
    
    def bark(self):
        print('Woof!!')
    
    def walking(self):
        print('Paseando alegre')
        
    def eat(self):
        print('Comiendo contento')

class Cachorro(Perro):
    def __init__(self):
        pass
    
    def play(self):
        print('Jugando y mordiendo zapatos')
        
cachorro1 = Cachorro()
cachorro1.bark()
cachorro1.play()
cachorro1.features()

# class Vehicle:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.is_available = True

#     def sell(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"El vehiculo {self.brand}, ha sido vendido")
#         else:
#             print(f"El vehiculo {self.brand}, no esta disponible")
    
#     def check_available(self):
#         return self.is_available
    
#     def get_price(self):
#         return self.price
    
#     def start_engine(self):
#         raise NotImplementedError("Este metodo debe ser implementado por la subclase(clase hija)")
    
#     def stop_engine(self):
#         raise NotImplementedError("Este metodo debe ser implementado por la subclase(clase hija)")
    
# class Car(Vehicle):
#     def start_engine(self):
#         if not self.is_available:
#             return print(f"el motor del coche {self.brand} esta en marcha")
#         else:
#             return print(f"el coche {self.brand} no esta disponible")
        
#     def stop_engine(self):
#         if self.is_available:
#             return print(f"El motor del coche {self.brand} se ha detenido")
#         else:
#             return print(f"El coche {self.brand} no esta disponible")
        

