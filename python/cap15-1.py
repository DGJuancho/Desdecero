# EJERCICIOS CAPÍTULO 15

# Analizar el código

edades = [20, 10, 29]

for edad in edades:
    if edad < 15:
        break
    print(
        edad
    )  # Aquí sólo imprimirá las edad 20, porque al iterar el 10 por ser < a 15, se para el ciclo.


# Ejercicios Prácticos

a1 = {"nombre": "20022 HX1", "distancia": 2490000}
a2 = {"nombre": "20022 HA2", "distancia": 4620000}
a3 = {"nombre": "101955 Bennu", "distancia": 32490000}

asteroides = [a1, a2, a3]

contar_asteroides = 0
distancia = 0

for asteroide in asteroides:
    if asteroide["distancia"] < 7500000:
        contar_asteroides += 1
    distancia = distancia + asteroide["distancia"]

promedio_distancia = distancia / len(asteroides)
print(f"Existe alta probabilidad de colisión con {contar_asteroides} asteroides")
print(
    f"La distancia promedio de los {len(asteroides)} asteroides con la tierra es de: {int(promedio_distancia)} kms."
)
