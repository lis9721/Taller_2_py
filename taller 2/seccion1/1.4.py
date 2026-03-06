# Ejercicio 1.4 – Validador de contraseña segura


def run():
    print("Validador De Contraseña Segura\n")
    password = input("Ingrese una contraseña: ")
    
    criterios = {
        "longitud": len(password) >= 8,
        "mayuscula": any(c.isupper() for c in password),
        "numero": any(c.isdigit() for c in password),
        "especial": any(c in "!@#$%^&*" for c in password)
    }
    
    # Mostrar resultados
    if all(criterios.values()):
        print("La contraseña es segura.")
    else:
        print("La contraseña no cumple con los siguientes criterios:")
        if not criterios["longitud"]:
            print("  - Debe tener al menos 8 caracteres.")
        if not criterios["mayuscula"]:
            print("  - Debe contener al menos una letra mayúscula.")
        if not criterios["numero"]:
            print("  - Debe contener al menos un número.")
        if not criterios["especial"]:
            print("  - Debe contener al menos un carácter especial (!@#$%^&*).")

if __name__ == "__main__":
    run()
    
    