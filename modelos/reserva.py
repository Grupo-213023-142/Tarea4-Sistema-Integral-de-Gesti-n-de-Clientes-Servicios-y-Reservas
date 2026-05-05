
## Módulo encargado de gestionar las reservas del sistema


# Importamos librería de logs
import logging

# Importamos clases de servicios
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

# Importamos excepción personalizada
from excepciones.errores_personalizados import ErrorReserva


# Clase Reserva
class Reserva:

    # Constructor de la clase
    def __init__(self, cliente, servicio, duracion):

        # Atributos de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        # Estado inicial
        self.estado = "pendiente"

    # Método encargado de confirmar la reserva
    def confirmar(self):

        try:

            # Verificamos si el servicio es ReservaSala
            if isinstance(self.servicio, ReservaSala):

                costo = self.servicio.calcular_costo(
                    horas=self.duracion,
                    impuesto=0.19
                )

            # Verificamos si el servicio es AlquilerEquipo
            elif isinstance(self.servicio, AlquilerEquipo):

                costo = self.servicio.calcular_costo(
                    dias=self.duracion,
                    impuesto=0.19
                )

            # Verificamos si el servicio es AsesoriaEspecializada
            elif isinstance(self.servicio, AsesoriaEspecializada):

                costo = self.servicio.calcular_costo(
                    horas=self.duracion,
                    tarifa_extra=20
                )

            # Si el servicio no existe
            else:

                raise ErrorReserva(
                    "Servicio no soportado"
                )

        # Capturamos errores durante el proceso
        except Exception as e:

            # Cambiamos estado a fallida
            self.estado = "fallida"

            # Registramos error en logs
            logging.error(
                f"Error al confirmar reserva: {e}"
            )

            # Encadenamos excepción
            raise ErrorReserva(
                f"No se pudo confirmar la reserva: {e}"
            ) from e

        # Se ejecuta si no ocurre excepción
        else:

            # Cambiamos estado
            self.estado = "confirmada"

            # Registramos evento exitoso
            logging.info(
                f"Reserva confirmada para {self.cliente}"
            )

            return costo

        # Se ejecuta siempre
        finally:

            logging.info(
                "Proceso de confirmación finalizado"
            )

    # Método encargado de cancelar reserva
    def cancelar(self):

        try:

            # Cambiamos estado
            self.estado = "cancelada"

        # Capturamos errores
        except Exception as e:

            raise ErrorReserva(
                f"Error al cancelar reserva: {e}"
            ) from e

        # Se ejecuta si no ocurre error
        else:

            logging.info(
                f"Reserva cancelada para {self.cliente}"
            )

        # Se ejecuta siempre
        finally:

            logging.info(
                "Proceso de cancelación finalizado"
            )