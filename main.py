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

paises = [
    {
        "nombre":"Argentina",
        "poblacion": "45376763",
        "superficie": "2780400",
        "continente": "America"
    },
    {
        "nombre":"Japon",
        "poblacion": "125800000",
        "superficie": "377975",
        "continente": "Asia"
    },
    {
        "nombre":"Brasil",
        "poblacion": "213993437",
        "superficie": "8515767",
        "continente": "America"
    },
    {
        "nombre":"Alemania",
        "poblacion": "83149300",
        "superficie": "357022",
        "continente": "Europa"
    }
]

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
