# Ejercicio 1

peliculas = []
peliculas.append(
    input("Por favor ingrese sus películas favoritas, separada por comas: ")
)

print(peliculas)


# Ejercicio 2

mensaje_secreto = [
    "Planeta",
    "Más",
    "Secreto",
    "Alienigena",
    "Zombie",
    "Serás",
    "Nuclear",
    "Vos",
]

i = 1

while i < len(mensaje_secreto):
    print(mensaje_secreto[i])
    i = i + 2
