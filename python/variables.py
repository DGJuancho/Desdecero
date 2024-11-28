# precioProducto = 150
# print(precioProducto)
# print(type(precioProducto))

# precioProducto = 250.5
# print(precioProducto)
# print(type(precioProducto))

edadLuis = 10
edadLaura = 20
sumaEdades = edadLuis + edadLaura

print(sumaEdades)

promedioEdades = sumaEdades / 2

# Para imprimir una variable en medio de un string podemos utilizar la función format, colocando una f antes del string y dentro de llaves las variables a imprimir.

print(f"El promedio de edad entre Luis y Laura es de: {promedioEdades}")

# La siguiente linea representa el salario mensuales de una persona

salario = 100

"""Dividiremos el salario, para repartirlo con la esposa y mostramos el resultado por pantalla"""

esposo = salario * 0.25
esposa = salario - esposo

print(
    f"Del salario mensual del esposo, le corresponde a la esposa {esposa}$ y al esposo {esposo}$ sin chilladera"
)
