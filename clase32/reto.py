# CSV A JSON

import csv
import json

file_csv='clase32/products.csv'
reto_csv_to_json='clase32/reto_csv_to_json.json'

data=[]

with open(file_csv,'r') as fileCSV:
    csvreader=csv.DictReader(fileCSV)
    for row in csvreader:
        data.append(row)

with open(reto_csv_to_json,mode='w') as file:
    json.dump(data,file,indent=4)

print(data[0:3])

# [{'name': 'Laptop', 'price': '1200', 'quantity': '4', 'brand': 'BrandName', 'category': 'Electronics', 'entry_date': '2024-01-05'}, {'name': 'Mouse', 'price': '45', 'quantity': '120', 'brand': 'TechGear', 'category': 'Accessories', 'entry_date': '2024-02-10'}, {'name': 'Keyboard', 'price': '70', 'quantity': '60', 'brand': 'KeyMasters', 'category': 'Accessories', 'entry_date': '2024-02-12'}]


# JSON A CSV

import csv
import json

file_json ='clase32/products.json'
reto_json_to_csv ='clase32/reto_json_to_csv.csv'

with open(file_json, 'r') as file:
    data = json.load(file)

headers =  data[0].keys()

with open(reto_json_to_csv, mode='w', newline='') as file:

    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(data)

for row in data:
    print(row)

# {'name': 'Laptop', 'price': 1200, 'quantity': 4, 'brand': 'BrandName', 'category': 'Electronics', 'entry_date': '2024-01-05'}
# {'name': 'Mouse', 'price': 45, 'quantity': 120, 'brand': 'TechGear', 'category': 'Accessories', 'entry_date': '2024-02-10'}
# {'name': 'Headphones', 'price': 150, 'quantity': 25, 'brand': 'SoundMax', 'category': 'Audio', 'entry_date': '2024-03-15'} 
