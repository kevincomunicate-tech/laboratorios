class Notificacion:
    def enviar(self, mensaje):
        return f"Notificación: {mensaje}"


class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        return f"Correo enviado: {mensaje}"


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        return f"Consola: {mensaje}"


notificaciones = [
    NotificacionCorreo(),
    NotificacionConsola()
]

for n in notificaciones:
    print(n.enviar("Inventario actualizado"))
