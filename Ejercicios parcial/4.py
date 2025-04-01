# 6. Crea un juego en el que el usuario debe adivinar un número secreto 
# (por ejemplo, 7). El programa debe seguir pidiendo intentos hasta 
# que el usuario acierte o ingrese "salir".
import random

def juego ():
    while True:
         try:
            ingreso= input("Adivina adivinador el número secresto del 1 al 10: ")
            numero_aleatorio = random.randint(1, 10)

            if ingreso == "salir":
                print("Gracias por jugar!")
                break
            elif int(ingreso)== numero_aleatorio:
                print ("felicidades ganaste el juego!")
                break
            else:
                print("lol, q mal vuelve a intentar")
                print(f"el numero secreto es {numero_aleatorio}")
         except ValueError:
            print("Entrada inválida. Debes ingresar un número del 1 al 10 o 'salir'.")

juego() 

        