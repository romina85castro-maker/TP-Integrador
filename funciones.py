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


def menu_actualizar_pais(): #### ROMI #####    

    print("""
==========================================
     M E N Ú ACTUALIZACION DE DATOS
==========================================""")
    return questionary.select(
        "Seleccione una opción:",
        choices=[
            "1 - Actualizar Poblacion de un País.",
            "2 - Actualizar Superficie de un Pais.",
            "3 - Actualizar Poblacion y Superficie de un País.",
            "4 - Salir."
        ]
    ).ask()

def actualizar_pais(paises):

    opcion= menu_actualizar_pais()
    opcion = int(opcion[0])
    
    if opcion == 1:
        
        nombre_pais = pedir_nombre_pais()

        if pais_existencia(nombre_pais, paises):

            posicion = posicion_pais (paises, nombre_pais)

            nueva_poblacion = pedir_poblacion()

            paises [posicion - 1]["poblacion"] = nueva_poblacion
            
            print("La poblacion se actualizo CORRECTAMENTE.")

        else:
            print("El Pais ingresado NO EXISTE")
    

    elif opcion == 2:
        
        nombre_pais = pedir_nombre_pais()

        if pais_existencia(nombre_pais, paises):

            posicion = posicion_pais (paises, nombre_pais)

            nueva_superficie = pedir_superficie()

            paises [posicion - 1]["superficie"] = nueva_superficie
            
            print("La superficie se actualizo CORRECTAMENTE.")

        else:
            print("El Pais ingresado NO EXISTE")

        
    elif opcion== 3:

        nombre_pais = pedir_nombre_pais()

        if pais_existencia(nombre_pais, paises):

            posicion = posicion_pais (paises, nombre_pais)

            nueva_poblacion = pedir_poblacion()
            nueva_superficie = pedir_superficie()

            paises [posicion - 1]["poblacion"] = nueva_poblacion
            paises [posicion - 1]["superficie"] = nueva_superficie
            
            print("La Poblacion y la Superficie se actualizo CORRECTAMENTE.")

        else:
            print("El Pais ingresado NO EXISTE")

    else:
        print(" Ha salido del Menu de Actualizacion de Poblacion y Superficie. GRACIAS")

def buscar_pais(paises):
    if not lista_vacia(paises):
        return
    
    pais_buscado = pedir_nombre_pais()
    if pais_buscado == None:
        return
    
    encontrados = []

    for pais in paises:
        if busqueda_parcial(pais_buscado, pais['nombre']):
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron países.")
    else:
        for pais in encontrados: 
            print(f"""
\nPais: {pais['nombre']}
Población: {pais['poblacion']} habitantes
Superficie: {pais['superficie']} km2
Continente: {pais['continente']}""")

def filtrar_pais(paises):  #### ROMI #####
    pass

def ordenar_pais(paises): #### MIA #####
    if not lista_vacia(paises):
        return
    elegir_criterio = questionary.select(
        "Ordenar paises por: ",
        choices= [
            "nombre",
            "poblacion",
            "superficie"
        ]
    ).ask()

    tipo_orden = questionary.select(
        "Elija tipo de orden: ",
        choices=[
            "Ascendente",
            "Descendente"
        ]
    ).ask()
    paises_ordenados = ordenamiento_burbuja(paises, elegir_criterio, tipo_orden)
    for pais in paises_ordenados:
        print(f"""
Pais: {pais['nombre']}
Población: {pais['poblacion']}
Superficie: {pais['superficie']}
Continente: {pais['continente']}""")

def mostrar_estadisticas(paises):  #### ROMI #####
    pass
