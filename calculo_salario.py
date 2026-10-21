nombre = input("Nombre del trabajador: ")
horas = int(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

pago_total = horas * valor_hora

print(f"Trabajador: {nombre}")
print(f"Horas: {horas}")
print(f"Valor por hora: ${valor_hora}")
print(f"Pago total: ${pago_total}")
