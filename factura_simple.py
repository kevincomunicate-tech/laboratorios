
nombre_producto = "Teclado Mecánico"
precio_unitario = 100000.0
cantidad = 2
porcentaje_descuento = 0.10  
porcentaje_impuesto = 0.19 

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento
total_con_descuento = subtotal - valor_descuento

base_impuesto = total_con_descuento
valor_impuesto = base_impuesto * porcentaje_impuesto
total_final = base_impuesto + valor_impuesto

print(f"Producto: {nombre_producto}")
print("--- Ejercicio Principal ---")
print(f"Subtotal: ${subtotal:.1f}")
print(f"Descuento: ${valor_descuento:.1f}")
print(f"Total después del descuento: ${total_con_descuento:.1f}")

print(f"Base después del descuento: ${base_impuesto:.1f}")
print(f"Valor del impuesto ({porcentaje_impuesto * 100}%): ${valor_impuesto:.1f}")
print(f"Total final: ${total_final:.1f}")
