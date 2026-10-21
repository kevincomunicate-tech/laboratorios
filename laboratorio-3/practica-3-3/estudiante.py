class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print("Nombre:", self.nombre)
        print("Ficha:", self.ficha)
        print("Promedio:", self.promedio)

    def aprobo(self):
        return self.promedio >= 3.0


est1 = Estudiante("Ana", "123", 2.8)
est2 = Estudiante("Luis", "456", 4.1)

est1.mostrar_perfil()
print("Aprobó:", est1.aprobo())

est2.mostrar_perfil()
print("Aprobó:", est2.aprobo())
