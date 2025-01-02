# Ciclo for

"""La estructura básica del ciclo for es la siguiente:
Se define la colección a recorrer (lista, diccionario, texto), luego se coloca la palabra for para definir el ciclo, se define una variable de control, luego la palabra y la variable que representa la colección a recorrer y :, finalmente se define el cuerpo del ciclo de manera indentada."""

edades = [80, 68, 53, 52, 50, 46]

for edad in edades:
    print(edad)

# Recorrer textos con for

mensaje = "Hola Juancho"

for caracter in mensaje:
    print(caracter)

# Se recomienda nombrar la variable de control de forma que represente lo que está iterando


# ciclo for con diccionarios

ciclista = {"Nombre": "Egan", "Apellido": "Bernal", "Tipo": "Escalador"}

for clave in ciclista:
    print(clave + ": " + ciclista[clave])


# Ciclos con listas que contienen diccionarios

discoteca1 = {"nombre": "Perro Negro", "ubicación": "Poblado"}
discoteca2 = {"nombre": "Teatro Victoria", "ubicación": "Poblado"}

discotecas = [discoteca1, discoteca2]

for discoteca in discotecas:
    print(discoteca["nombre"] + " - " + discoteca["ubicación"])


# "Función RANGE"

"""La función range permite crear secuencias de números, en su forma más simple la función recibe 1 solo argumento 'range(n)' y devuelve la secuencia con las características por defecto, es decir, inicia en 0 en incrementos de 1 y la secuencia termina antes de llegar a 'n'."""

for numero in range(10):
    print(numero)

"""Función range recibe hasta 3 argumentos, que seria range(inicio, fin, paso) el argumento 'paso' es opcional"""

for impares in range(1, 23, 2):
    print(impares)
