import json
from pathlib import Path

ruta = Path("productos.json")

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
    print("Productos cargados:", len(productos))
    for p in productos:
        print(p)
except FileNotFoundError:
    print("El archivo no existe. Se inicia con lista vacía.")
    productos = []
except json.JSONDecodeError:
    print("El archivo no contiene JSON válido. No se sobrescribe.")
