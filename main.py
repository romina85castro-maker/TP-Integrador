# Programa principal:

from funciones import (
    menu,
    agregar_pais,
    actualizar_pais,
    buscar_pais,
    filtrar_pais,
    ordenar_pais,
    mostrar_estadisticas
)

paises = []

if __name__ == "__main__":

    while True:
        opcion = menu()
        opcion = opcion[0]
        
        match opcion:

            case "1":
                agregar_pais(paises)

            case "2":
                actualizar_pais()

            case "3":
                buscar_pais(paises)

            case "4":
                filtrar_pais()

            case "5":
                ordenar_pais(paises)

            case "6":
                mostrar_estadisticas()

            case "7":
                print("Saliendo del sistema... ¡Hasta pronto!")
                break
