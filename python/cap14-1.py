# Ejercicios de funciones


# Ejercicio 14.4
def primer_nombre(nombres):
    print(nombres[0])


nombres = ["Zeus", "Poseidon", "Ares"]
primer_nombre(nombres)


# Ejercicios 14.5
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


def multiplicar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"El resultados de la multiplicación es: {resultado}")


def dividir():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultados de la división es: {resultado}")
    else:
        print("Denominador Inválido")


def potencia():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1**num2
    print(f"El resultados de la potencia es: {resultado}")


while True:
    print("----INGRESE----")
    print("1) Para sumar")
    print("2) Para restar")
    print("3) Para multiplicar")
    print("4) Para dividir")
    print("5) Para potencia")
    print("0) Para salir")
    opcion = int(input())
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        potencia()
    elif opcion == 0:
        print("Hasta luego")
        break
