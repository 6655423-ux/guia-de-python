# Ciclo, iteracion, bucle

# while
"""
i = 0
while i < 10:
    if i < 5:
        print("El numero", i, "Es menor a 5")
    else:
        print("El numero", i, "es mayor o igual a 5")
    i += 1

print("Termino la iteracion")
"""

# for x in range(1, 11):
#     print(x)

while True:
    print("escribe la opcion deseada")
    print("1: Saludar")
    print("2: salir")
    
    Respuesta = int(input())
    
    if Respuesta == 1:
        print("saludos terricola!")
    elif Respuesta == 2:
        break

print("terminando programa")
