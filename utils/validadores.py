# Módulo que contiene funciones auxiliares de validación.


# Importamos expresiones regulares
import re


# Función para validar correos electrónicos
def validar_email(email):

    # Patrón de validación
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Retornamos si el correo cumple el patrón
    return re.match(patron, email)


# Función para validar teléfonos
def validar_telefono(telefono):

    # Verificamos si el teléfono es numérico
    return telefono.isdigit()