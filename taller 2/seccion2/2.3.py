# Ejercicio 2.3 – Calculadora con menú mejorado 

def run():
    print("Calculadora Con Menú Mejorado\n")
    while True:
        print("\nMenú de las operaciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Debe ingresar números válidos.")
                continue
            
            if opcion == "1":
                print(f"{num1} + {num2} = {num1 + num2}")
            elif opcion == "2":
                print(f"{num1} - {num2} = {num1 - num2}")
            elif opcion == "3":
                print(f"{num1} * {num2} = {num1 * num2}")
            elif opcion == "4":
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    run()

