print("Bienvenido al conversor de millas a kilometros")

print("Escribe el numero de millas")
millas = input()  #string

print("tipo de dato de millas", type(millas))
#comvertir de string a numero
millas = float(millas)
print("tipo de dato de millas", type(millas))

#1 milla = 1.609 kms
kilometros = millas * 1.609

print("millas ingresadas:", millas)
print("kilometros:", kilometros)
