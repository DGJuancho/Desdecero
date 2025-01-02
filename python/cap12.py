# Diccionarios

"""Un diccionario se crea definiendo el nombre de la variable, luego entre llaves se colocan la parejas 'key:value' (clave:valor), con los datos que queremos guardar, separados por comas."""

misDatos = {"nombre": "Juancho", "Edad": 46, "Estatura": 1.78}

producto = {"nombre": "iPhone 14", "precio": 799, "color": "Plata"}

print(producto)
print(type(producto))

# Ejemplo de Listas
notas = [4.5, 3.0, 5.0]
dias = ["Lunes", "Martes", "Miércoles"]
edades = [40, 12, 29, 55]

# Ejemplo de diccionarios
computador = {"marca": "Dell", "procesador": "i7"}
personaje = {"nombre": "Mago", "ataque": 20}
pais = {"nombre": "Colombia", "capital": "Bogotá"}

"""Para acceder a un valor de un diccionario debemos:
Colocar el nombre de la variable, luego entre corchetes [] colocamos la clave a la cual está asociada el valor al que queremos acceder"""

carro = {"marca": "Toyota", "color": "negro"}

print(len(carro))
print(carro["marca"])
print(carro["color"])

"""Para modificar un valor:
Colocamos el nombre de la variable, luego entre corchetes [] colocamos la clave del valor que queremos modificar,luego el símbolo = y finalmente el nuevo valor"""

carro["color"] = "rojo"
print(carro["color"])

"""Para agregar un valor:
Colocamos el nombre de la variable, entre corchetes [] colocamos la nueva clave, luego = y finalmente el nuevo valor que estamos asignando."""

carro["maletero"] = "SkyBox 16"
carro["guardabarro"] = "Pocket Style"

print(carro["maletero"])
print(carro)

"""Paa eliminar un valor:
Colocamos el nombre de la variable, luego colocamos un punto'.' a continuación colocamos pop() y dentro del paréntesis colocamos la clave del valor a eliminar. Este procedimiento eliminar la clave y el valor"""

carro.pop("maletero")

print(carro)

# listas que contienen diccionarios

producto1 = {"nombre": "Monitor", "precio": 119}
producto2 = {"nombre": "Mouse", "precio": 6}

listaProductos = []
listaProductos.append(producto1)
listaProductos.append(producto2)

print(listaProductos)
print(listaProductos[0])
print(listaProductos[1]["nombre"])

i = 0

while i < len(listaProductos):
    print("Nombre del Producto: " + listaProductos[i]["nombre"])
    print("Precio del Producto: " + str(listaProductos[i]["precio"]))
    i = i + 1
