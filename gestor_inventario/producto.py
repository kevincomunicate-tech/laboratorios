import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if codigo.strip() == "":
            raise ValueError("El código no puede estar vacío.")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if categoria not in CATEGORIAS:
            raise ValueError("Categoría no permitida.")
        if not isinstance(precio, (int, float)) or not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser un número finito mayor que cero.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo.")

        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            return False
        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )
