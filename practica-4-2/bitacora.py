nombre = input("Nombre de la prueba: ")
resultado = input("Resultado (aprobada/fallida): ")
observacion = input("Observación: ")

linea = f"{nombre} | {resultado} | {observacion}\n"

with open("pruebas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(linea)

print("Registro agregado.")
