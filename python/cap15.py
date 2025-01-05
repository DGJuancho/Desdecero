# CONTADORES, ACUMULADORES Y BANDERAS

# CONTADORES: Un contador es una variable que se utiliza para llevar la cuenta de algo.

# Contador con Listas

edades = [34, 50, 28, 20, 44, 18, 30]

contador_mayores30 = 0

i = 0
while i < len(edades):
    if edades[i] > 30:
        contador_mayores30 += 1
    i = i + 1
print(
    f"El total de trabajadores mayores a 30 años es de: {contador_mayores30} personas"
)

# Contador con diccionarios

ciudad1 = {"nombre": "Envigado", "habitantes": 249800}
ciudad2 = {"nombre": "Sabaneta", "habitantes": 87981}
ciudad3 = {"nombre": "Rionegro", "habitantes": 147484}

ciudades = [ciudad1, ciudad2, ciudad3]

contador = 0

for ciudad in ciudades:
    if ciudad["habitantes"] > 90000:
        contador += 1
print(f"Hay {contador} ciudades con más de 90.000 habitantes")


# ACUMULADORES: Un acumulador es una variables que se utiliza para acumular valores.

# Acumulador con Listas

salarios = [3000, 1500, 800, 450, 2345]

acumulador_salario = 0
i = 0

while i < len(salarios):
    acumulador_salario = acumulador_salario + salarios[i]
    i = i + 1

print(f"La suma total de la nómina para este mes de: {acumulador_salario} dólares.")


# Acumuladores con lista que contienen diccionarios

ciudad1 = {"nombre": "Envigado", "habitantes": 249800}
ciudad2 = {"nombre": "Sabaneta", "habitantes": 87981}
ciudad3 = {"nombre": "Rionegro", "habitantes": 147484}

ciudades = [ciudad1, ciudad2, ciudad3]

acumulador = 0

for ciudad in ciudades:
    acumulador = acumulador + ciudad["habitantes"]

promedio = acumulador / len(ciudades)
print(
    f"El promedio de habitantes entre las {len(ciudades)} ciudades es de: {acumulador} habitantes."
)


# BANDERAS: Una bandera es una variables booleana que se utiliza para verificar si ha sucedido cierta situación.

notas = [3.5, 4.5, 4.4, 4.6, 4.0]

nota_alta = False

for nota in notas:
    if nota > 4.5:
        nota_alta = True
        break

if nota_alta:
    print("Te sacaste al menos una nota alta")
else:
    print("Eres un vago puras notas bajas")
