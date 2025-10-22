"""nombre = "Antonio" 

repetidos = nombre.lower().count("a")
print(repetidos)"""

"""nombres = ["Ana", "Antonio", "Ana", "Jose"]

contador = 0 

for nombre in nombres:
    if nombre == "Ana":
        contador += 1

print(contador)"""

"""nombres = ["Ana", "Antonio", "Ana", "Jose"]
contador = 0 

for i in range(1, len(nombres)):
    if nombres[i] == "Ana": 
        contador += 1 
        print(contador)"""
    
# .append() = Agregar al final 
# .insert() = Agregar en una posicion 
# .remove() = elimina por valor 
# .pop() p del = eliminar por indice 
# lista[i] = nuevo_valor = Remplazar un valor 
# for o list comprehension = cambiar o eliminar segun condicion 

##############################################

numero = 6 

captura = int(input("Adivina el numero (un intento ): "))
if captura == numero:
    print("Le aceertase!")
else: 
    print("Puedes seguir jugando. ")
    
# elif = otra condicional  
