def mostrar_productos(productos):
    for producto in productos:
        print(producto)


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def valor_inventario(productos):
    total = 0
    for producto in productos:
        total += producto["precio"] * producto["cantidad"]
    return total


def productos_sin_stock(productos):
    nombres = []
    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])
    return nombres


productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

mostrar_productos(productos)
print(buscar_producto(productos, "P001"))
print(valor_inventario(productos))
print(productos_sin_stock(productos))
