from datetime import datetime

print("*************")
print("* BIENVENIDO A           *")
print("* TIENDA DE MASCOTAS       *")
print("*************")

inventario = {
    "perro": 10,
    "gato": 8,
    "pajaro": 25,
    "iguana": 2
}

animales_totales = 0
for val in inventario.values():
    animales_totales += val

print("porfavor ingresa tu nombre")
nombre = input()
print("porfavor ingesa tu apellido")
apellido = input()

#Concatenacion
nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos,", nombre_completo)

compras = []

def mostrar_menu():
    print("")
    print("===================================")
    print("selecciona la opcion que deseas:")
    print("1: conocer cuantos animales tiene la tienda")
    print("2: comprar un animal")
    print("3: mostrar compras")
    print("4: salir del programa")


def mostrar_inventario():
    print("** INVENTARIO ***")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
    print("En total tenemos:", animales_totales, "Animales")


def comprar_animal():
    carrito = []
    
    while True:
        print("¿Que animal deseas comprar? solo puedes eligir")
        print("escribe f para terminar la lista, o v para ver")
        animal = input()
        
        if animal == "f":
            break
            
        if animal == "v":
            print(f"tu carrito de compras contiene {carrito}")
            continue
            
        if animal not in inventario:
            print(f"lo sentimos no contamos con el animal {animal}")
        elif inventario[animal] == 0:
            print(f"lo sentimos, no tenemos en existencia el {animal}")
        elif animal not in carrito:
            carrito.append(animal)
        else:
            print("ese animal ya se encuentra en tu carrito")
            #print("Haz comprado un", animal)

    print("el contenido de tu carrito es")
    for animal in carrito:
        print(" ", animal)
        inventario[animal] -= 1

        #agregar esta co(mpra al carrito de compras
        fecha = datetime.now()
        compras.append( (nombre, carrito, fecha) )


def mostrar_compras():
    print("")
    print("** COMPRAS REALIZADAS **")
    for compra in compras: # compra = tupla que tiene nombre
        print(f" {compra[0]} compro {compra[1]} en {compra[2]}")


while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("saliendo del programa")
        break
