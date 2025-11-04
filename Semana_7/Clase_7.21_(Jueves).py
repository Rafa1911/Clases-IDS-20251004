"""monto = float(input("Digite el monto: "))
tipo = input("Tipo (local/internacional): ")
impuesto = 0

if tipo.lower() == "local" and monto > 100:
    
 impuesto == 0.07
 
elif tipo.lower() == "local" and 75 < monto < 100:
 
 impuesto == 0.05
 
elif tipo.lower() == "local" and monto < 75 or tipo.lower() == "internacional" and monto < 75:
    
 impuesto == 0   
 
elif tipo.lower() == "internacional" and monto > 100:
    
 impuesto == 0.12
 
elif tipo.lower() == "internacional" and 75 < monto < 100:
 
 impuesto == 0.09

else: 
    
 print("Ese tipo no existe")

print(f"El tipo {tipo} con monto {monto:,.2f}")
print(f"paga un impuesto de {monto*impuesto:,.2f}")"""

###################################################################################3

#Bucles(Loops)

# Dos tipos de loop "For" y "While"

# for = se utiliza para iterar sobre una secuencia(como lista, una tupla, etc) y ejecutar un bloque de codigo para cada elemento de la secuencia. 

nombres = {"Ana", "Jose", "Luis"}

for i in nombres: 
    
   if i == "Jose": 
       print("Lo encontre")
    
   else: 
       print("No esta Jose")