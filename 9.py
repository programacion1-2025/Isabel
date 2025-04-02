#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor, el menor y la media aritmética.
# Se recuerda que la media aritmética de un conjunto de valores es la suma de esos valores dividida por la cantidad de valores.

def mayor_menor_media():
    while True:
        try:
            cantidad = int(input("¿Cuántos números deseas introducir? "))
            if cantidad < 1:
                print("Debes introducir al menos un número.")
            else:
                break
        except ValueError:
            print("Debes introducir un número entero.")

    mayor = 0
    menor = 0
    suma = 0 
    for i in range (cantidad):
        while True:
            try:
                numero = float(input(f"Introduce un número: "))
                if i == 0:
                    mayor = numero
                    menor = numero
                else:
                    if numero > mayor:
                        mayor = numero
                    elif numero < menor:
                        menor = numero
                suma += numero
                break
            except ValueError:  
                print("Debes introducir un número.")
    media = round (suma / cantidad, 2)
    print(f"El número mayor es: {mayor}. El número menor es: {menor}. La media aritmética es: {media}", end="")
mayor_menor_media()   