# Ejercicio 2.4 – Sistema de calificaciones con letras

def run():
    print("Conversor DE calificaciones\n")
    try:
        nota = float(input("Ingrese la nota (0-100): "))
        
        if nota < 0 or nota > 100:
            print("Error: La nota debe estar entre 0 y 100.")
        elif nota >= 90:
            print("Calificación: A")
        elif nota >= 80:
            print("Calificación: B")
        elif nota >= 70:
            print("Calificación: C")
        elif nota >= 60:
            print("Calificación: D")
        else:
            print("Calificación: F")
    except ValueError:
        print("Error: Debe ingresar un número.")

if __name__ == "__main__":
    run()
    
    