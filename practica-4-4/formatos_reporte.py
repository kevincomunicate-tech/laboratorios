class ReporteTexto:
    def generar(self, datos):
        return f"Reporte con los datos: {datos}"


class ReporteResumen:
    def generar(self, datos):
        return f"Cantidad de registros: {len(datos)}"


reportes = [ReporteTexto(), ReporteResumen()]
datos = ["Teclado", "Mouse", "Monitor"]

for reporte in reportes:
    print(reporte.generar(datos))
