from funciones_validaciones import *
import csv
import questionary
import os

# ----------------------------------------------
# Funciones de utilidad:
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def volver_al_menu():
    input("\nPresione Enter para continuar...")

def guardar_csv(paises):
    ruta = os.path.join(os.path.dirname(__file__), "paises.csv")

    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)  

def cargar_csv():
    paises = []
    try:
        ruta = os.path.join(os.path.dirname(__file__), "paises.csv")

        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": float(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
    except FileNotFoundError:
        print("El archivo paises.csv no existe. Se comenzará con una lista vacía.")
    return paises

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
        volver_al_menu()
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
    
    guardar_csv(paises)
    print("El país se cargó con éxito.")
    volver_al_menu()

def menu_actualizar_pais():  
    print("""
==========================================
            ACTUALIZACION DE DATOS
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

    if lista_vacia(paises):
        print("No hay paises cargados.")
        volver_al_menu()
        return

    opcion= menu_actualizar_pais()
    opcion = int(opcion[0])
    
    if opcion == 1:
        nombre_pais = pedir_nombre_pais()

        if nombre_pais is None:
            return

        if pais_existencia(nombre_pais, paises):
            posicion = posicion_pais (paises, nombre_pais)
            nueva_poblacion = pedir_poblacion()

            if nueva_poblacion is None:
                return

            paises [posicion]["poblacion"] = nueva_poblacion        
            print("La poblacion se actualizo CORRECTAMENTE.")
            volver_al_menu()

        else:
            print("El Pais ingresado NO EXISTE")
            volver_al_menu()

    elif opcion == 2:
        nombre_pais = pedir_nombre_pais()

        if nombre_pais is None:
            return

        if pais_existencia(nombre_pais, paises):

            posicion = posicion_pais(paises, nombre_pais)
            nueva_superficie = pedir_superficie()

            if nueva_superficie is None:
                return

            paises [posicion]["superficie"] = nueva_superficie
            print("La superficie se actualizo CORRECTAMENTE.")
            volver_al_menu()

        else:
            print("El Pais ingresado NO EXISTE")
            volver_al_menu()
        
    elif opcion== 3:
        nombre_pais = pedir_nombre_pais()

        if nombre_pais is None:
            return

        if pais_existencia(nombre_pais, paises):
            posicion = posicion_pais (paises, nombre_pais)
            nueva_poblacion = pedir_poblacion()
            if nueva_poblacion is None:
                return

            nueva_superficie = pedir_superficie()
            if nueva_superficie is None:
                return

            paises [posicion]["poblacion"] = nueva_poblacion
            paises [posicion]["superficie"] = nueva_superficie
            print("La Poblacion y la Superficie se actualizaron CORRECTAMENTE.")
            volver_al_menu()

        else:
            print("El Pais ingresado NO EXISTE")
            volver_al_menu()

    else:
        print(" Ha salido del Menu de Actualizacion de Poblacion y Superficie.")
        volver_al_menu()
    guardar_csv(paises)
    
def buscar_pais(paises):
    if lista_vacia(paises):
        print("No hay paises cargados.")
        volver_al_menu()
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
    volver_al_menu()

def menu_filtrar_pais():
    print("""
==========================================
            FILTRAR PAISES POR: 
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

def filtrar_pais(paises):

    if lista_vacia(paises):
        print("No hay paises cargados.")
        volver_al_menu()
        return

    opcion= menu_filtrar_pais()
    opcion = int(opcion[0])

    if opcion == 1:
        filtrar_continente(paises)

    elif opcion== 2:
        filtrar_poblacion(paises)

    elif opcion== 3:
        filtrar_superficie(paises)
    volver_al_menu()

def ordenar_pais(paises): 
    if lista_vacia(paises):
        print("No hay paises cargados.")
        volver_al_menu()
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
    volver_al_menu()

def mostrar_estadisticas(paises): 

    if lista_vacia(paises):
        print("No hay paises cargados.")
        volver_al_menu()
        return

    poblacion_mayor = mayor_poblacion(paises)
    poblacion_menor = menor_poblacion(paises)
    poblacion_promedio = promedio_poblacion(paises)
    superficie_promedio = promedio_superficie(paises)
    cantidad_x_continente = cantidad_por_continente(paises)
    

    print("""
===========================================
                ESTADÍSTICAS
===========================================
""")
    print("LA MAYOR POBLACION ESTA EN EL PAIS DE: ", poblacion_mayor)
    print("LA MENOR POBLACION ESTA EN EL PAIS DE: ", poblacion_menor)
    print("EL PROMEDIO DE POBLACION A NIVEL MUNDIAL ES: ", poblacion_promedio)
    print("EL PROMEDIO DE SUPERFICIE A NIVEL MUNDIAL ES: ", superficie_promedio)
    
    print("""
=========================================
    CANTIDAD DE PAÍSES POR CONTINENTE
=========================================
""")

    print(f"Africa: ", cantidad_x_continente["África"])
    print(f"América: ", cantidad_x_continente["América"])
    print(f"Asia: ", cantidad_x_continente["Asia"])
    print(f"Europa: ", cantidad_x_continente["Europa"])
    print(f"Oceanía: ", cantidad_x_continente ["Oceanía"])
    print(f"Antártida: ", cantidad_x_continente["Antártida"])

    volver_al_menu()

# -------------------------------------------
# Carga inicial de paises
def carga_inicial_paises():
    return [
        {
            "nombre": "Argentina",
            "poblacion": 45376763,
            "superficie": 2780400,
            "continente": "América"
        },
        {
            "nombre": "Japón",
            "poblacion": 125800000,
            "superficie": 377975,
            "continente": "Asia"
        },
        {
            "nombre": "Brasil",
            "poblacion": 213993437,
            "superficie": 8515767,
            "continente": "América"
        },
        {
            "nombre": "Alemania",
            "poblacion": 83149300,
            "superficie": 357022,
            "continente": "Europa"
        }
    ]