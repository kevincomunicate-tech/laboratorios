from pathlib import Path

ruta = Path("mensaje.txt")

try:
    contenido = ruta.read_text(encoding="utf-8")
    print("Contenido:")
    print(contenido)
except FileNotFoundError:
    print("No se encontró el archivo.")
