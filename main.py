# Programa principal:
import os
from funciones import *

if os.path.exists("paises.csv"):
    paises = cargar_csv()
else:
    paises = carga_inicial_paises()
    guardar_csv(paises)

if __name__ == "__main__":

    while True:
        opcion = menu()
        opcion = opcion[0]
        
        match opcion:

            case "1":
                agregar_pais(paises)

            case "2":
                actualizar_pais(paises)

            case "3":
                buscar_pais(paises)

            case "4":
                filtrar_pais(paises)

            case "5":
                ordenar_pais(paises)

            case "6":
                mostrar_estadisticas(paises)

            case "7":
                print("Saliendo del sistema... ¡Hasta pronto!")
                break
