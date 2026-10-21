from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("Debes escribir un número válido.")
            continue
        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue
        return precio


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debes escribir un número entero.")
            continue
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue
        return cantidad


def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio = leer_precio()
            cantidad = leer_cantidad()
            try:
                producto = Producto(codigo, nombre, categoria, precio, cantidad)
                if inventario.registrar_producto(producto):
                    print("Producto registrado.")
                else:
                    print("Código duplicado. No se registró.")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "2":
            productos = inventario.listar_productos()
            if len(productos) == 0:
                print("No hay productos registrados.")
            else:
                for p in productos:
                    print(p.codigo, "-", p.nombre, "-", p.categoria, "- $", p.precio, "-", p.cantidad, "unidades")

        elif opcion == "3":
            codigo = input("Código: ").strip()
            encontrado = inventario.buscar_por_codigo(codigo)
            if encontrado is not None:
                print(encontrado.codigo, "-", encontrado.nombre, "-", encontrado.categoria, "- $", encontrado.precio, "-", encontrado.cantidad, "unidades")
            else:
                print("Producto no registrado.")

        elif opcion == "4":
            codigo = input("Código: ").strip()
            nueva = leer_cantidad()
            if inventario.actualizar_existencias(codigo, nueva):
                print("Existencias actualizadas.")
            else:
                print("No se pudo actualizar.")

        elif opcion == "5":
            codigo = input("Código: ").strip()
            if inventario.eliminar_producto(codigo):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":
            agotados = inventario.productos_sin_stock()
            if len(agotados) == 0:
                print("No hay productos sin stock.")
            else:
                print("Sin existencias:")
                for nombre in agotados:
                    print("-", nombre)

        elif opcion == "7":
            cantidad, unidades, valor, categorias = inventario.resumen()
            print("Productos registrados:", cantidad)
            print("Unidades disponibles:", unidades)
            print("Valor del inventario: $", valor)
            print("Categorías utilizadas:", len(categorias))

        elif opcion == "0":
            print("Programa finalizado.")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
