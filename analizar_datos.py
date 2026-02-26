import pandas as pd
import openpyxl

# Leer con openpyxl para ver la estructura raw
wb = openpyxl.load_workbook('docente XLSX.xlsx')
ws = wb.active

print("=" * 80)
print("ANÁLISIS DEL ARCHIVO EXCEL")
print("=" * 80)
print(f"\nDimensiones de la hoja: {ws.dimensions}")
print(f"\nPrimeras 15 filas (datos raw):")

for i in range(1, 16):
    row_data = []
    for j in range(1, 15):
        cell = ws.cell(row=i, column=j)
        row_data.append(cell.value)
    print(f"Fila {i}: {row_data}")

# Ahora leer con pandas
print("\n" + "=" * 80)
print("ANÁLISIS CON PANDAS")
print("=" * 80)

df = pd.read_excel('docente XLSX.xlsx', sheet_name=0)
print(f"\nForma del dataframe: {df.shape}")
print(f"\nNombres de columnas:")
for i, col in enumerate(df.columns):
    print(f"  Columna {i}: {col}")

print(f"\nPrimeras 10 filas:")
print(df.head(10))

print(f"\nInfo del dataframe:")
print(df.info())

# Ver valores únicos en columnas clave
print(f"\nValores únicos en columna 0 (Regional): {df.iloc[:, 0].nunique()}")
print(f"Primeros 5 valores únicos: {df.iloc[:, 0].dropna().unique()[:5].tolist()}")
