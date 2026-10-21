import validaciones

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
categoria = input("Categoría: ")

if (
    validaciones.nombre_valido(nombre)
    and validaciones.precio_valido(precio)
    and validaciones.cantidad_valida(cantidad)
    and validaciones.categoria_valida(categoria, CATEGORIAS)
):
    print("Datos aceptados.")
else:
    print("Revisa los datos.")
