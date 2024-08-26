# Funciones y Manejo de Excepciones en Python

# Manejo de Excepciones en Python y uso de pass

"""
¿Te estresas cuando te aparece un error en tu código? No te preocupes, todos los programadores nos enfrentamos a errores constantemente. De hecho, encontrar y solucionar errores es parte del trabajo diario de un programador. Sin embargo, lo que distingue a un buen programador de un excelente programador es la habilidad para manejar esos errores de manera efectiva. En este blog, exploraremos qué son las excepciones y los errores, por qué es importante manejarlos adecuadamente, y cómo hacerlo en Python.

Errores y Excepciones

Los términos “errores” y “excepciones” en el código a menudo se utilizan indistintamente, pero tienen diferencias clave:

Errores: Son problemas en el código que pueden ser sintácticos (como errores de escritura) o semánticos (como errores en la lógica del programa). Los errores detienen la ejecución del programa.
Excepciones: Son eventos que ocurren durante la ejecución de un programa y que alteran el flujo normal del código. A diferencia de los errores, las excepciones pueden ser manejadas para evitar que el programa se detenga.
Comprender los errores y las excepciones es vital porque:

Mejora la calidad del código: Permite escribir programas más robustos y menos propensos a fallos.
Facilita la depuración: Ayuda a identificar y solucionar problemas de manera más eficiente.
Mejora la experiencia del usuario: Evita que el programa se cierre abruptamente, ofreciendo mensajes de error claros y manejables.

Errores Básicos en Python

Antes de profundizar en el manejo de excepciones, es importante familiarizarnos con algunos errores comunes en Python.

SyntaxError

El SyntaxError ocurre cuando hay un error en la sintaxis del código. Por ejemplo:

# Código con SyntaxError
print("Hola Mundo"
Resultado:

SyntaxError: unexpected EOF while parsing
TypeError
El TypeError se produce cuando se realiza una operación en un tipo de dato inapropiado. Por ejemplo:

# Código con TypeError
resultado = "10" + 5
Resultado:

TypeError: can only concatenate str (not "int") to str
Estos son solo algunos ejemplos de los errores más comunes que se pueden encontrar en Python. Ahora, veamos cómo manejar excepciones para evitar que estos errores detengan la ejecución de nuestro programa.

La Estructura del try-except

En Python, el manejo de excepciones se realiza principalmente a través de la estructura try-except. Esta estructura permite intentar ejecutar un bloque de código y capturar las excepciones que puedan ocurrir, proporcionando una forma de manejar los errores de manera controlada. Esto no solo evita que el programa se detenga abruptamente, sino que también ofrece la oportunidad de informar al usuario sobre lo que salió mal y cómo puede solucionarlo.

¿Qué hace try?

La palabra clave try se utiliza para definir un bloque de código donde se anticipa que puede ocurrir un error. Python ejecuta este bloque y, si ocurre una excepción, transfiere el control al bloque except.

¿Qué hace except?

La palabra clave except define un bloque de código que se ejecuta si ocurre una excepción en el bloque try. Aquí es donde podemos manejar el error, limpiar el desorden, o proporcionar mensajes informativos al usuario.

Estructura Básica

La estructura básica de try-except es la siguiente:

try:
    # Código que puede generar una excepción
    pass
except NombreDeLaExcepcion:
    # Código que maneja la excepción
    pass

¿Por qué es importante manejar las excepciones?

Permitir que los errores sigan su curso sin control puede tener varias consecuencias negativas:

Interrupción del programa: Un error no manejado puede hacer que tu programa se detenga abruptamente, causando frustración en los usuarios.
Pérdida de datos: Si el programa se cierra inesperadamente, es posible que se pierdan datos importantes no guardados.
Mala experiencia del usuario: Los usuarios prefieren programas que manejen errores de manera elegante y les proporcionen mensajes claros sobre lo que salió mal y cómo pueden solucionarlo.
Manejar las excepciones con try-except permite:

Continuidad del programa: Permite que el programa continúe ejecutándose incluso cuando se encuentra un error.
Mensajes de error claros: Proporciona mensajes específicos que pueden ayudar al usuario a corregir el problema.
Mejor depuración: Facilita la identificación y corrección de errores, haciendo el proceso de depuración más eficiente.
Ejemplo de try-except
"""

# try:
#     valor = int(input("Ingresa un número: "))
#     resultado = 10 / valor
#     print(f"El resultado es {resultado}")
# except ValueError:
#     print("Por favor, ingresa un número válido.")
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")


"""
Resultado:

# Si el usuario ingresa "a":
Por favor, ingresa un número válido.

# Si el usuario ingresa "0":
No se puede dividir por cero.
Jerarquía de Excepciones
En Python, las excepciones están organizadas en una jerarquía, donde las excepciones más generales se encuentran en la parte superior y las más específicas en la parte inferior. Por ejemplo:

Jerarquia de Excepciones

Exception
    ArithmeticError
        FloatingPointError
        OverflowError
        ZeroDivisionError
    AssertionError
    AttributeError
    BufferError
    EOFError
    ImportError
        ModuleNotFoundError
        ZipImportError
    LookupError
        IndexError
        KeyError
        CodecRegistryError
    MemoryError
    NameError
        UnboundLocalError
    OSError
        BlockingIOError
        ChildProcessError
        ConnectionError
            BrokenPipeError
            ConnectionAbortedError
            ConnectionRefusedError
            ConnectionResetError
        FileExistsError
        FileNotFoundError
        InterruptedError
        IsADirectoryError
        NotADirectoryError
        PermissionError
        ProcessLookupError
        TimeoutError
        UnsupportedOperation
    ReferenceError
    RuntimeError
        NotImplementedError
        RecursionError
        _DeadlockError
    StopAsyncIteration
    StopIteration
    SyntaxError
        IndentationError
            TabError
    SystemError
        CodecRegistryError
    TypeError
    ValueError
        UnicodeError
            UnicodeDecodeError
            UnicodeEncodeError
            UnicodeTranslateError
        UnsupportedOperation
    Warning
        BytesWarning
        DeprecationWarning
        EncodingWarning
        FutureWarning
        ImportWarning
        PendingDeprecationWarning
        ResourceWarning
        RuntimeWarning
        SyntaxWarning
        UnicodeWarning
        UserWarning
    ExceptionGroup

Conocer esta jerarquía es útil para manejar excepciones de manera más precisa y efectiva.

Ejemplos Prácticos
Ejemplo 1: Manejo de ValueError
"""

# try:
#     edad = int(input("Introduce tu edad: "))
#     print(f"Tu edad es {edad}")
# except ValueError:
#     print("Error: Debes introducir un número.")

"""
Resultado:

# Si el usuario ingresa "veinte":
Error: Debes introducir un número.
Ejemplo 2: Manejo de múltiples excepciones
try:
    divisor = int(input("Ingresa un número divisor: "))
    resultado = 100 / divisor
    print(f"El resultado es {resultado}")
except ValueError:
    print("Error: Debes introducir un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
Resultado:

# Si el usuario ingresa "cero":
Error: No se puede dividir por cero.
Ejemplo 3: Manejo General de Excepciones
"""

# try:
#     nombre = input("Introduce tu nombre: ")
#     print(f"Hola, {nombre}!")
# except Exception as e:
#     print(f"Ha ocurrido un error: {e}")

"""
Resultado:

Hola, Juan!
Explorando la Jerarquía de Excepciones en Python
En Python, las excepciones están organizadas en una jerarquía de clases, donde cada excepción específica es una subclase de la clase base Exception.

El código proporcionado utiliza recursión para imprimir esta jerarquía comenzando desde la clase base Exception. Cada clase de excepción se muestra indentada según su nivel en la jerarquía, lo que ayuda a visualizar cómo están relacionadas las excepciones entre sí.
"""

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)

"""
Ahora te toca a ti! Ejecuta el código y observa cómo se imprime la jerarquía de excepciones, esto te permitirá comprender mejor cómo están estructuradas las excepciones y cómo puedes aprovechar esta estructura para manejar errores de manera más efectiva en tus programas.

Uso de pass

Antes de concluir, hablemos del uso de pass. Imagina que estás creando una función que sabes que vas a necesitar, pero no quieres crear la lógica ahora mismo y sigues con el código. Si solo pones el def sin el cuerpo o código dentro del nivel de indentación de la función, te producirá un error IndentationError.

Puedes solucionar esto usando pass, que es una declaración nula; no hace nada cuando se ejecuta, pero es útil como un marcador de posición para que la estructura del código sea válida.

Ejemplo de pass

def mi_funcion():
    pass  # Marcador de posición para el cuerpo de la función

print("Continuando con el código...")

Resultado:

Continuando con el código...

En este ejemplo, pass permite definir la estructura de la función sin implementar la lógica de inmediato, evitando errores de indentación y permitiendo continuar con el desarrollo del código.

A medida que utilices nuevas herramientas en Python, como librerías y otros tipos de datos, te encontrarás con excepciones específicas de esas herramientas. Familiarizarte con las excepciones comunes de cada librería te permitirá manejarlas de manera más efectiva y escribir código más robusto. Recuerda, el manejo adecuado de excepciones no solo mejora tu código, sino que también te convierte en un programador más competente y confiable.
"""



