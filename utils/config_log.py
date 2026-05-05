# Configuración básica de logs
import logging

# Configuramos el sistema de logs para que guarde en archivos y muestre en consola
logging.basicConfig(
    level=logging.INFO,   # Nivel de detalle (INFO muestra eventos normales y errores)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato de cada línea
    handlers=[
        logging.FileHandler("logs/eventos.log"),   # Archivo para eventos normales
        logging.FileHandler("logs/errores.log"),   # Archivo para errores
        logging.StreamHandler()                    # También mostrar en consola
    ]
)
