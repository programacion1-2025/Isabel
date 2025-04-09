positivos = []
negativos = []

numeros = {
    "positivos": positivos,
    "negativos": negativos
}

print(numeros)

#obtener
def obtener_num ():
    while True:
        try:
            num = int(input("ingresa un número entero (0 para salir) : "))
            return num
    
        except ValueError as e:
            print(f"el número de be ser entero:::: {e}")

def validar_num():
    while True:
        num = obtener_num()
        if num == 0:
            break
        if num > 0:
            #la lista numeros es una variable global que podríamos implementar aquí"
            numeros ["positivos"].append(num) #recuerda que append es para agregar números
        else:
            numeros ["negativos"].append(num)

#mostrar
def mostrar_num():
    validar_num ()
    print (f"positivos {len(numeros['positivos'])}")
    print (f"negativos{len(numeros['negativos'])}")


    

    
    #guardar lo que me devuelve una función en una variable y lo hacemos con el return de arriba
mostrar_num()
