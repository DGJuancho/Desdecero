# función input para ingresar datos del usuario
"""
print("Por favor ingrese un nombre")

nombre = input()

print(f"Su nombre es: {nombre}")
"""
# Podemos mejorar esta sentencia, eliminando el print para ingresar el nombre y colocarlo directamente en la varaible

nombre = input("Por favor ingrese un nombre: ")

""" todo lo que se ingresa a través de la función input es de tipo string por defecto,
para convertir el tipo de dato, se usan las funciones int, float, str,
como lo veremos a continuación."""

edad = int(input("ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))
print(f"Su nombre es: {nombre}, tiene {edad} años y su estatura es de: {estatura} mts")

print(type(nombre))
print(type(edad))
print(type(estatura))

"""
Para concatenar cadenas de texto y contenido de variables utilizamos el símbolo +
Sin embargo, en ocasiones requerimos la función str (convierte valores numéricos a string)
Puesto que en python no podemos concatenar textos con números.
"""

nombre_producto = "Televisor"
precio_producto = 200.00
print("Nombre: " + nombre_producto)
print("Precio: " + str(precio_producto))

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su Apellido: ")

print(apellido + " " + nombre)

calculo_cientifico = float(
    input("Por favor indique en cuantos años caerá el asteroide: ")
)

tiempo_real = calculo_cientifico / 2

print("El asteroide caerá en " + str(tiempo_real) + " años")
