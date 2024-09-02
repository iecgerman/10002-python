# Funciones y Manejo de Excepciones en Python

# Uso de Funciones en Python 

# def greet():
#     print('Hola Mundo')

# greet()

# def greet(name):
#     print("Hola", name)

# greet('German')
# greet('Yanira')

# def greet(name, last_name):
#     print('Hola', name, last_name)

# greet("German", "Garcia")
# greet("Yanira", "Mendoza")


# def greet(name, last_name="FALTO SU APELLIDO"):
#     print('Hola', name, last_name)

# greet("German")
# greet("Yanira", "Mendoza")

# greet(last_name="MENDOZA", name="YANIRA")

def sumando(a,b):
    return a+b

def restando(a,b):
    return a-b

def multiplicando(a,b):
    return a*b

def dividiendo(a,b):
    return a/b

def calculadora():
    while True:
        print("Selecciones una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Exit")

        option = input("Ingresa su opción 1,2,3,4 o 5: ")

        if option == "5":
            print("Esta saliendo de la calculadora")
            break
        
        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                print("La suma es: ", sumando(num1, num2))
            elif option == "2":
                print("La resta es:", restando(num1, num2))
            elif option == "3":
                print("La multiplicación es: ", multiplicando(num1,num2))
            elif option == "4":
                print("La división es: ", dividiendo(num1,num2))
        
        else:
            print("Opción no válida, por favor intente de nuevo")

calculadora()