kilometros = float(input("Ingresa la distancia en Kilometros:"))

metros = kilometros * 1000
centimetros = kilometros * 100000
millas = kilometros * 0.621371

print(f"Kilómetros: {kilometros} km")
print(f"Metros:     {metros} m")
print(f"Centímetros:{centimetros} cm")
print(f"Millas:     {millas:.6f} mi")