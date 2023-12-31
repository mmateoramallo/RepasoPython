# Ejercicio Calculadora de impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
def calc_impuesto(pago_sin_impuesto, impuesto):
    pago_final = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_final


# Realizar convertidor de temperatura
def convert_temp():
    op = mostrar_menu_temp()
    gradosConvertir = float(input("Introduce el valor de los grados a convertir: "))
    grados_final = 0.0
    while op != 0:
        # Pasar de Celsius a fahrenheit
        if op == 1:
            grados_final = (9 / 5) * gradosConvertir + 32
            print(f"El valor de la conversion es: {grados_final} y el valor ingresado fue: {gradosConvertir}")
            op = mostrar_menu_temp()
            gradosConvertir = float(input("Introduce el valor de los grados a convertir: "))
            grados_final = 0.0
        # Pasar de Celsius a Kelvin
        elif op == 2:
            grados_final = gradosConvertir + 273.15
            print(f"El valor de la conversion es: {grados_final} y el valor ingresado fue: {gradosConvertir}")
            op = mostrar_menu_temp()
            gradosConvertir = float(input("Introduce el valor de los grados a convertir: "))
            grados_final = 0.0
        # Pasar de fahrenheit a Celsius
        elif op == 3:
            grados_final = (gradosConvertir - 32) / 1.8
            print(f"El valor de la conversion es: {grados_final} y el valor ingresado fue: {gradosConvertir}")
            op = mostrar_menu_temp()
            gradosConvertir = float(input("Introduce el valor de los grados a convertir: "))
            grados_final = 0.0
        # Pasar de Kelvin a Celsius
        elif op == 4:
            grados_final = gradosConvertir - 273.15
            print(f"El valor de la conversion es: {grados_final} y el valor ingresado fue: {gradosConvertir}")
            op = mostrar_menu_temp()
            gradosConvertir = float(input("Introduce el valor de los grados a convertir: "))
            grados_final = 0.0



def mostrar_menu_temp():
    print("*" * 21, "Conversor De Temperatura", "*" * 21)
    print("*" * 21, "1) Pasar de Celsius a fahrenheit", "*" * 21)
    print("*" * 21, "2) Pasar de Celsius a Kelvin", "*" * 21)
    print("*" * 21, "3) Pasar de fahrenheit a Celsius", "*" * 21)
    print("*" * 21, "4) Pasar de Kelvin a Celsius", "*" * 21)
    print("*" * 21, "0) Salir", "*" * 21)

    op = int(input("Ingrese la opcion deseada: "))

    return op


if __name__ == '__main__':
    """
    pago_sin_impuesto = int(input('Introduce el valor del pago sin impuesto: '))
    impuesto = int(input('Introduce el valor del porcentaje del impuesto: '))
    pago_final = calc_impuesto(pago_sin_impuesto, impuesto)
    print(f"El valor del pago final es de {pago_final}, \n Teniendo en cuenta que el pago sin impuesto es: {pago_sin_impuesto} \n y el impuesto es ")
    """
    convert_temp()
