# Importamos librerías necesarias
from abc import ABC, abstractmethod

# Clase abstracta que servirá como base para todas las entidades
class EntidadAbstracta(ABC):
    def __init__(self, id):
        # Guardamos el identificador de la entidad
        self._id = id

    @abstractmethod
    def validar(self):
        # Método abstracto que cada clase hija debe implementar
        pass

    def __str__(self):
        # Representación sencilla de la entidad
        return f"Entidad con id: {self._id}"
