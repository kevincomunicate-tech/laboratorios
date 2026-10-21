from pathlib import Path

carpeta = Path("reportes")
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "resumen.txt"
ruta.write_text(
    "Resumen de inventario\nProductos registrados: 0\nValor total: 0\n",
    encoding="utf-8"
)

contenido = ruta.read_text(encoding="utf-8")
print(contenido)
print("Ruta:", ruta)
