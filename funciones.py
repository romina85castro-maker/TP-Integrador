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


def menu_filtrar_pais(): ###ROMI####

    print("""
==========================================
     MENÚ: FILTRAR PAISES POR: 
==========================================""")
    return questionary.select(
        "Seleccione una opción:",
        choices=[
            "1 - CONTINENTE.",
            "2 - RANGO DE POBLACION.",
            "3 - RANGO DE SUPERFICIE.",
            "4 - SALIR."
        ]
    ).ask()

def filtrar_pais(paises):  #### ROMI #####    

    opcion= menu_filtrar_pais()
    opcion = int(opcion[0])

    if opcion == 1:

        filtrar_continente(paises)

    elif opcion== 2:

        filtrar_poblacion(paises)
        
    elif opcion== 3:
        
        filtrar_superficie(paises)

    else:
        print(" Ha salido del MENÚ FILTRAR PAISES. GRACIAS")
        

def ordenar_pais(paises): #### MIA #####
    pass

def mostrar_estadisticas(paises):  #### ROMI #####

    mayor_poblacion = mayor_poblacion(paises)
    menor_poblacion = menor_poblacion(paises)
    promedio_poblacion = promedio_poblacion(paises)
    promedio_superficie = promedio_superficie(paises)
    cantidad_por_continente = cantidad_por_continente(paises)
    

    print("""
=========================================
    ---------ESTADISTICAS----------------
=========================================
""")
    print("LA MAYOR POBLACION ESTA EN EL PAIS DE: ", mayor_poblacion)
    print("LA MENOR POBLACION ESTA EN EL PAIS DE: ", menor_poblacion)
    print("EL PROMEDIO DE PROBLACION A NIVEL MUNDIAR ES: ", promedio_poblacion)
    print("EL PROMEDIO DE SUPERFICIE A NIVEL MUNDIAR ES: ", promedio_superficie)
    
    print("""
=========================================
    CANTIDAD DE PAÍSES POR CONTINENTE
=========================================
""")

print(f"África: ", cantidad_por_continente["África"])
print(f"América: ", cantidad_por_continente["América"])
print(f"Asia: ", cantidad_por_continente["Asia"])
print(f"Europa: ", cantidad_por_continente["Europa"])
print(f"Oceanía: ", cantidad_por_continente ["Oceanía"])
print(f"Antártida: ", cantidad_por_continente["Antártida"])

