# Fundamentos de Programación y Python

# Todo lo que Debes Saber sobre print en Python

# La coma dentro de la función print se usa para separar varios argumentos. Al hacerlo, Python añade automáticamente un espacio entre los argumentos. Esto es diferente a concatenar cadenas con el operador +, que no añade espacios adicionales.

print("manzana", "pera", "naranja", "melon")

# Resultado:

# manzana pera naranja melon

# Por otro lado, al concatenar cadenas con el operador +, los elementos se unen sin ningún espacio adicional, a menos que lo añadas explícitamente.

print("manzana" + "pera" + "naranja" + "melon")

# Resultado:

# manzanaperanaranjamelon

# Para añadir un espacio explícitamente cuando concatenas cadenas, debes incluirlo dentro de las comillas.

print("manzana" + " " + "pera" + " " + "naranja" + " " + "melon")

# Resultado:

# manzana pera naranja melon

# El parámetro sep permite especificar cómo separar los elementos al imprimir.

print("ventas@tunegocio.com","compras@tunegocio.com","comercial@tunegocio.com", sep=", ")

# Resultado:

# ventas@tunegocio.com, compras@tunegocio.com, comercial@tunegocio.com

# El parámetro end cambia lo que se imprime al final de la llamada a print. En lugar de imprimir cada mensaje en una nueva línea, end="" asegura que “German” y “Paco” se impriman en la misma línea, resultando en “German, Paco”.

print("Lista de invitados: ")
print("German", end=", ")
print("Paco")
print("Lizandro")

# Resultado:

# Lista de invitados:
# German, Paco
# Lizandro

# Puedes usar print para mostrar el valor de las variables. En este ejemplo, imprimirá “Frase: Just Do It” y “Autor: Nike”. Esto es útil para depurar y ver los valores de las variables en diferentes puntos de tu programa.

frase="Just Do It"
author = "Nike"
print("Frase:",frase,"Autor:",author)

# Resultado:

# Frase: Just Do It Autor: Nike

# Las f-strings permiten insertar expresiones dentro de cadenas de texto. Al anteponer una f a la cadena de texto, puedes incluir variables directamente dentro de las llaves {}

base = 10
altura = 30
area = base * altura
print(f"Al multiplicar la base de {base} m por la altura de {altura} metros, obtenemos un area de {area} m2")

# Resultado:

# Al multiplicar la base de 10 m por la altura de 30 metros, obtenemos un area de 300 m2
# Resultado:

# Puedes controlar el formato de los números al imprimir. En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales. Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales. Esto es especialmente útil cuando trabajas con datos numéricos y necesitas un formato específico.

pi = 3.1415926535897932384626433832795
print("pi es igual: {:.5f}".format(pi))

# Resultado:

# pi es igual: 3.14159

# Los saltos de línea en Python se indican con la secuencia de escape \n. Por ejemplo, para imprimir “Hola\nmundo”, que aparecerá en dos líneas:

print("Hola\nmundo")

# Resultado:

# Hola
# mundo

# Para imprimir una cadena que contenga comillas simples o dobles dentro de ellas, debes usar secuencias de escape para evitar confusiones con la sintaxis de Python. Por ejemplo, para imprimir la frase “Hola soy ‘Carli’”:

print('Hola soy \'Carli\'')

# Otra es que simepre usas las mismas comilas y las que quieras imprimir no las uses como codigo
print("hola soy 'German'")
print('hola soy "German"')

# Resultado:

# Hola soy 'Carli'
# hola soy 'German'
# hola soy "German"

# Si necesitas imprimir una ruta de archivo en Windows, que incluya barras invertidas, también necesitarás usar secuencias de escape para evitar que Python interprete las barras invertidas como parte de secuencias de escape. Por ejemplo:

print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")

# Resultado:

# La ruta de archivo es: C:\Users\Usuario\Desktop\archivo.txt