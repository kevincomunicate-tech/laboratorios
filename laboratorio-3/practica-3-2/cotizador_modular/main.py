from calculos import calcular_subtotal, calcular_descuento, calcular_impuesto
from validaciones import precio_valido, cantidad_valida, porcentaje_valido

precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
descuento_porcentaje = float(input("Descuento: "))
impuesto_porcentaje = float(input("Impuesto: "))

if (
    precio_valido(precio)
    and cantidad_valida(cantidad)
    and porcentaje_valido(descuento_porcentaje)
    and porcentaje_valido(impuesto_porcentaje)
):
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
else:
    print("Revisa los datos.")
