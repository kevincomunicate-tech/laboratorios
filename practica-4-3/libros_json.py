import json
from pathlib import Path

libros = [
    {"codigo": "L001", "titulo": "Python Básico", "autor": "Ana López", "año": 2020},
    {"codigo": "L002", "titulo": "Estructuras de Datos", "autor": "Carlos Ruiz", "año": 2021},
    {"codigo": "L003", "titulo": "POO en Python", "autor": "María Gómez", "año": 2022}
]

ruta = Path("libros.json")

with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, ensure_ascii=False, indent=4)

print("Libros guardados.")

with ruta.open("r", encoding="utf-8") as archivo:
    recuperados = json.load(archivo)

for libro in recuperados:
    print(libro["codigo"], "-", libro["titulo"], "-", libro["autor"])
