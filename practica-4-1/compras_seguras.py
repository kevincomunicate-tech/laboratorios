compras = []
suma = 0

while True:
    try:
        valor = float(input("Importe de compra (0 para terminar): "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if valor == 0:
        break

    if valor < 0:
        print("No se aceptan valores negativos.")
        continue

    compras.append(valor)
    suma += valor

print("Compras aceptadas:", len(compras))
print("Suma acumulada:", suma)
