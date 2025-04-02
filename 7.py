# 9. Genera una lista de 100 números aleatorios entre 1 y 100 y calcula el número más frecuente.

import random 

def frecuencia():
    lista = [random.randint(1, 100) for i in range(100)]
    frecuencia = {}
    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1

    max_frecuencia = 0
    numero_max_frec = None

    for numero, repeticiones in frecuencia.items():
        if repeticiones > max_frecuencia:
            max_frecuencia = repeticiones
            numero_max_frec = numero
    print(f"El número más frecuente es {numero_max_frec} y aparece {max_frecuencia} veces.")
frecuencia()