"""
Módulo encargado de definir los servicios ofrecidos por Software FJ.

Incluye una clase abstracta Servicio y tres servicios especializados:
reserva de salas, alquiler de equipos y asesorías especializadas.
Se aplican principios de abstracción, herencia, polimorfismo,
sobrescritura de métodos y validaciones de costos.
"""

from abc import ABC, abstractmethod
from excepciones.errores_personalizados import ErrorValidacion


class Servicio(ABC):
    """
    Clase abstracta base para todos los servicios del sistema.

    Cada servicio debe implementar su propio cálculo de costo y su
    descripción, permitiendo aplicar polimorfismo.
    """

    def __init__(self, nombre, costo_base):
        self._nombre = nombre
        self._costo_base = costo_base
        self._disponible = True
        self._validar_datos_base()

    @property
    def nombre(self):
        """Retorna el nombre del servicio."""
        return self._nombre

    @property
    def costo_base(self):
        """Retorna el costo base del servicio."""
        return self._costo_base

    @property
    def disponible(self):
        """Indica si el servicio está disponible."""
        return self._disponible

    def cambiar_disponibilidad(self, disponible):
        """
        Cambia el estado de disponibilidad del servicio.

        Args:
            disponible: Valor booleano que indica disponibilidad.
        """

        if not isinstance(disponible, bool):
            raise ErrorValidacion("La disponibilidad debe ser un valor booleano.")

        self._disponible = disponible

    def _validar_datos_base(self):
        """
        Valida los datos comunes de todos los servicios.

        Raises:
            ErrorValidacion: Si el nombre o el costo base son inválidos.
        """

        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ErrorValidacion("El nombre del servicio no puede estar vacío.")

        if not isinstance(self._costo_base, (int, float)):
            raise ErrorValidacion("El costo base del servicio debe ser numérico.")

        if self._costo_base <= 0:
            raise ErrorValidacion("El costo base del servicio debe ser mayor a cero.")

    def _validar_numero_positivo(self, valor, nombre_campo):
        """
        Valida que un valor sea numérico y mayor a cero.
        """

        if not isinstance(valor, (int, float)):
            raise ErrorValidacion(f"{nombre_campo} debe ser un valor numérico.")

        if valor <= 0:
            raise ErrorValidacion(f"{nombre_campo} debe ser mayor a cero.")

    def _validar_porcentaje(self, valor, nombre_campo):
        """
        Valida porcentajes expresados entre 0 y 1.
        """

        if not isinstance(valor, (int, float)):
            raise ErrorValidacion(f"{nombre_campo} debe ser un valor numérico.")

        if valor < 0 or valor > 1:
            raise ErrorValidacion(f"{nombre_campo} debe estar entre 0 y 1.")

    @abstractmethod
    def calcular_costo(self, **kwargs):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def descripcion(self):
        """Retorna la descripción del servicio."""
        pass

    def __str__(self):
        return f"{self.descripcion()} - Costo base: {self._costo_base}"


class ReservaSala(Servicio):
    """
    Servicio especializado para reserva de salas.
    """

    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        """
        Calcula el costo de reservar una sala.

        Args:
            horas: Número de horas de reserva.
            impuesto: Porcentaje de impuesto entre 0 y 1.
            descuento: Porcentaje de descuento entre 0 y 1.
        """

        self._validar_numero_positivo(horas, "Las horas")
        self._validar_porcentaje(impuesto, "El impuesto")
        self._validar_porcentaje(descuento, "El descuento")

        costo = self._costo_base * horas
        costo += costo * impuesto
        costo -= costo * descuento

        if costo <= 0:
            raise ErrorValidacion("El costo final de la reserva de sala no puede ser menor o igual a cero.")

        return costo

    def descripcion(self):
        return f"Reserva de sala: {self._nombre}"


class AlquilerEquipo(Servicio):
    """
    Servicio especializado para alquiler de equipos.
    """

    def calcular_costo(self, dias, impuesto=0.0):
        """
        Calcula el costo del alquiler de un equipo.

        Args:
            dias: Cantidad de días de alquiler.
            impuesto: Porcentaje de impuesto entre 0 y 1.
        """

        self._validar_numero_positivo(dias, "Los días")
        self._validar_porcentaje(impuesto, "El impuesto")

        costo = self._costo_base * dias
        costo += costo * impuesto

        return costo

    def descripcion(self):
        return f"Alquiler de equipo: {self._nombre}"


class AsesoriaEspecializada(Servicio):
    """
    Servicio especializado para asesorías.
    """

    def calcular_costo(self, horas, tarifa_extra=0.0):
        """
        Calcula el costo de una asesoría especializada.

        Args:
            horas: Número de horas de asesoría.
            tarifa_extra: Valor adicional aplicado por hora.
        """

        self._validar_numero_positivo(horas, "Las horas")

        if not isinstance(tarifa_extra, (int, float)):
            raise ErrorValidacion("La tarifa extra debe ser numérica.")

        if tarifa_extra < 0:
            raise ErrorValidacion("La tarifa extra no puede ser negativa.")

        costo = (self._costo_base + tarifa_extra) * horas

        return costo

    def descripcion(self):
        return f"Asesoría especializada: {self._nombre}"