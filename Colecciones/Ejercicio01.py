# Ejercicio 1 Iterar un rango 0 a 10, imprimir numeros divisibles a 3
divTres = range(0, 11, 1)
for x in divTres:
    if (x % 3 == 0):
        print(x)

print('-' * 21)
ranDosSeis = range(2, 7, 1)
for x in ranDosSeis:
    print(x)
print('-' * 21)

ranTres = range(3, 11, 2)

for x in ranTres:
    print(x)