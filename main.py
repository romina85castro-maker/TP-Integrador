import questionary

def menu():
    print("""
=================================
            M E N Ú 
=================================""")
    return questionary.select(
        "Seleccione una opción:",
        choices=[
            "1 - Agregar",
            "2 - Ver"

        ]
    ).ask()

menu()
