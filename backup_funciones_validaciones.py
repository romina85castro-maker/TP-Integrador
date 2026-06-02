# ------------------------------
# Validaciones de entrada.
# ------------------------------

def validar_campo_vacio(texto):
    if texto != "":
        return True
    return False

import questionary

def menu():
    print("""
=================================
            M E N Ú 
=================================""")
    return questionary.select(
        "Seleccione una opción:",
        choices=[
            "1 - Agregar Pais",
            "2 - Actualizar Pais",
            "3 - Buscar Pais",
            "4 - Filtrar Paises",
            "5 - Ordenar Paises",
            "6 - Mostrar Estadisticas",
            "7 - Salir"

        ]
    ).ask()