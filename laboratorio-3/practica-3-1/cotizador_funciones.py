def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    return base * porcentaje / 100


precio = 100000
cantidad = 2
descuento_porcentaje = 10
impuesto_porcentaje = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, descuento_porcentaje)
base = subtotal - descuento
impuesto = calcular_impuesto(base, impuesto_porcentaje)
total = base + impuesto

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Base después del descuento:", base)
print("Impuesto:", impuesto)
print("Total:", total)
