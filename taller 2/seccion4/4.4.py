# Ejercicio 4.4 – Analizador estadístico


def run():
    print("Analizador Estadistico\n")
    entrada = input("Ingrese números separados por comas: ").strip()
    
    # Convertir a lista de números
    try:
        numeros = [float(x.strip()) for x in entrada.split(",") if x.strip()]
    except ValueError:
        print("❌ Error: Asegúrese de ingresar solo números separados por comas.")
        return
    
    if not numeros:
        print("No se ingresaron números válidos.")
        return
    
    # Calcular estadísticas
    suma = sum(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    promedio = suma / len(numeros)
    
    print(f"\nResultados:")
    print(f"  Números ingresados: {numeros}")
    print(f"  Cantidad: {len(numeros)}")
    print(f"  Suma: {suma:.2f}")
    print(f"  Máximo: {maximo:.2f}")
    print(f"  Mínimo: {minimo:.2f}")
    print(f"  Promedio: {promedio:.2f}")

if __name__ == "__main__":
    run()