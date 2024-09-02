# Programación Orientada a Objetos en Python

# Uso de super() en Python

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello! I am a person.")

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def greet(self):
#         super().greet()
#         print(f"Hello, my student ID is {self.student_id}")

# student = Student("Ana", 20, "S123")
# student.greet()

#ahora LivingBegin sera nuestra super clase
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
        print(f"Hi, I am {self.name}, I have {self.age} years old, and my student ID is {self.student_id}")

student = Student("Ana", 20, "S123")
student.introduce()

# Hi, I am Ana, I have 20 years old, and my student ID is S123