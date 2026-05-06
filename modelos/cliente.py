#Módulo encargado de gestionar los clientes del sistema.

#Incluye validaciones y encapsulación de datos.


# Importamos la clase abstracta base
from modelos.entidad_abstracta import EntidadAbstracta

# Importamos excepción personalizada
from excepciones.errores_personalizados import ErrorValidacion

# Importamos funciones de validación
from utils.validadores import validar_email, validar_telefono


# Clase Cliente que hereda de EntidadAbstracta
class Cliente(EntidadAbstracta):

    # Constructor de la clase
    def __init__(self, id, nombre, email, telefono):

        # Inicializamos atributos heredados
        super().__init__(id)

        # Atributos encapsulados del cliente
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    # Método property para acceder al nombre
    @property
    def nombre(self):

        return self._nombre

    # Método encargado de validar datos del cliente
    def validar(self):

        # Verificamos que el correo sea válido
        if not validar_email(self._email):

            raise ErrorValidacion(
                "Correo electrónico inválido"
            )

        # Verificamos que el teléfono sea numérico
        if not validar_telefono(self._telefono):

            raise ErrorValidacion(
                "Teléfono inválido"
            )

    # Método que retorna información del cliente
    def __str__(self):

        return f"Cliente: {self._nombre} - {self._email}"

    # Método usado para representar el objeto
    def __repr__(self):

        return f"Cliente({self._id}, {self._nombre})"