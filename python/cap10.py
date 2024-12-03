## Textos ##

nombre = "Juliana"  # Definir variable str con comillas dobles
apellido = "Parra"  # Definir variable str con comillas simples
nombre_completo = nombre + " " + apellido  # Concatenar texto

print(nombre_completo)  # Mostrar en pantalla variable string
print("30 Años de edad")  # Mostrar en pantalla valor string
print(type(nombre_completo))  # Mostrar en pantalla el tipo de dato de una variable

# obtener la longitud de un texto

mensaje = "Hola, Juancho"

tamaño1 = len(mensaje)  # La función "len" recibe un argumento,
tamaño2 = len(
    "Medellin"
)  # y retorna el número de elementos que contiene ese argumento.

print(
    mensaje,
    " este mensaje tiene longitud de",
    tamaño1,
    "y este otro mensaje tiene tamaño",
    tamaño2,
)

# Extracción de elementos (Carácter)

caracter_po0 = mensaje[0]
caracter_po4 = mensaje[4]
caracter_final = mensaje[len(mensaje) - 1]

print(caracter_po0)
print(caracter_po4)
print(caracter_final)

# Extracción de elementos (Conjunto de Caracteres)
texto = "Precio: 250.00"

sub_texto1 = texto[0:7]
sub_texto2 = texto[8:14]

print(sub_texto1)
print(sub_texto2)

# Búsqueda de elementos (Carácter o Conjunto de Caracteres)

pos0 = mensaje.find("o")
pos_texto = mensaje.find("Juancho")
pos_z = mensaje.find("z")

# El método find devuelve la posición en que aparece el caracter o subtexto que buscamos, en caso de no conseguirlo, retorna el valor  -1.

print(pos0)
print(pos_texto)
print(pos_z)

# El método find sólo está disponible para valores (variables) de tipo string.

# Búsqueda de elementos desde una posición inicial
datos = 'Monitor Compaq 21"-$ 1,250-20'
pos_guion1 = datos.find("-")
pos_guion2 = datos.find("-", pos_guion1 + 1)

producto = datos[0:(pos_guion1)]
precio = datos[pos_guion1 + 1 : pos_guion2]
cantidad = datos[pos_guion2 + 1 : len(datos)]

print(pos_guion1)
print(pos_guion2)
print(producto)
print(precio)
print(cantidad)

# Método para cambiar todo el texto a minúsculas

mensaje = "Ubicación: Provenza"

mensaje_minus = mensaje.lower()

print(mensaje_minus)

mensaje_mayus = mensaje.upper()

print(mensaje_mayus)

# Métodos para contar la veces que aparece un carácter

conteo = mensaje.count("q")

print(conteo)

# Método para reemplazar un carácter por otro

nuevo_caracter = mensaje.replace("a", "x")

print(nuevo_caracter)
