# Funciones y Manejo de Excepciones en Python

# Manejo de Excepciones en Python y uso de pass

while True:
    try:
        divisor = int(input("Ingresa un numero divisor: "))
        result = 100/divisor
        print(result)
    except ZeroDivisionError as e:
        print("ERROR: No se puede dividir entre 0")
        print("Ha ocurrido un error del tipo:", e)
    except ValueError as e:
        print("ERROR: Debes introducir cualquier numero que no sea cero")
        print("Ha ocurrido un error del tipo:", e)