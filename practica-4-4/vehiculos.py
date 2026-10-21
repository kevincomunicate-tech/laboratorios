class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje


moto1 = Motocicleta("Yamaha", "YZF-R3", 321)
moto2 = Motocicleta("Honda", "CBR500R", 471)

print(moto1.marca, moto1.modelo, moto1.cilindraje)
print(moto2.marca, moto2.modelo, moto2.cilindraje)
