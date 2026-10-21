import json
from pathlib import Path
from inventario import Inventario
from producto import Producto

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


def guardar_inventario(inventario):
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
    datos = inventario.exportar_datos()
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
    return True


def cargar_inventario():
    if not RUTA_JSON.exists():
        return Inventario()

    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError:
        raise ValueError("El archivo JSON está dañado o tiene formato incorrecto.")

    if not isinstance(datos, list):
        raise ValueError("El contenido del JSON no es una lista de productos.")

    inventario = Inventario()
    try:
        inventario.cargar_desde_datos(datos)
    except (KeyError, TypeError, ValueError) as e:
        raise ValueError(f"Error al reconstruir productos: {e}")

    return inventario
