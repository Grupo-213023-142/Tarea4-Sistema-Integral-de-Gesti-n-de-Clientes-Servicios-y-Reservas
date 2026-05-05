# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción del Proyecto

Este proyecto corresponde al desarrollo de un sistema integral orientado a objetos para la empresa ficticia **Software FJ**, el cual permite gestionar:

- Clientes
- Servicios
- Reservas

El sistema fue desarrollado en **Python**, aplicando los principios fundamentales de la **Programación Orientada a Objetos (POO)** y sin utilizar bases de datos, tal como lo establece la guía de la actividad.

Toda la información es administrada mediante:
- Objetos
- Listas
- Manejo de archivos
- Registro de logs

---

# Objetivo del Proyecto

Desarrollar una aplicación modular, estable y extensible que implemente:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones

garantizando el correcto funcionamiento del sistema incluso cuando ocurran errores durante la ejecución.

---

# Características Implementadas

## Programación Orientada a Objetos

El proyecto implementa:

- Clases abstractas
- Herencia
- Sobrescritura de métodos
- Encapsulación de atributos
- Polimorfismo

---

## Manejo de Excepciones

El sistema incorpora:

- Excepciones personalizadas
- Bloques `try/except`
- Bloques `try/except/else`
- Bloques `try/except/finally`
- Encadenamiento de excepciones

---

## Logging

El sistema registra automáticamente:

- Eventos importantes
- Reservas exitosas
- Cancelaciones
- Errores
- Excepciones

mediante archivos `.log`.

---

# Estructura del Proyecto

```plaintext
EJERCICIO_4/
│
├── excepciones/
│   └── errores_personalizados.py
│
├── gestores/
│   └── gestion_sistema.py
│
├── logs/
│   ├── errores.log
│   └── eventos.log
│
├── modelos/
│   ├── cliente.py
│   ├── entidad_abstracta.py
│   ├── reserva.py
│   └── servicio.py
│
├── utils/
│   ├── config_log.py
│   └── validadores.py
│
├── main.py
└── README.md