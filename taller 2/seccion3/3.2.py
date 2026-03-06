# Ejercicio 3.2 – Acumulador numérico
  
def run():
    print("Acumulador Númerico\n")
    suma = 0
    contador = 0
    while True:
        try:
            numero = float(input(f"Ingrese un número (0 para terminar): "))
            if numero == 0:
                break
            suma += numero
            contador += 1
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    
    if contador == 0:
        print("No se ingresaron números para sumar.")
    else:
        print(f"\nSe ingresaron {contador} números.")
        print(f"La suma total es: {suma}")

if __name__ == "__main__":
    run()
    
    