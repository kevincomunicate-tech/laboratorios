nombre = input("Ingresa tu nombre completo: ")
ciudad = input("Ingresa tu ciudad de residencia: ")

edad = int(input("Ingresa tu edad (en años): "))

estatura = float(input("Ingresa tu estatura (en metros, ej: 1.75): "))

print("\n" + "="*30)

print("="*30)
print(f"Nombre:   {nombre}")
print(f"Ciudad:   {ciudad}")
print(f"Edad:     {edad} años")
print(f"Estatura: {estatura:.2f} metros")
print("="*30)
