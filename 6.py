# 8. Escribe un programa donde el usuario juegue contra la computadora en un 
# juego de piedra, papel o tijera. El programa debe seguir ejecutándose 
# hasta que el usuario escriba "salir". Consulta el uso del módulo random

import random

def juego():
    while True:
        usuario= input("Ingresa piedra, papel o tijeras / salir : ").strip().lower()
        computadora = random.choice(["piedra","papel","tijera"])
        
        if usuario == "salir" :
            print("Gracias por jugar...")
            break
        
        elif usuario == computadora:
            print("Empate!ambos eligieron {usuario} ")
        
        elif usuario == "piedra":
            if computadora == "papel" :
                print("Jaja, perdiste")
        
        elif usuario == "papel" :
            if computadora == "piedra" :
                print(" Haz ganado!")
        
        elif usuario == "tijera" :
            if computadora == "piedra":
                print("JAJA, perdiste")
        
        elif usuario == "tijera":
            if computadora == "papel":
                print("Wow haz ganado")
        
        else:
            print("entrada invalida: solo puede ingresa piedra papel o tijera")

juego()




