import csv

file_path = 'clase31/products_updated.csv'
iva_file_path = 'clase31/iva_file_path.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['IVA']

    with open(iva_file_path, mode='w', newline='') as iva_file:
        csv_writer = csv.DictWriter(iva_file, fieldnames=fieldnames)
        csv_writer.writeheader() # Escribir los encabezados

        for row in csv_reader:
            row['IVA'] = float(row['total_value']) * float(0.16)
            csv_writer.writerow(row)