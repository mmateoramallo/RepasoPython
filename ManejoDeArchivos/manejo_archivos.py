

try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios...')
except Exception as e:
    print(f'Ocurrio un Error: {e}')
finally:
    archivo.close()
    #Ya se cerro el archivo, no se puede leer ni escribir datos