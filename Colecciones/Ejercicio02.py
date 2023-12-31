#Dada la siguiente lista:
#Crear la lista que solo incluya los numeros menos a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
listaM = []
for x in tupla:
    if x < 5:
        listaM.append(x)

print(listaM)