# Ejercicio 1.3 – Validación de correo electrónico

def run():
    print("=== VALIDADOR DE CORREO ELECTRÓNICO ===\n")
    correo = input("Ingrese su correo electrónico: ").strip()
    
    # Verificar que tenga @
    if "@" not in correo:
        print("Correo inválido: falta el símbolo '@'.")
        return
    
    # Separar local y dominio
    partes = correo.split("@")
    if len(partes) != 2:
        print("Correo inválido: debe tener exactamente un '@'.")
        return
    
    local, dominio = partes
    
    # Validar no tenga partes vacías
    if not local or not dominio:
        print("Correo inválido: no puede haber partes vacías antes o después de '@'.")
        return
    
    # Verificar que el dominio contenga un 'punto' y que no sea el primer o último carácter
    if "." not in dominio:
        print("Correo inválido: el dominio debe contener un punto (.).")
        return
    
    #  Verificar que el punto no esté al inicio o final del dominio
    if dominio.startswith(".") or dominio.endswith("."):
        print("Correo inválido: el punto no puede estar al inicio o final del dominio.")
        return
    
    # Verificar que despues del ultimo punto haya al menos un caracter
    partes_dominio = dominio.split(".")
    if len(partes_dominio[-1]) < 2:
        print("Correo inválido: el dominio de nivel superior debe tener al menos 2 caracteres.")
        return
    
    print("El correo es verdadero.")

if __name__ == "__main__":
    run()
    