# 4. Crea una lista de temperaturas en grados Celsius y calcula el promedio, 
# la temperatura máxima y la mínima usando for.

def promedio ():
    temperaturas = []
    while True:
        entrada = input("ingrese temepraturas en grados celcius, con punto para decimales si así desea y calcular el promedio / fin para salir del sistema:")
        if entrada == "fin":
            print(" Ha salido del sistema con éxito!.....")
            break
        try:
            temperatura = float(entrada)
            temperaturas.append(temperatura)
        except ValueError:
            print("ingrese numeros, no letras")
        for temperatura in temperaturas:
            promedio = sum(temperaturas)/len (temperaturas)
            mayor = max(temperaturas)
            menor= min(temperaturas)
        if len(temperaturas)== 0:
            print(" no se ingresaron temperaturas al sistema")
        else:
            print(f"el promedio de las temperaturas es {promedio}")
            print(f"la temperatura mayor es {mayor}")
            print(f"la temperatura menor es {menor}")
promedio ()
           

