import questionary
import unicodedata

# ------------------------------
# Validaciones de entrada.
# ------------------------------

def validar_campo_vacio(texto):
    if texto == "":
        raise ValueError("No puede dejar vacíos.")

def validar_positivo(numero):
    if numero <= 0:
        raise ValueError("Debe ingresar un número mayor a 0")
    return True

def validar_numero(numero):
    if not numero.isdigit():
        raise ValueError("Debe ingresar un número.")

def normalizar_texto(texto):
    texto = texto.lower()
    texto = ''.join(
        caracter for caracter in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caracter) != "Mn"
    )
    return texto

def busqueda_parcial(texto_buscado, texto_comparado):
    texto_buscado = normalizar_texto(texto_buscado)
    texto_comparado = normalizar_texto(texto_comparado)
    return texto_buscado in texto_comparado

# ------------------------------
# Validar y pedir datos.
# ------------------------------

def pedir_nombre_pais():
    while True:
        try:
            pais = input("Ingrese el nombre del país: ").strip().title()
            validar_campo_vacio(pais)
            return pais
        
        except ValueError as e:
            print(f"Error: {e}")

            reintentar = questionary.confirm(
                "¿Desea intentar nuevamente?"
            ).ask()
            if not reintentar:
                return None

def pedir_poblacion():
    while True:
        try:
            poblacion = input("Ingrese la población: ").strip()

            validar_numero(poblacion)
            poblacion = int(poblacion)
            validar_positivo(poblacion)
            return poblacion
        
        except ValueError as e:
            print(f"Error: {e}")

            reintentar = questionary.confirm(
                "¿Desea intentar nuevamente?"
            ).ask()

            if not reintentar:
                return None
            
def pedir_superficie():
    while True:
        try:
            superficie = input("Ingrese la superficie: ").strip()

            validar_numero(superficie)
            superficie = int(superficie)
            validar_positivo(superficie)
            return superficie
        
        except ValueError as e:
            print(f"Error: {e}")

            reintentar = questionary.confirm(
                "¿Desea intentar nuevamente?"
            ).ask()

            if not reintentar:
                return None

def pedir_continente():
    while True:
        try:
            continente = input("Ingrese el nombre del continente: ").strip().title()
            validar_campo_vacio(continente)
            return continente
        
        except ValueError as e:
            print(f"Error: {e}")

            reintentar = questionary.confirm(
                "¿Desea intentar nuevamente?"
            ).ask()
            if not reintentar:
                return None