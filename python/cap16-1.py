# EJERCICIOS CAPÍTULO 16
archivo_canciones = open("python/archivos/canciones.csv", encoding="utf-8")
contenido_canciones = archivo_canciones.readlines()
h = 1
i = 1
j = 1
k = 1
l = 1

# Parte 1: Canciones lanzadas en el año 2000
print("CANCIONES AÑO 2000:")
while i < len(contenido_canciones):
    linea_limpia = contenido_canciones[i].strip()
    datos_cancion = linea_limpia.split(",")
    if int(datos_cancion[4]) == 2000:
        print(datos_cancion[1])
    i = i + 1
print("---", "\n")

# Parte 2: Canciones de Eminem
print("CANCIONES EMINEM:")
while j < len(contenido_canciones):
    linea_limpia = contenido_canciones[j].strip()
    datos_cancion = linea_limpia.split(",")
    if datos_cancion[0] == "Eminem":
        print(datos_cancion[1])
    j = j + 1
print("---", "\n")

# Parte 3: Canciones que empiezan por "D"
print('TÍTULOS QUE COMIENZA POR LA LETRA "D"')
while h < len(contenido_canciones):
    linea_limpia = contenido_canciones[h].strip()
    datos_cancion = linea_limpia.split(",")
    if datos_cancion[1][0] == "D":
        print(datos_cancion[1])
    h = h + 1
print("---", "\n")

# Parte 4: Canciones que duran más de 6 minutos
print("Canciones que duran más de 6 minutos")
while k < len(contenido_canciones):
    linea_limpia = contenido_canciones[k].strip()
    datos_cancion = linea_limpia.split(",")
    if int(datos_cancion[2]) > 400000:
        print(datos_cancion[1])
    k = k + 1
print("---", "\n")

# Parte 5: Promedio de popularidad
print("Promedio de popularidad de Canciones de la lista")
popularidad = 0
while l < len(contenido_canciones):
    linea_limpia = contenido_canciones[l].strip()
    datos_cancion = linea_limpia.split(",")
    popularidad = popularidad + int(datos_cancion[5])
    l = l + 1
promedio_pop = popularidad / (len(contenido_canciones) - 1)
print(
    f"El promedio de popularidad entre las {len(contenido_canciones)-1} canciones de la lista, es de: {promedio_pop}"
)
