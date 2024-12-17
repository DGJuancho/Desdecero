# Listas en Python
"""Para generar una lista, primero definimos el nombre, dentro de [corchetes] colocamos cada valor separado por una coma """

nombres = ["Pedro", "Luisa", "Ana"]
print(nombres)
print(type(nombres))

mis_datos = ["Juancho", 46, "juancho.designs@icloud.com", 1.78]
print(mis_datos)

edad = 48
hobbies = ["Leer"]


# Acceder a elementos de una lista
"""Primero colocamos el nombre de la variable donde se almacenará la lista. Luego abrimos y cerramos corchetes “[]”, y en el medio de los corchetes colocamos la posición del elemento al cual queremos acceder."""

cantantes = ["Elvis", "Juan Gabriel", "Elton John", "Luciano Pavarotti"]
cantante1 = cantantes[0]
print(len(cantantes))
print(cantante1)
print(cantantes[2])
print(cantantes[len(cantantes) - 1])

# Modificar elementos
"""Colocamos el nombre de la variable, entre [corchetes] colocamos la posición del elemento a modificar, luego colocamos el signo igual y el nuevo valor del elemento."""

motocicletas = ["Honda", "Yamaha", "Suzuki"]
print(motocicletas[0])

motocicletas[0] = "Ducati"
print(motocicletas[0])

# Agregar elementos a una lista
"""Para agregar elementos en la lista colocamos el nombre de la variable, luego utilizamos el método append() y dentro del paréntesis colocamos el nuevo elemento a agregar"""

aliens = []
aliens.append("E.T.")
aliens.append("Goku")
aliens.append("Marvin")
aliens.append("Gazoo")

print(aliens[3])

# eliminiar elementos de una lista
"""Para eliminar un elemento colocamos el nombre de la variable, luego el método pop() y dentro del paréntesis se coloca la posición del elemento a eliminar."""

aliens.pop(1)

print(aliens[1])

# Ciclos con Listas

autos = ["Chevrolet", "Mitsubishi", "Ford", "Toyota", "Nissan"]

i = 0

while i < len(autos):
    print(autos[i])
    i = i + 1
