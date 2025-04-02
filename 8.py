#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles 
# impares desde el primero hasta el segundo.

def numeros():
    while True:
        try: 
            print("PARES E IMPARES ")

            numero_1 = int(input("Ingrese un número entero: "))
            numero_2 = int(input("Ingrese otro número entero mayor o igual que el primero: "))

            if numero_1 < 0 or numero_2 < 0:
                print("Ambos números deben ser positivos.")
                continue
            elif numero_2 < numero_1:
                print("El segundo número debe ser mayor o igual que el primero.")
                continue
            else:
               for i in range (numero_1, numero_2 + 1):
                   if i % 2 == 0:
                       print(f"{i} es par.")
                   else:    
                       print(f"{i} es impar.")
               break
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
numeros()