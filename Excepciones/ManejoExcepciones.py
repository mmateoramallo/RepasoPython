from NumerosIdenticosException import *
resultado = None

# 10/0 -> Error
try:
    a = int(input('Proporcione un valor'))
    b = int(input('Proporcione un segundo valor'))
    if a == b:
        raise NumerosIdenticosException('Numeros Identicos')
    resultado = a / b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError -> Ocurrio un error: {e}')
except TypeError as e:
    print(f'TypeError -> Ocurrio un error: {e}')
except Exception as e:
    print(f'Exception -> Ocurrio un error: {e}')
else:
    print('No ocurrio ninguna excepcion')
finally:
    print('Se ejecuta siempre si se lanza o no una excepcion')
print(f'Resultado: {resultado}')
print('Continuamos...')
