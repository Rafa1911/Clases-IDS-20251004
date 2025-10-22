"""datos = [1,2, "tres",["lunes", "martes", "miercoles"]]
print(datos[-1][-1][3])"""

Numeros = ["uno", "dos", "tres"]

print(Numeros)

Numeros1 = Numeros + ["cuatro", "cinco", "seis"] 

print(Numeros1)
print (len(Numeros1))

Numeros1[2] = "trois"
print(Numeros1)
Numeros1.append(input("Escriba el siguiente numero: "))
print(Numeros1)
Numeros1.insert(2,input("Otro numero: "))
print(Numeros1)