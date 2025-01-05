# MANEJO DE ARCHIVOS

# Abrir un archivo
archivo_ahorros = open("python/archivos/ahorros.txt")

contenido_archivo = (
    archivo_ahorros.read()
)  # El método read retorna el contenido del archivo


# Separar la información por comas
ahorros = contenido_archivo.split(
    ","
)  # El método split separa la cadena de acuerdo al delimitador "," y retorna una lista con los elementos separados.

print(ahorros)
print(len(ahorros))
print(ahorros[0])


# Lectura por líneas
archivo_clientes = open("python/archivos/clientes.txt")
contenido_archivo = archivo_clientes.readlines()
for linea in contenido_archivo:
    linea_limpia = (
        linea.strip()
    )  # El método strip borra espacios indeseados o saltos de línea.
    datos_cliente = linea_limpia.split(",")
    print(f"Nombre: {datos_cliente[0]}")
    print(f"Apellido: {datos_cliente[1]}")
    print(f"Edad: {datos_cliente[2]}")


# "Escribir información en archivos"
archivo_ahorros = open("python/archivos/ahorros.txt")
contenido_archivo = archivo_ahorros.read()

archivo_ahorros_w = open("python/archivos/ahorros.txt", "w")
nuevo_ahorro = input("Por favor ingrese el ahorro de esta semana:")
nuevo_contenido = contenido_archivo + "," + nuevo_ahorro

archivo_ahorros_w.write(nuevo_contenido)
archivo_ahorros_w.close()


# DATASETS
"""Un DATASET Es una colección de datos tabulada, donde cada columna representa una variable y cada fila un elemento particular al que le esta almacenando información."""

archivo_canciones = open("python/archivos/canciones.csv", encoding="utf-8")
contenido_canciones = archivo_canciones.readlines()

i = 1

while i < len(contenido_canciones):
    linea_limpia = contenido_canciones[i].strip()
    datos_cancion = linea_limpia.split(",")
    print(datos_cancion[1])
    i = i + 1
