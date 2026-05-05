# Módulo encargado de configurar los logs del sistema.


# Importamos librería logging
import logging

# Creamos logger principal
logger = logging.getLogger()

# Configuramos nivel general
logger.setLevel(logging.INFO)

# Formato de logs
formato = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# Handler para eventos normales
eventos_handler = logging.FileHandler(
    "logs/eventos.log"
)

# Nivel INFO para eventos
eventos_handler.setLevel(logging.INFO)

# Aplicamos formato
eventos_handler.setFormatter(formato)

# Handler para errores
errores_handler = logging.FileHandler(
    "logs/errores.log"
)

# Nivel ERROR para errores
errores_handler.setLevel(logging.ERROR)

# Aplicamos formato
errores_handler.setFormatter(formato)

# Handler para consola
console_handler = logging.StreamHandler()

# Aplicamos formato
console_handler.setFormatter(formato)

# Agregamos handlers al logger
logger.addHandler(eventos_handler)
logger.addHandler(errores_handler)
logger.addHandler(console_handler)