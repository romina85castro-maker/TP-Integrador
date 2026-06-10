from funciones_validaciones import *
import csv
import requests
import questionary
import os

# ----------------------------------------------
# Funciones de utilidad:
def limpiar_pantalla():
    os.system("cls")

# ----------------------------------------------
# Funciones principales de menú:

def menu():
    limpiar_pantalla()

    print("""
==========================================
                M E N Ú 
==========================================""")
    return questionary.select(
        "Seleccione una opción:",
        choices=[
            "1 - Agregar País.",
            "2 - Actualizar Pais.",
            "3 - Buscar País.",
            "4 - Filtrar País.",
            "5 - Ordenar País.",
            "6 - Mostrar Estadísticas.",
            "7 - Salir."
        ]
    ).ask()


def agregar_pais(paises): #### MIA #####
    pass

encabezados = ["nombre", "poblacion", "superficie", "continente"]
def agregar_pais(paises):
    nombre = pedir_nombre_pais()
    if nombre is None:
        return
    
    if pais_existencia(nombre, paises):
        print("Ese país ya está cargado.")
        return
    
    poblacion = pedir_poblacion()
    if poblacion is None:
        return
    
    superficie = pedir_superficie()
    if superficie is None:
        return
    
    continente = pedir_continente()
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)

    with open("paises.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)


def actualizar_pais(paises): #### ROMI #####
    pass

def buscar_pais(paises): #### MIA #####
    pass

def filtrar_pais(paises):  #### ROMI #####
    pass

def ordenar_pais(paises): #### MIA #####
    pass

def mostrar_estadisticas(paises):  #### ROMI #####
    pass
