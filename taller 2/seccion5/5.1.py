# Ejercicio 5.1 – Generador de saludos personalizados


def saludar(nombre, hora):
    """
    Genera un saludo personalizado basado en la hora.
    
    Args:
        nombre (str): Nombre de la persona a saludar
        hora (int): Hora del día (0-23)
    
    Returns:
        str: Saludo completo
    """
    if 5 <= hora <= 12:
        saludo = "Buenos días"
    elif 13 <= hora <= 19:
        saludo = "Buenas tardes"
    else:  # 20-4
        saludo = "Buenas noches"
    
    return f"{saludo}, {nombre}!"

def run():
    print("Generador de Saludos Personalizado\n")
    nombre = input("Ingrese su nombre: ").strip()
    
    while True:
        try:
            hora = int(input("Ingrese la hora actual (0-23): "))
            if 0 <= hora <= 23:
                break
            else:
                print("La hora debe estar entre 0 y 23.")
        except ValueError:
            print("Error: Ingrese un número entero.")
    
    print(saludar(nombre, hora))

if __name__ == "__main__":
    run()