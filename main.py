# main.py

import logging
# 1. Inicializar la configuración de logs antes de cualquier otra cosa
from utils.config_log import configurar_logs
configurar_logs() 

# 2. Importar los gestores, servicios y excepciones
from gestores.gestion_sistema import GestorSistema
from modelos.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from excepciones.errores_personalizados import ErrorSistema

def ejecutar_prueba():
    print("=== Iniciando Sistema Integral de Gestión (Software FJ) ===")
    gestor = GestorSistema()

    try:
        # --- PRUEBA 1: Registrar un cliente ---
        print("\n[1] Registrando cliente...")
        cliente1 = gestor.registrar_cliente(
            id="101500", 
            nombre="Wilson Diaz", 
            email="wilson@unad.edu.co", 
            telefono="3123456789"
        )
        print(f"Cliente registrado con éxito: {cliente1.nombre}")

        # --- PRUEBA 2: Crear un servicio y una reserva ---
        print("\n[2] Creando una reserva de sala...")
        # Instanciamos un servicio de los que integraste en modelos.servicio
        servicio_sala = ReservaSala(
            id_servicio="S01", 
            nombre="Sala de Juntas B", 
            precio_base=50000.0, 
            capacidad=10
        )
        
        # El gestor crea la reserva
        reserva = gestor.crear_reserva(
            cliente=cliente1, 
            servicio=servicio_sala, 
            duracion=3 # 3 horas
        )
        print(f"Reserva confirmada. ID de la reserva: {getattr(reserva, 'id_reserva', 'Creada')}")

        # --- PRUEBA 3: Forzar un error controlado para probar excepciones ---
        print("\n[3] Probando control de excepciones (Registrar ID duplicado)...")
        gestor.registrar_cliente(
            id="101500", # Mismo ID para forzar el ErrorSistema
            nombre="Duplicado", 
            email="duplicado@unad.edu.co", 
            telefono="3000000000"
        )

    except ErrorSistema as err:
        print(f"Excepción controlada con éxito: {err}")
    except Exception as err:
        print(f"Ocurrió un error inesperado: {err}")

    # --- RESUMEN ---
    print("\n=== Resumen del Sistema ===")
    resumen = gestor.resumen_sistema()
    print(f"Clientes registrados: {resumen['clientes_registrados']}")
    print(f"Reservas activas: {resumen['reservas_registradas']}")

if __name__ == "__main__":
    ejecutar_prueba()