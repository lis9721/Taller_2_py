# 


def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        lista (list): Lista de números (enteros o flotantes)
    
    Returns:
        float or str: El promedio si la lista no está vacía, mensaje de error en caso contrario
    """
    if not lista:
        return "Error: La lista está vacía. No se puede calcular el promedio."
    
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

def run():
    print("=== CALCULADORA DE PROMEDIOS ===\n")
    
    # Ejemplo interactivo
    entrada = input("Ingrese números separados por comas: ").strip()
    try:
        numeros = [float(x.strip()) for x in entrada.split(",") if x.strip()]
    except ValueError:
        print("Error: Asegúrese de ingresar solo números válidos.")
        return
    
    resultado = calcular_promedio(numeros)
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"El promedio de {numeros} es: {resultado:.2f}")

if __name__ == "__main__":
    run()