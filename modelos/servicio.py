#Módulo encargado de gestionar los diferentes
#tipos de servicios del sistema.


# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# Importamos excepción personalizada
from excepciones.errores_personalizados import ErrorValidacion


# Clase abstracta Servicio
class Servicio(ABC):

    # Constructor de la clase
    def __init__(self, nombre, costo_base):

        # Atributos encapsulados
        self._nombre = nombre
        self._costo_base = costo_base

    # Método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass

    # Método abstracto para describir el servicio
    @abstractmethod
    def descripcion(self):
        pass


# Clase concreta para reserva de salas
class ReservaSala(Servicio):

    # Método sobrescrito para calcular costo
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):

        # Validamos horas válidas
        if horas <= 0:

            raise ErrorValidacion(
                "Las horas deben ser mayores a 0"
            )

        # Cálculo del costo
        costo = self._costo_base * horas

        # Aplicamos impuesto
        costo += costo * impuesto

        # Aplicamos descuento
        costo -= costo * descuento

        return costo

    # Método que describe el servicio
    def descripcion(self):

        return f"Reserva de sala: {self._nombre}"


# Clase concreta para alquiler de equipos
class AlquilerEquipo(Servicio):

    # Método sobrescrito para calcular costo
    def calcular_costo(self, dias, impuesto=0.0):

        # Validamos días válidos
        if dias <= 0:

            raise ErrorValidacion(
                "Los días deben ser mayores a 0"
            )

        # Calculamos costo total
        costo = self._costo_base * dias

        # Aplicamos impuesto
        costo += costo * impuesto

        return costo

    # Método que describe el servicio
    def descripcion(self):

        return f"Alquiler de equipo: {self._nombre}"


# Clase concreta para asesorías especializadas
class AsesoriaEspecializada(Servicio):

    # Método sobrescrito para calcular costo
    def calcular_costo(self, horas, tarifa_extra=0.0):

        # Validamos horas válidas
        if horas <= 0:

            raise ErrorValidacion(
                "Las horas deben ser mayores a 0"
            )

        # Calculamos costo total
        costo = (self._costo_base + tarifa_extra) * horas

        return costo

    # Método que describe el servicio
    def descripcion(self):

        return f"Asesoría especializada: {self._nombre}"
