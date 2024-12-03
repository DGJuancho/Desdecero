# Ciclos con textos

textO = input("Por faovr ingrese una palabra: ")

i = 0

while i < len(textO):
    print(textO[i])

    i = i + 1

texto = "Gatubela"

# Ejercicios

print(texto[0])
print(texto[0:3])
pos1 = texto.find("u")
print(pos1)

palabra = input("Ingresar un texto: ")
print(palabra[len(palabra) - 1])

"""Implemente un programa en el cual le solicite al usuario que ingrese por teclado un texto. Luego imprima el primer carácter de ese texto concatenado con el último carácter de ese texto."""

caracter = input("Por favor ingrese un texto: ")

print(caracter[0] + caracter[len(caracter) - 1])

# Bibliotecaria

texto = input("Por favor ingrese un texto: ")
texto_minus = texto.lower()

buscar_z = texto_minus.find("z")

if buscar_z == -1:
    print('El Texto no tiene la letra "z"')
else:
    print('El texto contiene la letra "z", no lo vayas a analizar')

# Comunicar con alien

dialecto = input("Ingrese una palabra")

i = 0

while i < len(dialecto):
    if (
        dialecto[i] != "a"
        and dialecto[i] != "e"
        and dialecto[i] != "i"
        and dialecto[i] != "o"
        and dialecto[i] != "u"
    ):
        print(dialecto[i])

    i = i + 1
