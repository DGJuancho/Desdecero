# CAPÍTULO 17. LIBRERÍAS EN PYTHON
# Para importar una librería utilizamos la palabra import y luego el nombre de la librería.

import math, random
import matplotlib.pyplot as plt

print(math.sqrt(16))
print(math.fabs(-8))

num_aleatorio = random.randint(1, 10)
print(num_aleatorio)

candidatos = ["Juan", "Pedro", "José", "María"]
print(random.choice(candidatos))

# x Representa los años
x = [2012, 2013, 2014, 2015, 2016, 2017]
# y Representa el dinero ahorrado
y = [0, 50, 70, 70, 100, 246]

# Función plot dibuja un polígono de acuerdo a las coordenadas de x e y.

plt.plot(x, y)
plt.xlabel("Año")
plt.ylabel("Ahorro (Dólares)")
plt.show()

x = [2017, 2018, 2019, 2020, 2021]
y = [1566, 1808, 1637, 1433, 2206]

# La función bar dibuja un diagrama de barras donde "x" da la posición de las barra y "y" la altura de las mismas.
plt.bar(x, y)
plt.xlabel("Año")
plt.ylabel("Terremotos")

plt.show()
