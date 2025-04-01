# 7. Crea un programa que pida al usuario una contraseña y siga pidiéndola hasta que cumpla con estos requisitos:
# Debe tener al menos 8 caracteres.
# Debe contener al menos un número.
# Debe contener al menos una letra mayúscula.

def contraseña ():
    while True:
        try:
            contraseña= input ("Ingrese una contraseña con al menos un número, al menos 8 caracteres y al menos una letra en mayúscula")
            if contraseña len(palabras) < 8:
            print("La contraseña debe tener 8 caracteres")

            elif not any(letra.isdigit() for letra in contraseña):
            print("la contraseña debe tener la menos 1 letra")

            elif any (letra.issuper() for letra in contraseña):
            print("la ocntraseña debe tener al menos una letra en Mayusucula")
            
            else:
            print("contraseña inválida")
            break
        except Exception as e:
        print(f"Error inesperado: {e}")

contraseña ()



    





