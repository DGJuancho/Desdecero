# Ciclo While

# Un ciclo permite agrupar una serie de instrucciones y que se ejecuten una y otra vez mientras se cumpla una condición. Ej.

i = 1  # Inicialización de la variable de control (i)

while i <= 3:  # Prueba sobre la variable
    print("Bienvenidos a un ciclo en Python")  # cuerpo del ciclo
    i = i + 1  # Cambio sobre la variable de control
print(i)
print("Fin del Programa")


# Imprimir los números del 1 al 5

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Fin del Programa")


# Imprimir los múltiplos de 5 hasta el 30
i = 5
while i <= 20:
    print(i)
    i = i + 5

# Contar desde el XX hasta el 0

i = 5
while i >= 0:
    print(i)
    i = i - 1

"Imprimir x veces una frase"

numero = int(input("Indicar cuántas veces quieres que se repita la frase: "))

i = 1
while i <= numero:
    print("Este es un ciclo divertido")
    i = i + 1

# Ciclo controlado por valor centinela

nombre = ""
while nombre != "Juan":
    nombre = input("Ingrese su nombre: ")

print("Bienvenido, " + nombre)

# Instrucción break

while True:
    capital = input("Cuál es la capital de Perú: ")
    if capital == "Lima":
        print("Felicidades, ganaste la trivia")
        break

## Ejercicios Prácticos ##
# Ej. 01

numero = int(input("Ingrese un número: "))
i = 1
while i <= numero:
    print("****")
    i = i + 1

# Ej. 02

while True:
    clave = input("Por favor ingrese la clave: ")
    if clave == "Roberto":
        print("Clave correcta")
        break
    else:
        print("Clave incorrecta")
