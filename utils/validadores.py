# Funciones sencillas de validación

def validar_email(email):
    # Verificamos que el correo tenga un @
    return "@" in email

def validar_telefono(telefono):
    # Verificamos que el teléfono sea numérico
    return telefono.isdigit()
