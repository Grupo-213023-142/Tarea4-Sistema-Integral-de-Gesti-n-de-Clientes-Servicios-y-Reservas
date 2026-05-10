"""
Módulo encargado de gestionar las operaciones principales del sistema Software FJ.

Esta clase administra clientes, reservas y cancelaciones mediante listas internas,
sin utilizar bases de datos. También centraliza validaciones y manejo de errores
para mantener la estabilidad del sistema.
"""

import logging

# Importamos modelos y excepciones (Unificados de ambas ramas)
from modelos.cliente import Cliente
from modelos.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from modelos.reserva import Reserva
from excepciones.errores_personalizados import ErrorSistema


class GestorSistema:
    """
    Clase encargada de coordinar las operaciones principales del sistema.

    Administra:
        - Registro de clientes.
        - Creación de reservas.
        - Cancelación de reservas.
        - Consulta de clientes y reservas almacenadas.
    """

    def __init__(self):
        # Listas internas para guardar clientes y reservas
        self.clientes = []
        self.reservas = []

    def _obtener_id_cliente(self, cliente):
        """
        Obtiene el identificador de un cliente de forma segura.

        Se usa getattr para conservar compatibilidad con distintas versiones
        de la clase Cliente durante la integración de ramas.
        """
        return getattr(cliente, "id", getattr(cliente, "_id", None))

    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca un cliente registrado por su identificador.

        Args:
            id_cliente: Identificador del cliente.

        Returns:
            Cliente o None: Cliente encontrado o None si no existe.
        """
        for cliente in self.clientes:
            if str(self._obtener_id_cliente(cliente)) == str(id_cliente):
                return cliente
        return None

    def registrar_cliente(self, id, nombre, email, telefono):
        """
        Registra un cliente en el sistema.

        Args:
            id: Identificador único del cliente.
            nombre: Nombre completo del cliente.
            email: Correo electrónico.
            telefono: Número telefónico.

        Returns:
            Cliente: Cliente registrado.

        Raises:
            ErrorSistema: Si el cliente no puede ser registrado.
        """
        try:
            if self.buscar_cliente_por_id(id) is not None:
                raise ErrorSistema(f"Ya existe un cliente registrado con ID {id}.")

            cliente = Cliente(id, nombre, email, telefono)

            # Se conserva esta llamada por claridad académica, aunque Cliente
            # también puede validar desde su constructor.
            cliente.validar()

        except ErrorSistema:
            logging.error(f"No se pudo registrar el cliente con ID {id}.")
            raise

        except Exception as error:
            logging.error(f"Error registrando cliente: {error}")
            raise ErrorSistema(
                f"Error registrando cliente: {error}"
            ) from error

        else:
            self.clientes.append(cliente)
            logging.info(f"Cliente registrado correctamente: {cliente}")
            return cliente

        finally:
            logging.info("Proceso de registro de cliente finalizado.")

    def crear_reserva(self, cliente, servicio, duracion):
        """
        Crea y confirma una reserva en el sistema.

        Args:
            cliente: Cliente asociado a la reserva.
            servicio: Servicio seleccionado.
            duracion: Duración de la reserva.

        Returns:
            Reserva: Reserva creada y confirmada.

        Raises:
            ErrorSistema: Si la reserva no puede crearse o confirmarse.
        """
        reserva = None
        try:
            if cliente is None:
                raise ErrorSistema("No se puede crear una reserva sin cliente.")

            if servicio is None:
                raise ErrorSistema("No se puede crear una reserva sin servicio.")

            id_cliente = self._obtener_id_cliente(cliente)

            if self.buscar_cliente_por_id(id_cliente) is None:
                raise ErrorSistema(
                    "El cliente debe estar registrado antes de crear una reserva."
                )

            reserva = Reserva(cliente, servicio, duracion)
            reserva.confirmar()

        except ErrorSistema:
            logging.error("No se pudo crear la reserva por una validación del sistema.")
            raise

        except Exception as error:
            logging.error(f"Error creando reserva: {error}")

            # Si la reserva alcanzó a crearse y quedó en estado fallido,
            # se registra para conservar trazabilidad de la operación.
            if reserva is not None and reserva not in self.reservas:
                self.reservas.append(reserva)

            raise ErrorSistema(
                f"Error creando reserva: {error}"
            ) from error

        else:
            self.reservas.append(reserva)
            logging.info(f"Reserva creada correctamente: {reserva}")
            return reserva

        finally:
            logging.info("Proceso de creación de reserva finalizado.")

    def cancelar_reserva(self, reserva):
        """
        Cancela una reserva existente en el sistema.

        Args:
            reserva: Reserva que se desea cancelar.

        Returns:
            Reserva: Reserva cancelada.

        Raises:
            ErrorSistema: Si la reserva no puede cancelarse.
        """
        try:
            if reserva is None:
                raise ErrorSistema("No se puede cancelar una reserva inexistente.")

            if reserva not in self.reservas:
                raise ErrorSistema("La reserva no pertenece al sistema.")

            reserva.cancelar()

        except ErrorSistema:
            logging.error("No se pudo cancelar la reserva por una validación del sistema.")
            raise

        except Exception as error:
            logging.error(f"Error cancelando reserva: {error}")
            raise ErrorSistema(
                f"Error cancelando reserva: {error}"
            ) from error

        else:
            logging.info(f"Reserva cancelada correctamente: {reserva}")
            return reserva

        finally:
            logging.info("Proceso de cancelación de reserva finalizado.")

    def listar_clientes(self):
        """
        Retorna la lista de clientes registrados.
        """
        return self.clientes

    def listar_reservas(self):
        """
        Retorna la lista de reservas gestionadas por el sistema.
        """
        return self.reservas

    def resumen_sistema(self):
        """
        Genera un resumen básico del estado actual del sistema.

        Returns:
            dict: Cantidad de clientes y reservas registradas.
        """
        return {
            "clientes_registrados": len(self.clientes),
            "reservas_registradas": len(self.reservas)
        }
    