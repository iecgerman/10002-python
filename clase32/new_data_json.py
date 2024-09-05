import json

file_path = 'clase32/products.json'

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-09-05"
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)
    """
    ¿Qué es dump() en Python?
    Función dump(). La función json. dump() de Python permite almacenar datos JSON directamente en un archivo .
    """

