# Sistema Integral de Gestión de Clientes, Servicios y Reservas (Software FJ)

Este proyecto corresponde al desarrollo práctico de la **Tarea 4** para el curso de **Programación de Sistemas** (UNAD 2026). Consiste en una aplicación de consola robusta escrita en Python que implementa los principios de la Programación Orientada a Objetos (POO), modularidad, validaciones estrictas y un sistema dinámico de logs para el control de eventos y errores.

---

## 👥 Desarrolladores
Este proyecto fue diseñado, desarrollado y unificado de forma colaborativa por:
* **Wilson Pedroza**
* **Weider Berbesi**
* **Andres Gomez**

---

## 🛠️ Estructura del Proyecto (Arquitectura Modular)

El proyecto está organizado bajo los estándares de desarrollo de software limpio, separando las responsabilidades de cada componente en directorios dedicados:

```text
Ejercicio 4/
│
├── excepciones/             # Excepciones personalizadas para el negocio
│   └── errores_personalizados.py
│
├── gestores/                # Controladores y lógica de administración
│   └── gestion_sistema.py
│
├── logs/                    # Archivos de registro generados en ejecución
│   ├── errores.log          # Registro exclusivo de fallos y excepciones
│   └── eventos.log          # Historial detallado de operaciones exitosas
│
├── modelos/                 # Clases base y objetos de negocio
│   ├── cliente.py
│   └── servicio.py
│
├── utils/                   # Herramientas de soporte y configuración
│   ├── config_log.py        # Configuración del sistema de logging
│   └── validaciones.py      # Filtros de formato (Email, Teléfono, etc.)
│
├── main.py                  # Punto de entrada y simulación (14 casos de prueba)
└── README.md                # Presentación de la entrega