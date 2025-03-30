# 2. Escribe un programa que permita al usuario ingresar números y clasifique 
# cada uno como par o impar hasta que ingrese "0" para salir.
def clasificar():
    while True:
        try:
            numero=int(input("ingresa un numero:"))
            if numero == 0:
                print("saliendo del programa...")
                break
            elif numero %2 == 0:
                print("el número es par")
            elif numero % 2 != 0:
                print("el número es impar")
            else:
                print("porfa ingresa un número que sea válido")
        except ValueError:
            print("Error 404. ingrese un número entero, no palabras")
clasificar()



