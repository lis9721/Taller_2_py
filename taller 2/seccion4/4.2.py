# Ejercicio 4.2 – Directorio de contactos



def run():
    print("Directorio de Contactos\n")
    contactos = {}
    
    while True:
        print("\nMenú de Contactos:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ").strip()
            if nombre in contactos:
                print(f"El contacto '{nombre}' ya existe. Use otra opción para modificarlo.")
                continue
            telefono = input("Ingrese el teléfono: ").strip()
            if nombre and telefono:
                contactos[nombre] = telefono
                print(f"Contacto '{nombre}' agregado.")
            else:
                print("Nombre y teléfono no pueden estar vacíos.")
        
        elif opcion == "2":
            if not contactos:
                print("El directorio está vacío.")
                continue
            nombre = input("Ingrese el nombre del contacto a buscar: ").strip()
            if nombre in contactos:
                print(f"{nombre}: {contactos[nombre]}")
            else:
                print(f"No se encontró el contacto '{nombre}'.")
        
        elif opcion == "3":
            if not contactos:
                print("El directorio está vacío.")
                continue
            nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print(f"No se encontró el contacto '{nombre}'.")
        
        elif opcion == "4":
            if not contactos:
                print("El directorio está vacío.")
            else:
                print("\nLista de contactos:")
                for nombre, telefono in contactos.items():
                    print(f"  {nombre}: {telefono}")
        
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    run()
    
    