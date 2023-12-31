# Funcion que se llama asi misma

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Imprimir los numeros de 5 a 1 de manera descendente usando funciones recursivas
def mostrarRecur(n):
    if n >= 1:
        print(n)
        mostrarRecur(n - 1)
    elif n == 0:
        return
    elif n < 0:
        print('Valor Incorrecto')


if __name__ == '__main__':
    #n = int(input('Ingrese el numero del cual desea buscar el factorial: '))
    #fac = factorial(n)
    #print(f"El factorial de {str(n)} es: {fac}")
    mostrarRecur(5)
