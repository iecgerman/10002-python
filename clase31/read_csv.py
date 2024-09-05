import csv

# Leer un archivo
# with open('clase31/products.csv', mode='r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)

# Mostrar la informacion por columnas
with open('clase31/iva_file_path.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"| Cantidad: {row['quantity']:^4} | Producto: {row['name']:<20} | P. Unitario:  $ {row['price']:>6} | Subtotal: $ {row['total_value']:>8} | IVA: $ {row['IVA']}") # IVA tiene que ir en mayúsculas porque así se declaró