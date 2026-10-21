class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False
        self.saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0 or monto > self.saldo:
            return False
        self.saldo -= monto
        return True

    def consultar_saldo(self):
        return self.saldo


b1 = Billetera("Ana")
b2 = Billetera("Luis")

b1.registrar_ingreso(100000)
b1.registrar_gasto(30000)
b2.registrar_ingreso(50000)

print("Saldo Ana:", b1.consultar_saldo())
print("Saldo Luis:", b2.consultar_saldo())
