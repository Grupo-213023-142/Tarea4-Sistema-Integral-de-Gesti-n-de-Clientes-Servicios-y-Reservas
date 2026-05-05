# Importamos modelos y excepciones
from modelos.cliente import Cliente
from modelos.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from modelos.reserva import Reserva
from excepciones.errores_personalizados import ErrorSistema

# Clase GestorSistema para manejar operaciones del sistema
class GestorSistema:
    def __init__(self):
        # Listas internas para guardar clientes y reservas
        self.clientes = []
        self.reservas = []

    def registrar_cliente(self, id, nombre, email, telefono):
        try:
            # Creamos un cliente y validamos sus datos
            cliente = Cliente(id, nombre, email, telefono)
            cliente.validar()
            self.clientes.append(cliente)
            return cliente
        except Exception as e:
            # Si algo falla, lanzamos un error del sistema
            raise ErrorSistema(f"Error al registrar cliente: {e}")

    def crear_reserva(self, cliente, servicio, duracion):
        try:
            # Creamos una reserva y la confirmamos
            reserva = Reserva(cliente, servicio, duracion)
            reserva.confirmar()
            self.reservas.append(reserva)
            return reserva
        except Exception as e:
            # Si algo falla, lanzamos un error del sistema
            raise ErrorSistema(f"Error al crear reserva: {e}")

    def cancelar_reserva(self, reserva):
        try:
            # Cancelamos la reserva
            reserva.cancelar()
            return reserva
        except Exception as e:
            raise ErrorSistema(f"Error al cancelar reserva: {e}")
