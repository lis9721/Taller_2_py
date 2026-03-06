# Ejercicio 5.5 – Factorial recursivo


def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    Args:
        n (int): Número entero no negativo
    
    Returns:
        int: El factorial de n, o un mensaje de error si n es negativo
    """
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def run():
    print("=== FACTORIAL RECURSIVO ===\n")
    try:
        num = int(input("Ingrese un número entero no negativo: "))
        resultado = factorial(num)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"El factorial de {num} es: {resultado}")
    except ValueError:
        print("Error: Debe ingresar un número entero.")

if __name__ == "__main__":
    run()