nombres = ["fernando", "saul", "dinora", "nicole", "cecilia"]
print(nombres)
#f-strings
for i, nombre in enumerate(nombres):
    #print(f"se inscribio", i, "en la lista:", i, nombre)
    print(f"se inscribio {nombre} en la lista con el indice")

print( "bienvenidos a la fiesta", nombre[:3] )
print( "lo sentimos", nombres[3:] )
