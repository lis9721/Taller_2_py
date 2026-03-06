# Ejercicio 5.4 – Detector de palíndromos

"""
Ejercicio 5.4: Detector de palíndromos
Función es_palindromo(texto) que ignora espacios, mayúsculas/minúsculas y signos de puntuación.
"""

import re

def es_palindromo(texto):
    """
    Determina si un texto es un palíndromo (se lee igual al derecho y al revés),
    ignorando espacios, signos de puntuación y diferencias de mayúsculas/minúsculas.
    
    Args:
        texto (str): El texto a evaluar
    
    Returns:
        bool: True si es palíndromo, False en caso contrario
    """
    # Convertir a minúsculas y eliminar caracteres no alfanuméricos
    texto_limpio = re.sub(r'[^a-z0-9]', '', texto.lower())
    # Comparar con su reverso
    return texto_limpio == texto_limpio[::-1]

def run():
    print("=== DETECTOR DE PALÍNDROMOS ===\n")
    frase = input("Ingrese una palabra o frase: ").strip()
    
    if es_palindromo(frase):
        print(f"✅ '{frase}' SÍ es un palíndromo.")
    else:
        print(f"❌ '{frase}' NO es un palíndromo.")

if __name__ == "__main__":
    run()