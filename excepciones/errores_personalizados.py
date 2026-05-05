# Definimos errores personalizados para el sistema

# Error de validación de datos (ejemplo: email o teléfono inválido)
class ErrorValidacion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Error relacionado con reservas (ejemplo: servicio no disponible)
class ErrorReserva(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Error general del sistema
class ErrorSistema(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
