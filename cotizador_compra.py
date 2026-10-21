cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
pct_descuento = int(input("Descuento (%): "))
pct_impuesto = int(input("Impuesto (%): "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (pct_descuento / 100)

base = subtotal - valor_descuento
valor_impuesto = base * (pct_impuesto / 100)

total = base + valor_impuesto

print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"TOTAL: ${total}")
