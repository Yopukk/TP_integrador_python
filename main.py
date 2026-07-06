
from estacionamiento import (
    ingresar_vehiculo,
    egresar_vehiculo,
    mostrar_espacios_disponibles,
    mostrar_estadisticas
)

vehiculos_estacionados = {}   # patente -> hora de ingreso
historial = []                # lista vehículos que ya egresaron


def mostrar_menu():
    print("\n===== SISTEMA DE ESTACIONAMIENTO =====")
    print("1. Ingresar vehículo")
    print("2. Registrar egreso de vehículo")
    print("3. Ver espacios disponibles")
    print("4. Ver estadísticas")
    print("5. Salir")


def leer_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("\n⚠ Debe ingresar un número válido.")
        return None


def main():
    opcion = None

    while opcion != 5:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            ingresar_vehiculo(vehiculos_estacionados)
        elif opcion == 2:
            egresar_vehiculo(vehiculos_estacionados, historial)
        elif opcion == 3:
            mostrar_espacios_disponibles(vehiculos_estacionados)
        elif opcion == 4:
            mostrar_estadisticas(historial)
        elif opcion == 5:
            print("\nGracias por usar el sistema. ¡Hasta luego!")
        elif opcion is not None:
            print("\n⚠ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
