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

def agregar_pais(paises):
    pass

def actualizar_pais(paises):
    pass

def buscar_pais(paises):
    pass

def filtrar_pais(paises):
    pass

def ordenar_pais(paises):
    pass

def mostrar_estadisticas(paises):
    pass
