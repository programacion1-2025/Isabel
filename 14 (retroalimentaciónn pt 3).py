def es_contraseña_valida(contraseña):
    # trabajaremos con la lógica de verdad y falso
    #diremos al incio que todo está mal
    tiene_8_caracteres = False
    tiene_2_num= False
    tiene_1_mayus = False
    completo = False #esto evalua un vacío que ingresa el usuario, es decir que voy a evaluar si no el usuario no ha ingresado nada

    if len(contraseña) >= 8:    # porque len (contraseña)? l
        tiene_8_caracteres = True
    #contraseña podemos evaluarla como una lista si usamos for
    contador = 0
    for c in contraseña:
        #python nos permite evaluar patrones eso es lo que estamos haciendo
        if  "0"<= c <= "9":
            contador = contador + 1
            # se usa un contador porque
            if contador >= 2:
                tiene_2_num = True
        if "A" <= c <= "Z":
            tiene_1_mayus = True
            #hacer identanción)?
    
    if contraseña:
        #evaluar si contraseña no está vacía
        completo = True
    if  tiene_8_caracteres and tiene_2_num and tiene_1_mayus and completo:
        return True, ["contraseña válida"] # el mensaje será una lista porque yo espero respuesta en forma de lista
    #si yo no pongo return más abajo se me rompe el código, si acá devolvemos algo allá en el bloque de código debe ser igual
    else:
        errores = []
        if not tiene_8_caracteres:
            mensaje = "debe tener 8 caracteres"
            errores.append("debe tener 8 caracteres")
        if not tiene_2_num:
            errores.append("Debe tener 2 números")
        if not tiene_1_mayus:
            errores.append("debe tener una mayúscula")
        if not completo:
            errores.append("no puede estar vacío")
        return False, errores
    #
    
def solicitar_contraseña ():
    # no puede ser while true porque no es un ciclo infinito, los ciclos son limitados
    intento= 1
    while intento <= 3:
        contraseña = input("ingresa la contraseña: ")
        
        valida, mss = es_contraseña_valida()
        print(mss)

        if valida:
            print("mss")
        else:
            print("mmal")

#no he puesto los loggins y se supone que al final deben estar puestos


    



               



         

