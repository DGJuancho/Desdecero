# Ejercicios Teóricos

numero = int(input())  # 4

for i in range(numero):
    print("Rocas")  # Imprime 4 veces Rocas

mercado = ["Pan", "Harina", "Huevos"]

for articulo in mercado:
    print(articulo)  # Se ejecuta todo el código

# Ejercicios prácticos

for numero in range(1, 81):
    print(numero)

for numero in range(1000, -1, -100):
    print(numero)

for pares in range(2, 67, 2):
    print(pares)

nombre1 = input("Por favor ingres un nombre: ")
nombre2 = input("Por favor ingres un nombre: ")
nombre3 = input("Por favor ingres un nombre: ")
nombre4 = input("Por favor ingres un nombre: ")

nombres = [nombre1, nombre2, nombre3, nombre4]

for nombre in nombres:
    if nombre[0] == "L":
        print("Nombre descartado")
    else:
        print("Nombre posible: " + nombre)
