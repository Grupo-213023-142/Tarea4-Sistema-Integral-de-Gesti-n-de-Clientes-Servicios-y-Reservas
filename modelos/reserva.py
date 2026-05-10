"""
Módulo encargado de gestionar las reservas del sistema Software FJ.

La clase Reserva integra un cliente, un servicio, una duración y un
estado. Implementa confirmación, cancelación y manejo de excepciones
para evitar que errores operativos detengan la ejecución del sistema.
"""

import logging

from modelos.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from excepciones.errores_personalizados import ErrorReserva, ErrorValidacion


class Reserva:
    """
    Representa una reserva realizada por un cliente sobre un servicio.

    Estados posibles:
        pendiente
        confirmada
        cancelada
        fallida
    """

    ESTADO_PENDIENTE = "pendiente"
    ESTADO_CONFIRMADA = "confirmada"
    ESTADO_CANCELADA = "cancelada"
    ESTADO_FALLIDA = "fallida"

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = self.ESTADO_PENDIENTE

        self.validar()

    def validar(self):
        """
        Valida los datos principales de la reserva.

        Raises:
            ErrorReserva: Si falta cliente, servicio o duración válida.
        """

        if self.cliente is None:
            raise ErrorReserva("La reserva debe tener un cliente asociado.")

        if self.servicio is None:
            raise ErrorReserva("La reserva debe tener un servicio asociado.")

        if not isinstance(self.duracion, (int, float)):
            raise ErrorReserva("La duración de la reserva debe ser numérica.")

        if self.duracion <= 0:
            raise ErrorReserva("La duración de la reserva debe ser mayor a cero.")

        return True

    def confirmar(self):
        """
        Confirma la reserva y calcula el costo del servicio asociado.

        Returns:
            float: Costo total calculado.

        Raises:
            ErrorReserva: Si la reserva no puede ser confirmada.
        """

        try:
            if self.estado != self.ESTADO_PENDIENTE:
                raise ErrorReserva(
                    f"No se puede confirmar una reserva en estado '{self.estado}'."
                )

            disponible = getattr(self.servicio, "disponible", True)

            if not disponible:
                raise ErrorReserva("El servicio seleccionado no está disponible.")

            if isinstance(self.servicio, ReservaSala):
                costo = self.servicio.calcular_costo(
                    horas=self.duracion,
                    impuesto=0.19
                )

            elif isinstance(self.servicio, AlquilerEquipo):
                costo = self.servicio.calcular_costo(
                    dias=self.duracion,
                    impuesto=0.19
                )

            elif isinstance(self.servicio, AsesoriaEspecializada):
                costo = self.servicio.calcular_costo(
                    horas=self.duracion,
                    tarifa_extra=20
                )

            else:
                raise ErrorReserva("Servicio no soportado por el sistema.")

        except (ErrorReserva, ErrorValidacion) as error:
            self.estado = self.ESTADO_FALLIDA
            logging.error(f"Error al confirmar reserva: {error}")

            raise ErrorReserva(
                f"No se pudo confirmar la reserva: {error}"
            ) from error

        except Exception as error:
            self.estado = self.ESTADO_FALLIDA
            logging.error(f"Error inesperado al confirmar reserva: {error}")

            raise ErrorReserva(
                f"Ocurrió un error inesperado al confirmar la reserva: {error}"
            ) from error

        else:
            self.estado = self.ESTADO_CONFIRMADA
            logging.info(f"Reserva confirmada para {self.cliente}")
            return costo

        finally:
            logging.info("Proceso de confirmación de reserva finalizado.")

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.

        Raises:
            ErrorReserva: Si la reserva ya está cancelada o fallida.
        """

        try:
            if self.estado == self.ESTADO_CANCELADA:
                raise ErrorReserva("La reserva ya se encuentra cancelada.")

            if self.estado == self.ESTADO_FALLIDA:
                raise ErrorReserva("No se puede cancelar una reserva fallida.")

            self.estado = self.ESTADO_CANCELADA

        except ErrorReserva as error:
            logging.error(f"Error al cancelar reserva: {error}")
            raise

        except Exception as error:
            logging.error(f"Error inesperado al cancelar reserva: {error}")
            raise ErrorReserva(
                f"Error inesperado al cancelar reserva: {error}"
            ) from error

        else:
            logging.info(f"Reserva cancelada para {self.cliente}")

        finally:
            logging.info("Proceso de cancelación de reserva finalizado.")

    def __str__(self):
        return (
            f"Reserva(cliente={self.cliente}, "
            f"servicio={self.servicio.descripcion()}, "
            f"duracion={self.duracion}, estado={self.estado})"
        )