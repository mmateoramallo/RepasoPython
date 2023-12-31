# Listas
listaUno = ["Mateo", "Francisco", "Cata", "Feli"]
# Imprimir toda la lista en una linea
# print(listaUno)
# Imprimirlos de manera iteradamente
# for l in listaUno:
# print(l)

# Acceder a los elementos de una lista
# print(listaUno[1])

# Imprimir un rango de la lista
# print(listaUno[0:2]) #Se excluye la cota inferior
# Cambiar un elemento de la lista
listaUno[1] = "Cata"
listaUno[2] = "Francisco"
print(listaUno)
# Cantidad de elementos
# print(len(listaUno))
# Insertar un elemento en una posicion especifica
listaUno.insert(0, "Luz")
# print(listaUno)
# Remover un elemento
listaUno.remove("Luz")
# print(listaUno)


# Tuplas -> Tipo inmutable a diferencia de las listas
miTupla = ("Naranja", "Platano", "Manzana")
for m in miTupla:
    print(m, end=", ")
# Funciones muy parecidas a las listas

# Castear una tupla a una lista
frutasLista = list(miTupla)
frutasLista.append("Pera")
frutas = tuple(frutasLista)
print('\n', frutas)
