precio = 215000.0
cantidad = 14
porcentaje_descuento = 0.19

subtotal = precio * cantidad
descuento = subtotal * porcentaje_descuento
total = subtotal - descuento

print("Precio unitario: $", precio)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", descuento)
print("Total: $", total)