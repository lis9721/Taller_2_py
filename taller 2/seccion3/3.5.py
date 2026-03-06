# Ejercicio 3.5 – Eliminador de duplicados en lista


def run():
    print("Eliminador de Duplicados en Lista\n")
    numeros = []
    
    # Ingreso de 10 números
    print("Ingrese 10 números (pueden repetirse):")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    
    # Eliminar duplicados manualmente (sin set)
    unicos = []
    for num in numeros:
        if num not in unicos:  # Verificamos si ya está en la lista de únicos
            unicos.append(num)
    
    print(f"\nLista original: {numeros}")
    print(f"Lista sin duplicados: {unicos}")

if __name__ == "__main__":
    run()
