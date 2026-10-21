import json
import csv
from pathlib import Path

productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0}
]

ruta_json = Path("inventario.json")
ruta_csv = Path("inventario.csv")

with ruta_json.open("w", encoding="utf-8") as archivo:
    json.dump(productos, archivo, ensure_ascii=False, indent=4)
print("Inventario guardado en JSON.")

try:
    with ruta_json.open("r", encoding="utf-8") as archivo:
        recuperados = json.load(archivo)
    print("Productos recuperados:")
    for p in recuperados:
        print(p["codigo"], "-", p["nombre"])
except FileNotFoundError:
    print("Archivo no encontrado.")
except json.JSONDecodeError:
    print("JSON inválido. No se sobrescribe.")

with ruta_csv.open("w", newline="", encoding="utf-8") as archivo:
    campos = ["codigo", "nombre", "precio", "cantidad"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(productos)
print("Inventario exportado a CSV.")
