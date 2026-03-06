# Ejercicio 4.3 – Gestor de inventario

def run():
    print("Gestor de Inventario\n")
    inventario = []  # Lista de diccionarios
    
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Actualizar precio")
        print("3. Mostrar inventario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            # Verificar si ya existe
            if any(p["nombre"].lower() == nombre.lower() for p in inventario):
                print(f"El producto '{nombre}' ya existe. Use actualizar para modificar.")
                continue
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))
                if precio < 0 or stock < 0:
                    print("Precio y stock deben ser no negativos.")
                    continue
                inventario.append({
                    "nombre": nombre,
                    "precio": precio,
                    "stock": stock
                })
                print(f"Producto '{nombre}' agregado.")
            except ValueError:
                print("Precio debe ser número y stock entero.")
        
        elif opcion == "2":
            if not inventario:
                print("El inventario está vacío.")
                continue
            nombre = input("Ingrese el nombre del producto a actualizar precio: ").strip()
            producto_encontrado = None
            for producto in inventario:
                if producto["nombre"].lower() == nombre.lower():
                    producto_encontrado = producto
                    break
            if producto_encontrado:
                try:
                    nuevo_precio = float(input(f"Nuevo precio para '{nombre}': "))
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        producto_encontrado["precio"] = nuevo_precio
                        print(f"Precio actualizado a {nuevo_precio:.2f}.")
                except ValueError:
                    print("Debe ingresar un número.")
            else:
                print(f"Producto '{nombre}' no encontrado.")
        
        elif opcion == "3":
            if not inventario:
                print("El inventario está vacío.")
            else:
                print("\nINVENTARIO:")
                for p in inventario:
                    print(f"  - {p['nombre']}: ${p['precio']:.2f} | Stock: {p['stock']}")
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    run()
    