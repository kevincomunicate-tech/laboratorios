from producto import Producto
from inventario import Inventario

inventario = Inventario()

print(inventario.agregar(Producto("P001", "Teclado")))
print(inventario.agregar(Producto("P002", "Mouse")))
print(inventario.agregar(Producto("P001", "Otro")))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

encontrado = inventario.buscar_por_codigo("P002")
if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")

print(inventario.eliminar("P999"))
print(inventario.eliminar("P001"))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)
