

"""
Sistema de gestión de biblioteca
Mini-taller integrador que aplica todos los conceptos:
- Listas de diccionarios
- Funciones
- Condicionales y ciclos
- Validaciones
- Menú interactivo
- Exportación a archivo de texto
"""

import os  # Para verificar existencia de archivo (opcional)


# ESTRUCTURA DE DATOS GLOBAL

# Lista de diccionarios que almacena todos los libros
biblioteca = []
# Variable para asignar IDs autoincrementales
proximo_id = 1


# FUNCIONES PRINCIPALES


def agregar_libro():
    """
    Permite registrar un nuevo libro.
    Solicita título, autor y año. Valida que el año sea numérico y mayor a 1900.
    Asigna un ID autoincremental y estado disponible por defecto (True).
    """
    global proximo_id
    print("\n--- AGREGAR NUEVO LIBRO ---")
    
    titulo = input("Título: ").strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return
    
    autor = input("Autor: ").strip()
    if not autor:
        print("El autor no puede estar vacío.")
        return
    
    # Validación de año
    try:
        año = int(input("Año de publicación: "))
        if año <= 1900:
            print("El año debe ser mayor a 1900.")
            return
    except ValueError:
        print("Debe ingresar un número entero válido para el año.")
        return
    
    # Crear diccionario del libro
    libro = {
        "id": proximo_id,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "disponible": True
    }
    biblioteca.append(libro)
    print(f"Libro agregado con ID {proximo_id}.")
    proximo_id += 1


def mostrar_libros():
    """
    Muestra todos los libros en formato legible.
    """
    print("\nLisado Completo de libros")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    for libro in biblioteca:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"  ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['año']}) [{estado}]")


def buscar_libro():
    """
    Busca libros por título o autor (coincidencia parcial, sin distinguir mayúsculas).
    Muestra los resultados encontrados.
    """
    print("\n--- BUSCAR LIBRO ---")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    criterio = input("Ingrese texto a buscar (título o autor): ").strip().lower()
    if not criterio:
        print("Debe ingresar algún texto de búsqueda.")
        return
    
    resultados = []
    for libro in biblioteca:
        if criterio in libro["titulo"].lower() or criterio in libro["autor"].lower():
            resultados.append(libro)
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} coincidencias:")
        for libro in resultados:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"  ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['año']}) [{estado}]")
    else:
        print("No se encontraron libros que coincidan con la búsqueda.")


def prestar_libro():
    """
    Cambia el estado de disponibilidad a False si el libro existe y está disponible.
    """
    print("\nPrestar Libro")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    try:
        id_libro = int(input("Ingrese el ID del libro a prestar: "))
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return
    
    for libro in biblioteca:
        if libro["id"] == id_libro:
            if libro["disponible"]:
                libro["disponible"] = False
                print(f"Libro '{libro['titulo']}' prestado correctamente.")
            else:
                print(f"El libro '{libro['titulo']}' ya está prestado.")
            return
    
    print(f"No se encontró un libro con ID {id_libro}.")


def devolver_libro():
    """
    Cambia el estado de disponibilidad a True si el libro existe y está prestado.
    """
    print("\n--- DEVOLVER LIBRO ---")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    try:
        id_libro = int(input("Ingrese el ID del libro a devolver: "))
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return
    
    for libro in biblioteca:
        if libro["id"] == id_libro:
            if not libro["disponible"]:
                libro["disponible"] = True
                print(f"Libro '{libro['titulo']}' devuelto correctamente.")
            else:
                print(f"El libro '{libro['titulo']}' ya estaba disponible (no estaba prestado).")
            return
    
    print(f"No se encontró un libro con ID {id_libro}.")


def eliminar_libro():
    """
    Elimina un libro solo si no está prestado actualmente.
    """
    print("\n--- ELIMINAR LIBRO ---")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    try:
        id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return
    
    for i, libro in enumerate(biblioteca):
        if libro["id"] == id_libro:
            if not libro["disponible"]:
                print(f"No se puede eliminar el libro '{libro['titulo']}' porque está prestado.")
                return
            # Eliminar el libro
            eliminado = biblioteca.pop(i)
            print(f"Libro '{eliminado['titulo']}' eliminado permanentemente.")
            return
    
    print(f"No se encontró un libro con ID {id_libro}.")


# FUNCIONES ADICIONALES DESAFIANTES


def libros_por_autor():
    """
    Lista todos los libros de un autor específico.
    """
    print("\n--- LIBROS POR AUTOR ---")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    autor_buscar = input("Ingrese el nombre del autor: ").strip().lower()
    if not autor_buscar:
        print("Debe ingresar un autor.")
        return
    
    encontrados = [libro for libro in biblioteca if autor_buscar in libro["autor"].lower()]
    
    if encontrados:
        print(f"\nLibros de '{autor_buscar.title()}' (coincidencia parcial):")
        for libro in encontrados:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"  ID: {libro['id']} - '{libro['titulo']}' ({libro['año']}) [{estado}]")
    else:
        print("No se encontraron libros de ese autor.")


def estadisticas():
    """
    Muestra estadísticas del sistema: total de libros, disponibles y prestados.
    """
    print("\nEstadisticas de la biblioteca")
    total = len(biblioteca)
    if total == 0:
        print("No hay libros en la biblioteca.")
        return
    
    disponibles = sum(1 for libro in biblioteca if libro["disponible"])
    prestados = total - disponibles
    
    print(f"  Total de libros: {total}")
    print(f"  Libros disponibles: {disponibles}")
    print(f"  Libros prestados: {prestados}")


def exportar_a_txt():
    """
    Guarda todos los libros en un archivo de texto llamado 'biblioteca.txt'.
    """
    print("\nEcportar Archivo")
    if not biblioteca:
        print("No hay libros para exportar.")
        return
    
    try:
        with open("biblioteca.txt", "w", encoding="utf-8") as archivo:
            archivo.write("=== CATÁLOGO DE LA BIBLIOTECA ===\n\n")
            for libro in biblioteca:
                estado = "Disponible" if libro["disponible"] else "Prestado"
                linea = f"ID: {libro['id']} | {libro['titulo']} | {libro['autor']} | {libro['año']} | {estado}\n"
                archivo.write(linea)
        print(f"Datos exportados correctamente a 'biblioteca.txt' ({len(biblioteca)} libros).")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu_principal():
    """
    Implementa un menú interactivo con todas las opciones.
    Se repite hasta que el usuario selecciona salir.
    """
    while True:
        print("\n" + "="*50)
        print("        SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("="*50)
        print("1. Agregar libro")
        print("2. Mostrar todos los libros")
        print("3. Buscar libro (por título o autor)")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Eliminar libro")
        print("7. Libros por autor")
        print("8. Estadísticas")
        print("9. Exportar a biblioteca.txt")
        print("0. Salir")
        print("-"*50)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            prestar_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            eliminar_libro()
        elif opcion == "7":
            libros_por_autor()
        elif opcion == "8":
            estadisticas()
        elif opcion == "9":
            exportar_a_txt()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")  # Pausa para ver resultados


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    menu_principal()