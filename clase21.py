# Funciones y Manejo de Excepciones en Python

# ¿Cómo realizar una función recursiva en Python?

# def factorial(n):    
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# factorial_5 = factorial(5)

# print(factorial_5)


# funcion de Fibonacci

# def fibonacci(n):
#     if n == 0:
#         return(0)
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# number = 5
# print(fibonacci(number))

#RETO SUMATORIA DE NUMEROS NATURALES
def suma_de_numeros_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_de_numeros_naturales(n-1)

print(suma_de_numeros_naturales(4))

for i in range(5):
    print(f"la suma de numeros naturales hasta {i} es: {suma_de_numeros_naturales(i)}")