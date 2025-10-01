cantidad_alumnos = 25
nombre_profe = "Alvin"
nuevas_inscripciones = 0
nombre_profe = input("Ingrese el nombre del profesor:  ") #casi el inverso de print, ingresar hacia la pantalla
nuevas_inscripciones = int(input("Nuevos alumos:  ")) #hay que poner "int" para que lo tome como entero y no como string
print(type(nombre_profe))
print(nombre_profe)
print(cantidad_alumnos + nuevas_inscripciones) 
