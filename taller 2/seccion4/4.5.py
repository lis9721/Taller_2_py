# Ejercicio 4.5 – Comparador avanzado de listas


def run():
    print("=== COMPARADOR DE LISTAS ===\n")
    
    def leer_lista(nombre):
        entrada = input(f"Ingrese los elementos de la {nombre} separados por comas: ").strip()
        # Usamos str para no limitar a números; pueden ser palabras
        items = [x.strip() for x in entrada.split(",") if x.strip()]
        return items
    
    lista1 = leer_lista("primera lista")
    lista2 = leer_lista("segunda lista")
    
    if not lista1 and not lista2:
        print("Ambas listas están vacías.")
        return
    
    # Calcular comunes (sin usar conjuntos)
    comunes = []
    for elem in lista1:
        if elem in lista2 and elem not in comunes:
            comunes.append(elem)
    
    # Únicos de lista1 (están en lista1 pero no en lista2)
    unicos1 = []
    for elem in lista1:
        if elem not in lista2 and elem not in unicos1:
            unicos1.append(elem)
    
    # Únicos de lista2 (están en lista2 pero no en lista1)
    unicos2 = []
    for elem in lista2:
        if elem not in lista1 and elem not in unicos2:
            unicos2.append(elem)
    
    print("\nRESULTADOS DE LA COMPARACIÓN:")
    print(f"  Lista 1: {lista1}")
    print(f"  Lista 2: {lista2}")
    print(f"  Elementos comunes: {comunes if comunes else '(ninguno)'}")
    print(f"  Únicos en lista 1: {unicos1 if unicos1 else '(ninguno)'}")
    print(f"  Únicos en lista 2: {unicos2 if unicos2 else '(ninguno)'}")

if __name__ == "__main__":
    run()

