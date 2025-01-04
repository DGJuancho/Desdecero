def realizar_operacion(operacion):
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if operacion == "dividir" and num2 == 0:
        print("Denominador Inválido")
        return
    resultado = {
        "sumar": num1 + num2,
        "restar": num1 - num2,
        "multiplicar": num1 * num2,
        "dividir": num1 / num2 if num2 != 0 else None,
        "potencia": num1**num2,
    }[operacion]
    print(f"El resultado de la {operacion} es: {resultado}")


while True:
    print("----INGRESE----")
    print("1) Para sumar")
    print("2) Para restar")
    print("3) Para multiplicar")
    print("4) Para dividir")
    print("5) Para potencia")
    print("0) Para salir")
    opcion = int(input())
    if opcion == 0:
        print("Hasta luego")
        break
    operaciones = {
        1: "suma",
        2: "resta",
        3: "multiplicación",
        4: "división",
        5: "potencia",
    }
    if opcion in operaciones:
        realizar_operacion(operaciones[opcion])
