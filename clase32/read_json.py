# Lectura y escritura de archivos

# Manejo de Archivos JSON (JAVASCRIPT OBJECT NOTATION)

import json

# Lectura de archivo JSON

with open('clase32/products.json', mode='r') as file:
    products = json.load(file)

# Mostrar el contenido

for product in products:
    #print(product)
    """
    {'name': 'Laptop', 'price': 1200, 'quantity': 4, 'brand': 'BrandName', 'category': 'Electronics', 'entry_date': '2024-01-05'}
    {'name': 'Mouse', 'price': 45, 'quantity': 120, 'brand': 'TechGear', 'category': 'Accessories', 'entry_date': '2024-02-10'}
    {'name': 'Headphones', 'price': 150, 'quantity': 25, 'brand': 'SoundMax', 'category': 'Audio', 'entry_date': '2024-03-15'}
    """
    print(f"| Producto: {product['name']:<16} | Precio: $ {product['price']:>8} |")
    """
    | Producto: Laptop           | Precio: $     1200 |
    | Producto: Mouse            | Precio: $       45 |
    | Producto: Headphones       | Precio: $      150 |
    """
