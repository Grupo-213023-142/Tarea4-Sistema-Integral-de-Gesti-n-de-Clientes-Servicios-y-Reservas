# Módulo que contiene las excepciones personalizadas del sistema.

# Excepción para errores de validación
class ErrorValidacion(Exception):

    # Constructor de la excepción
    def __init__(self, mensaje):

        super().__init__(mensaje)


# Excepción para errores relacionados con reservas
class ErrorReserva(Exception):

    # Constructor de la excepción
    def __init__(self, mensaje):

        super().__init__(mensaje)


# Excepción general del sistema
class ErrorSistema(Exception):

    # Constructor de la excepción
    def __init__(self, mensaje):

        super().__init__(mensaje)

# Excepción para servicios no disponibles
class ErrorServicio(Exception):

    # Constructor de la excepción
    def __init__(self, mensaje):

        super().__init__(mensaje)

# Excepción para errores de pago
class ErrorPago(Exception):

    # Constructor de la excepción
    def __init__(self, mensaje):

        super().__init__(mensaje)

# Excepción para duración inválida
class ErrorDuracion(Exception):

    # Constructor de la excepción
    def __init__(self, mensaje):

        super().__init__(mensaje)