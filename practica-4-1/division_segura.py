try:
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
except ValueError:
    print("Debes escribir números válidos.")
else:
    try:
        resultado = a / b
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
