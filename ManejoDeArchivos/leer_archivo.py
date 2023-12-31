archivo = open('prueba.txt', 'r', encoding='utf8')
#print(archivo.read()) -> Leer todo el archivo

#Leer algunos caracteres
#print(archivo.read(5)) # -> Cantidad de caracteres a leer
#print(archivo.read(6))


#Leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

#Iterar cada una de las lines
#for linea in archivo:
    #print(linea)

#Leer todas las lineas
#print(archivo.readlines())

#Acceder a una sola linea de la lista
#print(archivo.readlines()[0])


#Crear copia de un archivo

archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())


archivo2.close()
archivo.close()