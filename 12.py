#EL DE JULIANA
import random
import matplotlib.pyplot as plt # plt es una abreviacion para complicarse menos la vida

#Paso 1: Generar los pacientes aleatorios
while True:
    pacientes = []
    for i in range(10):
        paciente = {
            "ID":i,
            "FC":random.randint(50,130),
            "PA":random.randint(80,150)
        }
        pacientes.append(paciente)

    print(f"En este momento tienes un total de {len(pacientes)} pacientes")

    #Paso 2: Permitir agregar mas pacientes

    def entrada_int(mensaje, min, max):
        while True:
            try:
                valor = int(input(mensaje))
                if valor in range (min, max +1):
                    return valor
                else:
                    print(f"Los valores deben estar entre {min} y {max}")
            except ValueError as e:
                print("Porfavor ingrese un valor numerico")

    while True:
        continuar = input("¿Desea ingresar mas pacientes? s/n: ").lower().replace(" ","")

        if continuar in ["n","no"]:
            print("Finalizo ingreso de pacientes")
            break
        elif continuar in ["s","si"]:
            fc = entrada_int("Ingrese la frecuencia cardiaca: ", 50, 130)
            pa = entrada_int("Ingrese la presion arterial: ", 80, 150)
            pacientes.append({"ID":len(pacientes) , "FC":fc , "PA":pa})



    #Paso 3: función par aclasificar pacientes
    def clasificar_pacientes(frecuencia, presion):
        if (frecuencia not in range(60,101)) and (presion not in range(90,121)):
            return "critico", "Blue"
        elif (frecuencia not in range(60,101)) or (presion not in range(90,121)):
            return "riesgo", "Red"
        else:
            return "sano", "Green"
        
    #Paso 4: clasificar datos generados

    print("----------------Clasificacion de pacientes aleatorios------------")
    for paciente_clasificado in pacientes:
        estado,color = clasificar_pacientes(paciente_clasificado["FC"], paciente_clasificado["PA"])
        paciente_clasificado["estado"] = estado
        paciente_clasificado["color"] = color
        print(f"Paciente {paciente_clasificado['ID']} ---> Estado: {estado}")

    #paso 5: graficar en matplotlib

    fc_values = [paciente["FC"] for paciente in pacientes]
    pa_values = [paciente["PA"] for paciente in pacientes]  
    colores = [paciente["color"] for paciente in pacientes]

    plt.scatter(fc_values, pa_values, c=colores)  
    scatter = plt.scatter(fc_values, pa_values, c=colores, edgecolors='black')#edgecolors='black'-->  para que los circulitos tengan borde negro
    plt.xlabel("Frecuencia Cardíaca (LPM)") #lo que va en x
    plt.ylabel("Presión Arterial (mmHg)") #lo que va en y
    plt.title("CLASIFICACION DE PACIENTES")
    plt.show(block=False)#para que aparezca la pregunta que sigue



    while True:
        salida = input('¿Desea salir del programa? (s/n): ').strip().lower()
        if salida in ["s", "si"]:
            print("Finalizando programa...")
            break
        elif salida in ["n", "no"]:
            print("Reiniciando el proceso...\n")
            
            break
        else:
            print("Por favor responde con 's' o 'n'.")
    if salida in ["s", "si"]:
        break