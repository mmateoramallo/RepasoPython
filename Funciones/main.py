# Valores por defecto, se quedan marcados en la signatura
def sumar(a=0, b=0):
    return a + b


# Argumentos variables en una funcion en Python -> De manera interna se convierte en una tupla el parametro
def listarNombre(*nombres):
    for nombre in nombres:
        print(nombre)


def sumarNumeros(*numeros):
    acu = 0
    for num in numeros:
        acu += num
    return acu


def multNumeros(*numeros):
    acu = 1
    for num in numeros:
        acu *= num

    return acu


# Argumentos variables, llave-valor -> Se recibe un diccionario completo
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"La llave {llave}, tiene como valor: {valor}")


# Funcion que reciba una lista de elementos
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


if __name__ == '__main__':
    # s = sumar(3, 4)
    # print(f"El resultado de la suma es: {s}")
    # print(f"El resultado de la suma es: {sumar(4)}")
    # listarNombre('Mateo', 'Ramallo', 'Francisco', 'Ramallo')
    sumaTotal = sumarNumeros(3, 4, 5, 1)
    # print(f"El resultado de la suma es:{sumaTotal}")
    multiplicacionTotal = multNumeros(3, 4, 5)
    # print(f"El resultado de la multiplicacion es:{multiplicacionTotal}")
    # listarTerminos(IDE='Integrated Development Enviroment', OOP="Object Oriented Programming")
    nombres = ["Mateo", "Juan", "Carla", "Guillermo"]
    desplegarNombres(nombres)