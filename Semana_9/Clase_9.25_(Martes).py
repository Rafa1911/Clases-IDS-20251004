"""

mi_gato = {"nombre": "pelusa", 
           "edad": 3, 
           "personalidad": "simpatico"} # [nombre, edad, caracteristica]

print(type(mi_gato))
print(len(mi_gato)) 
print(mi_gato)

abys_cat = {
    
    "personalidad": "simpatico",
    "nombre": "peluza",
    "edad": 3
    
}

copia = mi_gato == abys_cat
print(copia)

#Vamos a crear un set 

colores = {"rojo", "rojo", "verde", "negro", "azul"}
print(type(colores))
print(len(colores))
print(colores)
"""
###################

birthdays = {
    
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
    
}



birthdays["Carol"] = "Abr 21"
birthdays["Fer"] = "Mar 3"
print(birthdays)
del birthdays["Bob"]

for persona, fecha in birthdays.items():
    
    print(f"El cumpleaños de {persona} es en {fecha}")

######################### 




"""
semana = {}
semana["Uno"] = "Lunes"
semana["Dos"] = "Martes"
semana["Tres"] = "Miercoles"
semana["Cuatro"] = "Jueves"
semana["Cinco"] = "Viernes"

print(semana)

for k, v in semana.items():
    print(f"{v}: {k}")
"""