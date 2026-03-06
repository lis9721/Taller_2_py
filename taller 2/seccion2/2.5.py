# Ejercicio 2.5 – Simulador de descuentos por categoría

def run():
    print("Simulador de Descuentos\n")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            return
        
        categoria = input("Ingrese la categoría (A, B, C u otra): ").strip().upper()
        
        if categoria == "A":
            descuento = 0.20
        elif categoria == "B":
            descuento = 0.15
        elif categoria == "C":
            descuento = 0.10
        else:
            descuento = 0.0
            print("Categoría sin descuento.")
        
        ahorro = precio * descuento
        total = precio - ahorro
        
        print(f"\nPrecio original: ${precio:.2f}")
        print(f"Descuento aplicado: {descuento*100:.0f}%")
        print(f"Ahorro: ${ahorro:.2f}")
        print(f"Total a pagar: ${total:.2f}")
        
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

if __name__ == "__main__":
    run()
