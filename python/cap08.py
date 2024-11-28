"""
temperatura = float(input("Por favor indique la temperatura actual:"))

if temperatura >= 27:
    print('"Debemos comprar helado"')
else:
    print('"Podemos comprar Jugo de Naranja"')

print("Fin del programa")
"""

# Cálculo del área de un cuadrado

lado = float(input("Por favor ingreese la medidad del lado del cuadrado:"))

if lado > 0:
    area = lado * lado
    print(f"El área del cuadrado es {area}")
else:
    print("La medida del lado del cuadrado no puede ser negativa")


# If, elif, else

temperatura = float(input("Por favor indique la temperatura actual:"))

if temperatura >= 27:
    print("Debemos comprar helado")
elif temperatura < 15:
    print("Hace frio, compremos chocolate")
else:
    print("Podemos comprar Jugo de Naranja")

print("Fin del programa")

# Condicionales anidadas

tipo_atraccion = int(input("Ingtrese el tipo de atracción  1) Montaña Rusa, 2) Tren:"))
if tipo_atraccion == 1:
    estatura = float(input("Por favor ingrese su estatura:"))
    if estatura >= 1.61:
        print("Diviértete en la Montaña Rusa")
    else:
        print("Debes crecer un poco más antes de subir a la montaña rusa")
elif tipo_atraccion == 2:
    print("Disfruta tu viaje en tren")
print("Fin del programa")


# Ejercicios prácticos
pinturaDerramada = 20
if pinturaDerramada >= 15:
    print("¿Qué es esooo?")
elif pinturaDerramada > 0:
    print("Podrías mejorar")
else:
    print("Tienes talento")
print("Fin programa")

genero_musical = input("Por favor indique su género musical:")
if genero_musical == "Rock":
    print("Excelente gusto")
else:
    print("Que asco :( ")

candidato1 = input("Indique el nombre del primer candidato: ")
votos_candidato1 = int(input(f"Indique cuántos votos obtuvo {candidato1}: "))
candidato2 = input("Indique el nombre del segundo candidato: ")
votos_candidato2 = int(input(f"Indique cuántos votos obtuvo {candidato2}: "))

if votos_candidato1 > votos_candidato2:
    print(f"El candidato ganador es: {candidato1}")
elif votos_candidato1 < votos_candidato2:
    print(f"El candidato ganador es: {candidato2}")
elif votos_candidato1 == votos_candidato2:
    print("Ha habido un empate")
