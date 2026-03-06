# Ejercicio 1.2 – Calculadora básica

def run():
    print("=== CALCULADORA BÁSICA ===\n")
    
    # Entrada de los numeros
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Debe ingresar números que sean válidos.")
        return
    
    operacion = input("Ingrese la operación que desea ejecutar (+, -, *, /): ").strip()
    
    # Operaciones
    if operacion == "+":
        resultado = num1 + num2
        print(f"\n{num1} + {num2} = {resultado}")
    elif operacion == "-":
        resultado = num1 - num2
        print(f"\n{num1} - {num2} = {resultado}")
    elif operacion == "*":
        resultado = num1 * num2
        print(f"\n{num1} * {num2} = {resultado}")
    elif operacion == "/":
        if num2 == 0:
            print("\nError: No se puede dividir por cero.")
        else:
            resultado = num1 / num2
            print(f"\n{num1} / {num2} = {resultado}")
    else:
        print("\nOperación no válida.")

if __name__ == "__main__":
    run()