import random
import matplotlib.pyplot as plt

#paso 1: generar pacientes aleatorios 
while True:
    pacientes = []
    for i in range(10):
        paciente = {
            'Id':i ,
            'FC':random.randint(50, 130),
            "PA":random.randint(80, 150)
        }
        pacientes.append(paciente)

    print(f"Hasta el momento cuenta con {len(pacientes)} pacientes")


    #paso 4: permitar agregar mas pacientes 
    def entrada_int(mensaje , min , max): 
        while True:
            try:
                valor = int(input(mensaje))
                if valor in range (min, max + 1):
                    return valor
                else:
                    print(f"Por favor ingrese un valor entre {min} y {max}")
            except ValueError:
                print("Por favor ingrese un valor numerico entero")

    while True: 

        continuar = input("Desea agregar un paciente? (si/no): ").lower().strip()
        if continuar in ['no', 'n']:
            print ("finalizo el programa")
            break
        elif continuar in ['si', 's']:
            fc = entrada_int("Ingrese la frecuencia cardiaca: ", 50, 130)
            Pa = entrada_int("Ingrese la presion arterial: ", 80, 150)
            pacientes.append({'Id': len(pacientes), 'FC': fc, "PA": Pa})
            print("Paciente agregado con exito!")
        else:
            print("Por favor ingrese una opcion valida")

    #paso 2:funcion para clasificar pacientes

    def clasificar_pacientes(frecuencia,presion):
        if (frecuencia not in range(60,101)) and (presion not in range(90,121)):
            return "Critico", "Red"
        elif (frecuencia not in range (60,101)) or (presion not in range (90,121)):
            return "Riesgo", "Orange"
        else:
            return "Sano", "Green"

    #paso 3: clasificar datos agregados

    print("------------Clasificacion Pacientes aleatorios------------")

    for paciente_clasificado in pacientes:
        estado, color = clasificar_pacientes(paciente_clasificado ["FC"], paciente_clasificado ["PA"])
        paciente_clasificado["estado"] = estado
        paciente_clasificado["color"] = color
        print(f"Paciente {paciente_clasificado ['Id']} --> estado {estado}")

    #paso 5: graficar datos con Matploit/

    # Extraer valores de Frecuencia Cardíaca y Presión Arterial del diccionario y ponerlos en su propia lista
    fc_values = [paciente['FC'] for paciente in pacientes]
    pa_values = [paciente['PA'] for paciente in pacientes]  
    color_real = [paciente['color'] for paciente in pacientes]


    plt.scatter(fc_values, pa_values, c=color_real, edgecolors='black')  
    plt.xlabel("Frecuencia Cardíaca (LPM)")
    plt.ylabel("Presión Arterial (mmHg)")
    plt.title("Pacientes - Gráfico de Dispersión")
    plt.show(block=False) 

    salida = input("desea salir del programa? (si/no): ").lower().strip()
    if salida == "si":
        print("Gracias por usar el programa")
    break