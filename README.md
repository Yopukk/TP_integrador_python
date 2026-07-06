# Sistema de Gestión de Estacionamiento

Trabajo Final Python - escesario 6

## Integrantes
- Gauna Ezequiel Andres
- 
- 

## Descripción

Sistema por consola para gestionar el funcionamiento de un estacionamiento.

Permite: Registrar el ingreso y egreso de vehiculos calculando el tiempo que pertenecen dentro del estacionamiento, podes consultar los espacios disponibles o ocupados y por ultimo ver las estadisticas total de vehiculos atendidos, permanencia y ganancias totales.


## Estructura del proyecto

```
estacionamiento/
├── main.py              
├── estacionamiento.py   
└── README.md
```

## Reglas del sistema

- Capacidad máxima: 20 vehículos (`CAPACIDAD_MAXIMA` en `estacionamiento.py`).
- Tarifa: $500 por hora, cobrando la hora en curso completa
  (`TARIFA_POR_HORA` en `estacionamiento.py`).
- La patente debe tener entre 6 y 7 caracteres alfanuméricos.

## Conceptos aplicados

- Estructuras condicionales y repetitivas.
- Funciones y modularización (separación en módulo `estacionamiento.py`).
- Validaciones (patente, opción de menú, capacidad, patente duplicada/inexistente).
- Acumuladores y contadores (recaudación total, cantidad de vehículos atendidos).
- Manejo básico de errores (`try/except` en la lectura de opciones del menú).
