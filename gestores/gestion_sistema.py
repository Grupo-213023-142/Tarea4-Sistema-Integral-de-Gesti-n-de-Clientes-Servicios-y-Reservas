##################################################################
# Módulo encargado de gestionar las operaciones
# principales del sistema.
#
# Aquí se administran:
# - Clientes
# - Reservas
# - Cancelaciones
##################################################################

# Importamos la clase Cliente
from modelos.cliente import Cliente

# Importamos la clase Reserva
from modelos.reserva import Reserva

# Importamos excepción personalizada
from excepciones.errores_personalizados import (
    ErrorSistema
)


# Clase encargada de controlar el sistema
class GestorSistema:

    # Constructor de la clase
    def __init__(self):

        # Lista para almacenar clientes
        self.clientes = []

        # Lista para almacenar reservas
        self.reservas = []

    # Método encargado de registrar clientes
    def registrar_cliente(
        self,
        id,
        nombre,
        email,
        telefono
    ):

        try:

            # Creamos objeto cliente
            cliente = Cliente(
                id,
                nombre,
                email,
                telefono
            )

            # Validamos datos del cliente
            cliente.validar()

        # Capturamos errores del proceso
        except Exception as e:

            # Encadenamos excepción personalizada
            raise ErrorSistema(
                f"Error registrando cliente: {e}"
            ) from e

        # Se ejecuta si no ocurre excepción
        else:

            # Guardamos cliente en la lista
            self.clientes.append(cliente)

            return cliente

        # Se ejecuta siempre
        finally:

            print(
                "Proceso de registro finalizado"
            )

    # Método encargado de crear reservas
    def crear_reserva(
        self,
        cliente,
        servicio,
        duracion
    ):

        try:

            # Creamos objeto reserva
            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            # Confirmamos la reserva
            reserva.confirmar()

        # Capturamos errores
        except Exception as e:

            # Encadenamos excepción personalizada
            raise ErrorSistema(
                f"Error creando reserva: {e}"
            ) from e

        # Se ejecuta si no ocurre excepción
        else:

            # Guardamos reserva
            self.reservas.append(reserva)

            return reserva

        # Se ejecuta siempre
        finally:

            print(
                "Proceso de reserva finalizado"
            )

    # Método encargado de cancelar reservas
    def cancelar_reserva(self, reserva):

        try:

            # Cancelamos la reserva
            reserva.cancelar()

        # Capturamos errores
        except Exception as e:

            # Encadenamos excepción personalizada
            raise ErrorSistema(
                f"Error cancelando reserva: {e}"
            ) from e

        # Se ejecuta si no ocurre excepción
        else:

            return reserva

        # Se ejecuta siempre
        finally:

            print(
                "Proceso cancelación finalizado"
            )