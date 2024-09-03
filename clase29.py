# Programación Orientada a Objetos en Python

# Superando los Fundamentos de Programación Orientada a Objetos en Python

"""
Para entender mejor la Programación Orientada a Objetos (POO), es esencial recordar los conceptos básicos de atributos y métodos.

Atributos: Son variables que pertenecen a una clase o a sus objetos. Definen las propiedades de un objeto. Por ejemplo, pensemos en una persona: ¿Qué caracteriza a una persona en general? Las personas tienen nombre, edad, dirección, etc. En términos de POO, estos serían los atributos de la clase Person.
Métodos: Son funciones definidas dentro de una clase que operan sobre sus objetos. Definen los comportamientos de un objeto. Siguiendo con el ejemplo de una persona, ¿Qué acciones puede realizar una persona? Puede hablar, caminar, comer, etc. En POO, estas acciones serían métodos de la clase Person.
"""

class Person:
    def __init__(self, name, age):
        self.name = name  # Atributo
        self.age = age    # Atributo

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")  # Método

# Crear una instancia de la clase Person
persona1 = Person("Ana", 30)
persona1.greet()  # Output: Hola, mi nombre es Ana y tengo 30 años.

"""
al usar herencia vimos el método init() que es le cosntructor, el mismo es llamado automáticamente cuando se crea una nueva instancia de una clase y se utiliza para inicializar los atributos del objeto.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Crear una instancia de Person
person1 = Person("Ana", 30)
print(person1.name)  # Output: Ana
print(person1.age)   # Output: 30

"""
En este ejemplo, el constructor __init__ inicializa los atributos name y age de la clase Person.

Uso de super() en Python

La función super() en Python te permite acceder y llamar a métodos definidos en la superclase desde una subclase. Esto es útil cuando quieres extender o modificar la funcionalidad de los métodos de la superclase sin tener que repetir su implementación completa.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hi, I'm {self.name}, and I'm a student with ID: {self.student_id}")

# Crear instancia de Student y llamar a greet
student = Student("Ana", "age", "S12345")
student.greet()  # Output: Hello! I am a person.
                 #         Hi, I'm Ana, and I'm a student with ID: S12345

"""
En este ejemplo:

La clase Person define un método greet() que imprime un saludo genérico.

La clase Student, que es una subclase de Person, utiliza super().__init__(name, age) para llamar al constructor de la superclase Person y luego sobrescribe el método greet() para agregar información específica del estudiante.

Jerarquía de Clases y Constructores

¿Qué sucede si una clase tiene una clase padre y esa clase padre tiene otra clase padre? En este caso, usamos super() para asegurar que todas las clases padre sean inicializadas correctamente.

Ejemplo de Jerarquía de Clases

"""
class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

# Crear instancia de Student
student = Student("Carlos", 21, "S54321")
student.introduce()  # Output: Hi, I'm Carlos, 21 years old, and my student ID is S54321

"""
En este ejemplo:

LivingBeing es la clase base que inicializa el atributo name.
Person es una subclase de LivingBeing que inicializa name a través de super().__init__(name) y luego inicializa age.
Student es una subclase de Person que inicializa name y age a través de super().__init__(name, age) y luego inicializa student_id.
Métodos que Vienen por Defecto en Python
En Python, todas las clases heredan de la clase base object. Esto significa que todas las clases tienen ciertos métodos por defecto, algunos de los cuales pueden ser útiles para personalizar el comportamiento de tus clases.

Métodos por Defecto Más Comunes
__init__(self): Constructor de la clase. Es llamado cuando se crea una nueva instancia de la clase. Inicializa los atributos del objeto.
__str__(self): Devuelve una representación en cadena del objeto, utilizada por print() y str(). Este método es útil para proporcionar una representación legible del objeto.
__repr__(self): Devuelve una representación “oficial” del objeto, utilizada por repr(). Este método está diseñado para devolver una cadena que represente al objeto de manera que se pueda recrear.
Ejemplo de Métodos __str__ y __repr__
Vamos a crear una clase Person que sobrescriba los métodos __str__ y __repr__.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Crear instancias de Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Uso de __str__
print(person1)  # Output: Alice, 30 años

# Uso de __repr__
print(repr(person1))  # Output: Person(name=Alice, age=30)
print(repr(person2))  # Output: Person(name=Bob, age=25)

"""
Explicación del Código
El método __str__ devuelve una representación en cadena del objeto, útil para mensajes de salida amigables.
El método __repr__ devuelve una representación más detallada del objeto, útil para la depuración.
Estos métodos proporcionan una manera conveniente de representar y comparar objetos, lo que facilita la depuración y el uso de los objetos en el código.

Importancia de Aprender estos Conceptos
Comprender y utilizar super(), los métodos por defecto y los constructores es crucial para escribir código limpio, eficiente y reutilizable en Python. Estos conceptos permiten:

Extender Funcionalidades: super() permite extender las funcionalidades de una superclase sin duplicar código.
Inicialización Correcta: El uso adecuado de constructores asegura que todos los atributos sean inicializados correctamente.
Personalizar Representaciones: Métodos como __str__ y __repr__ permiten personalizar cómo se representan los objetos, facilitando la depuración y el manejo de datos.
Comparar y Ordenar Objetos: Métodos como __eq__, __lt__, etc., permiten definir cómo se comparan y ordenan los objetos, lo cual es esencial para muchas operaciones de datos.
"""