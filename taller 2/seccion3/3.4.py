# Ejercicio 3.4 – Tabla de multiplicar interactiva

def run():
    print("Tabla de Multiplicar Interactiva\n")
    while True:
        try:
            num = int(input("¿De qué número desea ver la tabla de multiplicar? "))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
            continue
        
        print(f"\nTabla de multiplicar del {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
        
        # Preguntar si desea continuar
        respuesta = input("\n¿Desea ver otra tabla? (s/n): ").strip().lower()
        if respuesta != 's':
            print("Hasta luego")
            break
        print()  # Línea en blanco para separar

if __name__ == "__main__":
    run()