import random

def tirar_dados():
    return random.randint(2,12)

def pedir_respuesa():
    print("ingresa tu prediccion")
    print("1. par")
    print("2. impar")
    print("salir del juego")

    return  int( input() )

def imprimir_resultado(numero, prediccion):
    es_par = numero % 2 == 0
    if es_par and prediccion == 1:
        print("Ganaste! numero de los dados", numero)
    elif not es_par and prediccion == 2:
        print("Ganaste! numero de los dados", numero)
    else:
        print("Perdiste! numero de los dados", numero)

while True:
    numero = tirar_dados()
    prediccion = pedir_respuesa()
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion)

    print("Gracias por jugar")

#print("tiro de dados", tirar_dados())
