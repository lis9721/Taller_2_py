# Ejercicio 1.1 – Registro de usuario

def run():
    print("Registro de usuario\n")
    nombre = input("Ingrese su nombre: ").strip()
    ciudad = input("Ingrese su ciudad: ").strip()
    
    # Validación de la edad
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad > 0:
                break
            else:
                print("La edad debe ser un número positivo. Intentelo otra vez.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número que sea entero.")
    
    # Imprimir el mensaje
    print(f"\nHola {nombre}, tienes {edad} años y vives en {ciudad}.")

if __name__ == "__main__":
    run()
    
    
    
    
    
    
    