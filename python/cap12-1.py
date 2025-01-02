# Ejercicios

personaje = {"nombre": "Mago", "fuerza": 30.5, "vidas": 2}

print(personaje["nombre"])  # Mago
print(type(personaje["fuerza"]))  # float


juguete = {"nombre": "Tren", "precio": 99}  # Posee 2 claves

print(type(juguete))  # dict
print(type(juguete["precio"]))  # int
# print(juguete["marca"])  # error

mascota = {
    "nombre": input("Por favor ingrese el nombre de su mascota: "),
    "edad": input("Ahora ingrese la edad de su mascota: "),
    "raza": input("Por último, ingrese la raza de su mascota:"),
}

print(mascota)

fan = int(input("Por favor indique de cuántos clubes de futbol usted es fan: "))

clubes = []

i = 0

while i < fan:
    nombre = input("Ingrese el nombre de su equipo:")
    pais = input("Ingrese el país de orige:")
    equipo = {"nombre": nombre, "Pais": pais}
    clubes.append(equipo)
    i = i + 1

print(clubes)
