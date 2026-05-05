# Importamos librerías necesarias
from abc import ABC, abstractmethod

# Clase abstracta Servicio
class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self._nombre = nombre
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        # Método abstracto para calcular costo
        pass

    @abstractmethod
    def descripcion(self):
        # Método abstracto para describir el servicio
        pass

# Clase concreta: Reserva de Sala
class ReservaSala(Servicio):
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        # Calculamos costo con horas, impuestos y descuentos
        costo = self._costo_base * horas
        costo += costo * impuesto
        costo -= costo * descuento
        return costo

    def descripcion(self):
        return f"Reserva de sala: {self._nombre}"

# Clase concreta: Alquiler de Equipo
class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, impuesto=0.0):
        # Costo según días de alquiler
        costo = self._costo_base * dias
        costo += costo * impuesto
        return costo

    def descripcion(self):
        return f"Alquiler de equipo: {self._nombre}"

# Clase concreta: Asesoría Especializada
class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas, tarifa_extra=0.0):
        # Costo según horas más tarifa extra
        costo = (self._costo_base + tarifa_extra) * horas
        return costo

    def descripcion(self):
        return f"Asesoría especializada: {self._nombre}"
