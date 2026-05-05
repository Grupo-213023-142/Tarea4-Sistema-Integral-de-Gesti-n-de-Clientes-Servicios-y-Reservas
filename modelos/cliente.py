# Importamos la clase base y las excepciones personalizadas
from modelos.entidad_abstracta import EntidadAbstracta
from excepciones.errores_personalizados import ErrorValidacion

# Clase Cliente que hereda de EntidadAbstracta
class Cliente(EntidadAbstracta):
    def __init__(self, id, nombre, email, telefono):
        # Inicializamos atributos básicos
        super().__init__(id)
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    def validar(self):
        # Validamos que el email tenga un @
        if "@" not in self._email:
            raise ErrorValidacion("El correo no es válido")
        # Validamos que el teléfono sea numérico
        if not self._telefono.isdigit():
            raise ErrorValidacion("El teléfono debe ser numérico")

    def __str__(self):
        # Representación sencilla del cliente
        return f"Cliente: {self._nombre}, Email: {self._email}"
