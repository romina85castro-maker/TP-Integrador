# ------------------------------
# Validaciones de entrada.
# ------------------------------

def validar_campo_vacio(texto):
    if texto != "":
        return True
    return False

def validar_positivo(numero):
    if numero > 0:
        return True
    return False

def validar_numero(numero):
    if numero.isdigit():
        pass
    