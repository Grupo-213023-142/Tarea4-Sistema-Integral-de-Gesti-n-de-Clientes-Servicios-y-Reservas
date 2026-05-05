# Importamos librerías necesarias
import logging
from excepciones.errores_personalizados import ErrorReserva

# Clase Reserva que integra cliente y servicio
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def confirmar(self):
        try:
            # Intentamos calcular el costo de la reserva
            costo = self.servicio.calcular_costo(horas=self.duracion, impuesto=0.19)
            self.estado = "confirmada"
            logging.info(f"Reserva confirmada para {self.cliente} con costo {costo}")
        except Exception as e:
            # Si hay error, la reserva falla
            self.estado = "fallida"
            logging.error(f"Error al confirmar reserva: {e}")
            raise ErrorReserva(str(e))

    def cancelar(self):
        # Método sencillo para cancelar la reserva
        self.estado = "cancelada"
        logging.info(f"Reserva cancelada para {self.cliente}")
