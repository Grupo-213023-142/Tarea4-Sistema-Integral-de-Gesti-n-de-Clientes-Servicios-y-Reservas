"""
Archivo principal de ejecución del Sistema Integral de Gestión de Clientes,
Servicios y Reservas para Software FJ.

Este archivo simula operaciones válidas e inválidas para demostrar:
- Programación orientada a objetos.
- Manejo de excepciones.
- Validaciones.
- Gestión de clientes, servicios y reservas.
- Registro de eventos y errores en archivos de logs.
"""

import logging
import os

from excepciones.errores_personalizados import ErrorSistema
from gestores.gestion_sistema import GestorSistema
from modelos.cliente import Cliente
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)


def configurar_logs():
    """
    Configura los archivos de logs del sistema.

    Se crean dos archivos:
    - logs/eventos.log: registra eventos generales del sistema.
    - logs/errores.log: registra errores y excepciones.

    Se usa logging porque permite dejar evidencia de lo ocurrido durante
    la ejecución sin depender únicamente de mensajes en pantalla.
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Limpia handlers previos para evitar duplicación de mensajes si se ejecuta varias veces.
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    manejador_eventos = logging.FileHandler(
        "logs/eventos.log",
        mode="w",
        encoding="utf-8"
    )
    manejador_eventos.setLevel(logging.INFO)
    manejador_eventos.setFormatter(formato)

    manejador_errores = logging.FileHandler(
        "logs/errores.log",
        mode="w",
        encoding="utf-8"
    )
    manejador_errores.setLevel(logging.ERROR)
    manejador_errores.setFormatter(formato)

    logger.addHandler(manejador_eventos)
    logger.addHandler(manejador_errores)


def ejecutar_caso(numero, descripcion, accion, debe_fallar=False):
    """
    Ejecuta un caso de simulación de forma controlada.

    Args:
        numero: Número del caso ejecutado.
        descripcion: Descripción breve del caso.
        accion: Función que contiene la operación a ejecutar.
        debe_fallar: Indica si el caso está diseñado para generar error.

    Returns:
        dict: Resultado de la ejecución del caso.

    Esta función permite que el sistema continúe ejecutándose aunque una
    operación falle. Esa es precisamente la idea del manejo robusto de
    excepciones: controlar el error y seguir con el proceso.
    """

    print(f"\nCaso {numero}: {descripcion}")

    try:
        resultado = accion()

    except Exception as error:
        logging.error(f"Caso {numero} - {descripcion}: {error}")

        if debe_fallar:
            print(f"Error controlado esperado: {error}")
            return {
                "caso": numero,
                "descripcion": descripcion,
                "resultado": "OK - Error controlado"
            }

        print(f"Fallo inesperado: {error}")
        return {
            "caso": numero,
            "descripcion": descripcion,
            "resultado": "FALLO - Error inesperado"
        }

    else:
        if debe_fallar:
            print("Fallo: el caso debía generar error, pero fue exitoso.")
            return {
                "caso": numero,
                "descripcion": descripcion,
                "resultado": "FALLO - Se esperaba error"
            }

        print(f"Operación exitosa: {resultado}")
        logging.info(f"Caso {numero} ejecutado correctamente: {descripcion}")

        return {
            "caso": numero,
            "descripcion": descripcion,
            "resultado": "OK - Operación exitosa"
        }

    finally:
        logging.info(f"Caso {numero} finalizado.")


def main():
    """
    Ejecuta la simulación principal del sistema.

    Se realizan operaciones válidas e inválidas para comprobar que el
    programa mantiene su estabilidad y registra los errores sin detener
    toda la ejecución.
    """

    configurar_logs()

    print("Sistema Integral de Gestión - Software FJ")
    print("Inicio de simulación de operaciones")

    gestor = GestorSistema()
    contexto = {}
    resultados = []

    resultados.append(
        ejecutar_caso(
            1,
            "Registrar cliente válido",
            lambda: registrar_cliente_valido(gestor, contexto)
        )
    )

    resultados.append(
        ejecutar_caso(
            2,
            "Registrar cliente con correo inválido",
            lambda: gestor.registrar_cliente(
                2,
                "Pedro Ramírez",
                "correo_invalido",
                "3014567890"
            ),
            debe_fallar=True
        )
    )

    resultados.append(
        ejecutar_caso(
            3,
            "Registrar cliente con teléfono inválido",
            lambda: gestor.registrar_cliente(
                3,
                "Laura Gómez",
                "laura@correo.com",
                "telefono"
            ),
            debe_fallar=True
        )
    )

    resultados.append(
        ejecutar_caso(
            4,
            "Registrar cliente duplicado",
            lambda: gestor.registrar_cliente(
                1,
                "Ana Torres Duplicada",
                "ana2@correo.com",
                "3009999999"
            ),
            debe_fallar=True
        )
    )

    resultados.append(
        ejecutar_caso(
            5,
            "Crear servicio de reserva de sala válido",
            lambda: crear_servicio_sala(contexto)
        )
    )

    resultados.append(
        ejecutar_caso(
            6,
            "Crear servicio con costo negativo",
            lambda: ReservaSala("Sala inválida", -50000),
            debe_fallar=True
        )
    )

    resultados.append(
        ejecutar_caso(
            7,
            "Crear servicio de alquiler de equipo válido",
            lambda: crear_servicio_equipo(contexto)
        )
    )

    resultados.append(
        ejecutar_caso(
            8,
            "Crear servicio de asesoría especializada válido",
            lambda: crear_servicio_asesoria(contexto)
        )
    )

    resultados.append(
        ejecutar_caso(
            9,
            "Crear reserva exitosa de sala",
            lambda: crear_reserva_exitosa(gestor, contexto)
        )
    )

    resultados.append(
        ejecutar_caso(
            10,
            "Crear reserva con cliente no registrado",
            lambda: crear_reserva_cliente_no_registrado(gestor, contexto),
            debe_fallar=True
        )
    )

    resultados.append(
        ejecutar_caso(
            11,
            "Cancelar reserva válida",
            lambda: cancelar_reserva_valida(gestor, contexto)
        )
    )

    resultados.append(
        ejecutar_caso(
            12,
            "Cancelar reserva ya cancelada",
            lambda: gestor.cancelar_reserva(contexto["reserva_sala"]),
            debe_fallar=True
        )
    )

    resultados.append(
        ejecutar_caso(
            13,
            "Intentar reservar servicio no disponible",
            lambda: crear_reserva_servicio_no_disponible(gestor, contexto),
            debe_fallar=True
        )
    )

    resultados.append(
        ejecutar_caso(
            14,
            "Mostrar resumen final del sistema",
            lambda: gestor.resumen_sistema()
        )
    )

    print("\nResumen de ejecución")
    print("-" * 60)

    for resultado in resultados:
        print(
            f"Caso {resultado['caso']}: "
            f"{resultado['descripcion']} -> "
            f"{resultado['resultado']}"
        )

    print("-" * 60)
    print("Simulación finalizada.")
    print("Revise los archivos logs/eventos.log y logs/errores.log.")


def registrar_cliente_valido(gestor, contexto):
    """
    Registra un cliente válido y lo almacena en el contexto para usarlo
    en operaciones posteriores.
    """

    cliente = gestor.registrar_cliente(
        1,
        "Ana Torres",
        "ana@correo.com",
        "3001234567"
    )

    contexto["cliente_principal"] = cliente
    return cliente


def crear_servicio_sala(contexto):
    """
    Crea un servicio válido de reserva de sala.
    """

    servicio = ReservaSala(
        "Sala Ejecutiva",
        50000
    )

    contexto["servicio_sala"] = servicio
    return servicio.descripcion()


def crear_servicio_equipo(contexto):
    """
    Crea un servicio válido de alquiler de equipo.
    """

    servicio = AlquilerEquipo(
        "Portátil empresarial",
        80000
    )

    contexto["servicio_equipo"] = servicio
    return servicio.descripcion()


def crear_servicio_asesoria(contexto):
    """
    Crea un servicio válido de asesoría especializada.
    """

    servicio = AsesoriaEspecializada(
        "Asesoría en arquitectura de software",
        120000
    )

    contexto["servicio_asesoria"] = servicio
    return servicio.descripcion()


def crear_reserva_exitosa(gestor, contexto):
    """
    Crea una reserva válida usando el cliente principal y el servicio de sala.
    """

    reserva = gestor.crear_reserva(
        contexto["cliente_principal"],
        contexto["servicio_sala"],
        2
    )

    contexto["reserva_sala"] = reserva
    return f"Reserva creada con estado: {reserva.estado}"


def crear_reserva_cliente_no_registrado(gestor, contexto):
    """
    Intenta crear una reserva con un cliente válido, pero no registrado
    dentro del gestor del sistema.
    """

    cliente_no_registrado = Cliente(
        99,
        "Carlos Externo",
        "carlos@correo.com",
        "3022222222"
    )

    return gestor.crear_reserva(
        cliente_no_registrado,
        contexto["servicio_equipo"],
        1
    )


def cancelar_reserva_valida(gestor, contexto):
    """
    Cancela una reserva previamente confirmada.
    """

    reserva = gestor.cancelar_reserva(
        contexto["reserva_sala"]
    )

    return f"Reserva cancelada con estado: {reserva.estado}"


def crear_reserva_servicio_no_disponible(gestor, contexto):
    """
    Intenta crear una reserva sobre un servicio marcado como no disponible.
    """

    servicio_no_disponible = ReservaSala(
        "Sala en mantenimiento",
        60000
    )

    servicio_no_disponible.cambiar_disponibilidad(False)

    return gestor.crear_reserva(
        contexto["cliente_principal"],
        servicio_no_disponible,
        1
    )


if __name__ == "__main__":
    try:
        main()

    except ErrorSistema as error:
        logging.error(f"Error general del sistema: {error}")
        print(f"Error general del sistema: {error}")

    except Exception as error:
        logging.error(f"Error inesperado en la ejecución principal: {error}")
        print(f"Error inesperado en la ejecución principal: {error}")
        