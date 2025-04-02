#Escriba un programa que pida un número entero mayor que cero y calcule su factorial.

def factorial():
    while True:
        try:
            numero = int(input("Ingrese un número entero mayor que cero: "))
            if numero <= 0:
                print("El número debe ser mayor que cero.")
                continue
            else:
                factorial = 1
                for i in range(1, numero + 1):
                    factorial *= i
                print(f"El factorial de {numero} es: {factorial}")
                break
        except ValueError:  
            print("Entrada inválida. Intente de nuevo.")
factorial()