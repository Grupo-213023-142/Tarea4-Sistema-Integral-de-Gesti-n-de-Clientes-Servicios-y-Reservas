"""
Módulo encargado de gestionar los clientes del sistema Software FJ.

Incluye validaciones robustas, encapsulación de datos y herencia desde
la clase abstracta EntidadAbstracta.
"""

from modelos.entidad_abstracta import EntidadAbstracta
from excepciones.errores_personalizados import ErrorValidacion
from utils.validadores import validar_email, validar_telefono


class Cliente(EntidadAbstracta):
    """
    Representa un cliente dentro del sistema.

    La clase encapsula los datos principales del cliente y valida que
    la información ingresada sea consistente antes de permitir su uso
    en procesos de reserva.
    """

    def __init__(self, id, nombre, email, telefono):
        super().__init__(id)

        self._nombre = nombre
        self._email = email
        self._telefono = telefono

        # Se valida desde la creación del objeto para evitar clientes inválidos.
        self.validar()

    @property
    def id(self):
        """Retorna el identificador del cliente."""
        return self._id

    @property
    def nombre(self):
        """Retorna el nombre del cliente."""
        return self._nombre

    @property
    def email(self):
        """Retorna el correo electrónico del cliente."""
        return self._email

    @property
    def telefono(self):
        """Retorna el número telefónico del cliente."""
        return self._telefono

    def validar(self):
        """
        Valida los datos principales del cliente.

        Raises:
            ErrorValidacion: Cuando algún dato del cliente no cumple
            con las reglas mínimas requeridas por el sistema.
        """

        if self._id is None or str(self._id).strip() == "":
            raise ErrorValidacion("El ID del cliente no puede estar vacío.")

        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ErrorValidacion("El nombre del cliente no puede estar vacío.")

        if len(self._nombre.strip()) < 3:
            raise ErrorValidacion("El nombre del cliente debe tener al menos 3 caracteres.")

        if not isinstance(self._email, str) or not self._email.strip():
            raise ErrorValidacion("El correo electrónico no puede estar vacío.")

        if not validar_email(self._email):
            raise ErrorValidacion("Correo electrónico inválido.")

        if not isinstance(self._telefono, str) or not self._telefono.strip():
            raise ErrorValidacion("El teléfono no puede estar vacío.")

        if not validar_telefono(self._telefono):
            raise ErrorValidacion("Teléfono inválido.")

        return True

    def __str__(self):
        return f"Cliente: {self._nombre} - {self._email}"

    def __repr__(self):
        return f"Cliente(id={self._id}, nombre='{self._nombre}')"