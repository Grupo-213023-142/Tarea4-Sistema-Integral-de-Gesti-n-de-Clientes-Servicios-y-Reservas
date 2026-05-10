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

# Función para validar nombres
def validar_nombre(nombre):

    # Verificamos que no esté vacío
    return len(nombre.strip()) > 0


# Función para validar documentos
def validar_documento(documento):

    # Verificamos que sea numérico
    return documento.isdigit()


# Función para validar duración
def validar_duracion(duracion):

    # Verificamos que sea mayor a cero
    return duracion > 0


# Función para validar precios
def validar_precio(precio):

    # Verificamos que el precio sea válido
    return precio > 0