import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"


def exportar_csv(inventario):
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)
    datos = inventario.exportar_datos()

    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        campos = ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for item in datos:
            fila = {
                "codigo": item["codigo"],
                "nombre": item["nombre"],
                "categoria": item["categoria"],
                "precio": item["precio"],
                "cantidad": item["cantidad"],
                "valor_inventario": item["precio"] * item["cantidad"]
            }
            escritor.writerow(fila)

    return RUTA_CSV
