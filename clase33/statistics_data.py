# Biblioteca estándar de Python

# Librería Statistics y Análisis Estadístico

import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo CSV

monthly_sales = {}

with open('clase33/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())

# print(sales)

# Media: Promedio de todas las ventas mensuales.

# la media de los datos

mean_sales = statistics.mean(sales)
print(f"La media de es: {mean_sales}")

# Mediana: Valor medio de las ventas ordenadas, útil cuando hay valores extremos.

# la mediana de los datos

median_sales = statistics.median(sales)
print(f"La mediana de es: {median_sales}")

# Moda: Valor que más se repite en las ventas.

# la moda de los datos

mode_sales = statistics.mode(sales)
print(f"La moda de es: {mode_sales}")

# Desviación Estándar y Varianza: Miden la dispersión de las ventas respecto a la media; la desviación estándar está en las mismas unidades que los datos, mientras que la varianza está en unidades al cuadrado.

# La desvición estandar

stdev_sales = statistics.stdev(sales)
print(f"La desvición estándar es: {stdev_sales}")

# hallar la varianza

variance_sales = statistics.variance(sales)
print(f"La varianza es: {variance_sales}")

# Máximo y Mínimo: Ventas más altas y más bajas registradas.

max_sales = max(sales)
print(f"La venta mas alta fue: {max_sales}")

min_sales = min(sales)
print(f"La venta mas baja fue: {min_sales}")

# Rango de ventas

# Rango: Diferencia entre la venta más alta y la más baja.

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')