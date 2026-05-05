
#Módulo que contiene la clase abstracta base
#para todas las entidades del sistema.

#Curso: Programación
#Universidad Nacional Abierta y a Distancia - UNAD


# Importamos herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# Clase abstracta que servirá como base
# para todas las entidades del sistema
class EntidadAbstracta(ABC):

    # Constructor de la clase
    def __init__(self, id):

        # Atributo encapsulado para almacenar el ID
        self._id = id

    # Método abstracto que obliga a las clases hijas
    # a implementar su propia validación
    @abstractmethod
    def validar(self):
        pass

    # Método que retorna una representación en texto
    def __str__(self):

        return f"Entidad ID: {self._id}"
