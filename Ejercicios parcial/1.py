#Crea un programa que pida un número y cuente desde 1 hasta ese número,
#  pero se detenga si el número ingresado no es positivo.
def secuencia ():
    while True:
      try:
        numero= int(input("ingresa un número:"))
        if numero>0:
            for i in range(numero + 1):
               print(i)
        else:
            print("ingresa un valor positivo, intenta de nuevo:")
      except ValueError:
        print("ingresa un dato valido")
secuencia ()
