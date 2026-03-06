#  Ejercicio 3.1: Generador de números pares


def run():
    print("Generador de Números Pares\n")
    try:
        N = int(input("Ingrese un número entero positivo: "))
        if N < 1:
            print("Por favor, ingrese un número mayor o igual a 1.")
            return
        
        print(f"Números pares del 1 al {N}:")
        for i in range(2, N+1, 2):  # Comienza en 2 y avanza de 2 en 2
            print(i, end=" ")
        print()  # Salto de línea al final
    except ValueError:
        print("Error: Debe ingresar un número entero.")

if __name__ == "__main__":
    run()