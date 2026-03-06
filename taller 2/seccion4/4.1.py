# Ejercicio 4.1 – Lista de compras


def run():
    print("=== LISTA DE COMPRAS ===\n")
    compras = []
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar lista")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ").strip()
            if producto:
                compras.append(producto)
                print(f"{producto}' agregado a la lista.")
            else:
                print("El nombre no puede estar vacío.")
        
        elif opcion == "2":
            if not compras:
                print("La lista está vacía. No hay nada que eliminar.")
                continue
            
            print("Productos actuales:")
            for i, prod in enumerate(compras, 1):
                print(f"{i}. {prod}")
            
            try:
                indice = int(input("Ingrese el número del producto a eliminar: ")) - 1
                if 0 <= indice < len(compras):
                    eliminado = compras.pop(indice)
                    print(f"{eliminado}' eliminado de la lista.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Debe ingresar un número.")
        
        elif opcion == "3":
            if not compras:
                print("La lista de compras está vacía.")
            else:
                print("\n Lista de compras:")
                for i, prod in enumerate(compras, 1):
                    print(f"  {i}. {prod}")
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    run()