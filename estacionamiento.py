from datetime import datetime
import math

CAPACIDAD_MAXIMA = 20
TARIFA_POR_HORA = 500


def validar_patente(patente_ingresada):  #Valida que la patente tenga el formato correcto.
    patente = patente_ingresada.strip().upper()

    if len(patente) < 6 or len(patente) > 7:
        return None
    if not patente.isalnum():
        return None

    return patente


def ingresar_vehiculo(vehiculos_estacionados):  #Registra el ingreso del vehiculo y si hay espacio disponible.
    if len(vehiculos_estacionados) >= CAPACIDAD_MAXIMA:
        print("\n⚠ No hay espacios disponibles en este momento.")
        return

    patente_ingresada = input("Ingrese la patente del vehículo: ")
    patente = validar_patente(patente_ingresada)

    if patente is None:
        print("\n⚠ Patente inválida. Debe tener entre 6 y 7 caracteres alfanuméricos (ej: AB123CD).")
        return

    if patente in vehiculos_estacionados:
        print(f"\n⚠ El vehículo con patente {patente} ya se encuentra estacionado.")
        return

    vehiculos_estacionados[patente] = datetime.now()
    hora_texto = vehiculos_estacionados[patente].strftime("%H:%M:%S")
    print(f"\n✔ Ingreso registrado. Patente: {patente} - Hora: {hora_texto}")


def calcular_importe(tiempo_en_horas):  #Calcula el importe final.
    horas_a_cobrar = max(1, math.ceil(tiempo_en_horas))
    return horas_a_cobrar * TARIFA_POR_HORA


def egresar_vehiculo(vehiculos_estacionados, historial):  #Resgisto de salida de vehiculos y calcula el importe
    patente_ingresada = input("Ingrese la patente del vehículo que egresa: ")
    patente = validar_patente(patente_ingresada)

    if patente is None:
        print("\n⚠ Patente inválida.")
        return

    if patente not in vehiculos_estacionados:
        print(f"\n⚠ No se encontró un vehículo estacionado con la patente {patente}.")
        return

    hora_ingreso = vehiculos_estacionados[patente]
    hora_egreso = datetime.now()
    tiempo_transcurrido = hora_egreso - hora_ingreso
    tiempo_en_horas = tiempo_transcurrido.total_seconds() / 3600

    importe = calcular_importe(tiempo_en_horas)

    del vehiculos_estacionados[patente]
    historial.append({
        "patente": patente,
        "tiempo_horas": tiempo_en_horas,
        "importe": importe
    })

    print(f"\n✔ Egreso registrado. Patente: {patente}")
    print(f"  Tiempo de permanencia: {tiempo_en_horas:.2f} horas")
    print(f"  Importe a pagar: ${importe}")


def mostrar_espacios_disponibles(vehiculos_estacionados): #Muestra espacios disponibles y ocupados.
    ocupados = len(vehiculos_estacionados)
    disponibles = CAPACIDAD_MAXIMA - ocupados

    print(f"\n Espacios ocupados: {ocupados}/{CAPACIDAD_MAXIMA}")
    print(f" Espacios disponibles: {disponibles}")


def mostrar_estadisticas(historial): #uestra estadísticas: vehículos que ingresaron, tiempo promedio y ganancias totales.
    total_atendidos = len(historial)

    if total_atendidos == 0:
        print("\n Todavía no se registraron egresos de vehículos.")
        return

    suma_tiempos = 0
    suma_importes = 0

    for registro in historial:
        suma_tiempos += registro["tiempo_horas"]
        suma_importes += registro["importe"]

    tiempo_promedio = suma_tiempos / total_atendidos

    print("\n--- Estadísticas del estacionamiento ---")
    print(f" Vehículos atendidos: {total_atendidos}")
    print(f" Tiempo promedio de permanencia: {tiempo_promedio:.2f} horas")
    print(f" Recaudación total: ${suma_importes}")
