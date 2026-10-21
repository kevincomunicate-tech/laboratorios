from unidades import kilometros_a_metros, celsius_a_fahrenheit

km = float(input("Kilómetros: "))
metros = kilometros_a_metros(km)
print("Metros:", metros)

celsius = float(input("Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)
