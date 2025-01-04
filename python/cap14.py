# Funciones
"""Para crear un función, se usa la palabra reservada "def" seguido se nombra la función, se agregan los paréntesis () y dentro de los paréntesis se definen los parámetros de la función, los parámetros son opcionales; luego se colocan ":" y en la siguiente linea de forma "indented" se coloca el cuerpo de la función (instrucción o instrucciones). Si la función tiene retorno, se debe colocar la palabra reservada "return" seguido del valor a retornar (el retorno también es opcional)."""


def saludar():
    print("Bienvenido")
    print("A mi primera función")


"""Cuando deseas utilizar la función, se debe llama o "invocar" a la misma. Colocando el nombre de la misma y seguido entre paréntesis se colocan tantos argumentos como parámetros estén definidos en la función."""

saludar()
print("Fin del programa")

# Funciones con Parámetros


def saludo_personal(nombre, apellido):
    print("Hola " + nombre + " " + apellido)


saludo_personal(
    input("Por favor indícame tu nombre: "), input("Por favor indícame tu apellido: ")
)


def suma(num1, num2):
    suma = num1 + num2
    print(suma)


suma(
    float(input("Por favor indica el 1er número a sumar: ")),
    float(input("Por favor indicar el 2do término a sumar: ")),
)

# "Ámbito de las Variables: LOCAL - GLOBAL"

"""En la función anterior, las variables suma, num1, num2 sólo existen dentro de la función, ya que las mismas se encuentran en un ámbito local"""


# Ámbito Global
def calcular_precio_final(precio):
    precio_final = precio + impuestos
    print(precio_final)


impuestos = 10
calcular_precio_final(100)
"""En este caso la variable "impuestos" existe de manera global, ya que está definida fuera del cuerpo de la función"""

# Funciones con retorno


def calcular_multa(retraso):
    if retraso > 7:
        return retraso * 2
    else:
        return 3


dias = int(input("Ingrese los días de retraso: "))
multa = calcular_multa(dias)
print(
    "Usted debe pagar una multa de "
    + str(multa)
    + " dólares por el retraso en la entrega."
)

# CALCULADORA


def sumar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"El resultados de la suma es: {resultado}")


def restar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"El resultados de la resta es: {resultado}")


while True:
    print("----INGRESE----")
    print("1) Para sumar")
    print("2) Para restar")
    print("0) Para salir")
    opcion = int(input())
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 0:
        print("Hasta luego")
        break
