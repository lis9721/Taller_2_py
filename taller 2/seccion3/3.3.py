# Ejercicio 3.3 – Búsqueda en lista de nombres


def run():
    print("Búsqueda en Listas de Nombres\n")
    # Lista de ejemplo
    nombres = ["Carlos", "Marío", "Pedro", "Luz", "Juan", "Sofía"]
    print("Lista de nombres:", nombres)
    
    nombre_buscar = input("Ingrese el nombre que desea buscar: ").strip()
    
    encontrado = False
    for i, nombre in enumerate(nombres):
        if nombre.lower() == nombre_buscar.lower():  # Comparación sin distinguir mayúsculas
            print(f" {nombre_buscar}' encontrado en la posición {i} (índice {i})")
            encontrado = True
            break  # Detenemos la búsqueda al encontrar el primero
    
    if not encontrado:
        print(f" {nombre_buscar}' no se encuentra en la lista.")

if __name__ == "__main__":
    run()