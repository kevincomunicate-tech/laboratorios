num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
    division_entera = num1 // num2
    residuo = num1 % num2
else:
    division = "No se puede dividir entre cero"
    division_entera = "No se puede dividir entre cero"
    residuo = "No se puede dividir entre cero"

print("\n" + "="*30)
print("="*30)
print(f"Suma ({num1} + {num2}): {suma}")
print(f"Resta ({num1} - {num2}): {resta}")
print(f"Multiplicación ({num1} * {num2}): {multiplicacion}")
print(f"División ({num1} / {num2}): {division}")
print(f"División entera ({num1} // {num2}): {division_entera}")
print(f"Residuo/Módulo ({num1} % {num2}): {residuo}")
print("="*30)
