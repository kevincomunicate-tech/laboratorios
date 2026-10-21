from pathlib import Path

ruta = Path("operaciones.txt")

while True:
    print()
    print("1. Registrar operación")
    print("2. Mostrar historial")
    print("0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        concepto = input("Concepto: ").strip()
        valor = input("Valor: ").strip()
        linea = f"{concepto} | {valor}\n"
        with ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(linea)
        print("Operación registrada.")

    elif opcion == "2":
        try:
            contenido = ruta.read_text(encoding="utf-8")
            if contenido.strip() == "":
                print("No hay operaciones registradas.")
            else:
                print(contenido)
        except FileNotFoundError:
            print("No hay operaciones registradas.")

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
