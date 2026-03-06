# Ejercicio 2.1 – Clasificación de edades

def run():
    print("Clasificador De Edades\n")
    try:
        edad = int(input("Ingrese la edad: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        elif edad <= 12:
            print("Clasificación: NIÑO")
        elif edad <= 17:
            print("Clasificación: ADOLESCENTE")
        elif edad <= 64:
            print("Clasificación: ADULTO")
        else:
            print("Clasificación: ADULTO MAYOR")
    except ValueError:
        print("Error: Debe ingresar un número entero.")

if __name__ == "__main__":
    run()
    
    