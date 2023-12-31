#Coleccion de tipo Set, no mantiene un orden ni tampoco se pueden tener elementos duplicados

planetas = {"Marte", "Jupiter", "Venus"}

print(planetas)

#Conocer largo del set
print(len(planetas))
#Revisar si un elemento esta presente
print("Marte" in planetas)
#Agregar un elemento
planetas.add("Tierra")
print(planetas)
#Eliminar un elemento
planetas.remove("Tierra")   # ->Lanza un error en caso de que la llave no exista | 
print(planetas)


