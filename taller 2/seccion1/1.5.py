# Ejercicio 1.5 – Convertidor de unidades con menú


def run():
    print("Combertidor de unidades\n")
    while True:
        print("\nMenú:")
        print("1. Celsius a Fahrenheit")
        print("2. Kilómetros a Millas")
        print("3. Kilogramos a Libras")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            try:
                celsius = float(input("Ingrese grados Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
            except ValueError:
                print("Error: Ingrese un número válido.")
        
        elif opcion == "2":
            try:
                km = float(input("Ingrese kilómetros: "))
                millas = km * 0.621371
                print(f"{km:.2f} km = {millas:.2f} mi")
            except ValueError:
                print("Error: Ingrese un número válido.")
        
        elif opcion == "3":
            try:
                kg = float(input("Ingrese kilogramos: "))
                libras = kg * 2.20462
                print(f"{kg:.2f} kg = {libras:.2f} lb")
            except ValueError:
                print("Error: Ingrese un número válido.")
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    run()