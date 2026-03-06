# Ejercicio 2.2 – Menú de opciones básico

def run():
    print("Menú Basico\n")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ").strip()
    
    if opcion == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opcion == "2":
        print("¡Hasta luego! Que tengas un buen día.")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    run()
