"""usuario = "Javier" # Tipo String"""

"""
 # Validar el usuario
usuario == "Javier" 
 
 # Mostrar menus segun usuario
 
 
 # Definir tareas para usuario 
 
 
 # Presentar resumenes del usuario'''
  
"""
"""
cantidad_alumnos = 85
media_edad = 18.23387831
monto_hope = 1234567.8901
inversion_evento = -98765.21548
  
  
print(type(cantidad_alumnos))
print(type(media_edad))

print(type(cantidad_alumnos) is int)  #no es lo mismo "int" (entre comillas es la palabra)
print(type(media_edad) is int)



print("el usuario es",usuario , "y tiene ", cantidad_alumnos,"pajaritos en su aula")  
print("y la edad promedio es de ", media_edad)

print(f"El usurio es {usuario}") #f (f-string) capacidad de aceptar y tomar diferentes variables
print(f"y su aula hay { cantidad_alumnos - 4} pajaritos en su aula") # corchetes "{}" abre posibilidad de hacer cosas que un texto plano no podria hacer, Eg. Calculos 
print(f"con edad promedio de {media_edad:.3f} años") #":" Definir formato,  ".2f" dos decimales fijos
print(f"recolectaron ${monto_hope:,.2f} como un donativo") #"," separador de comas por miles 
print(f"y la totalidad de gastos fue de ${abs(inversion_evento):,.2f} dolares.") # "abs" valor absoluto

print(type(usuario) is str)

esta_lloviendo = False 
print(type(esta_lloviendo) is bool)
print(type(monto_hope) is not bool)
"""
nombre = "Alvin"
apellido = "Portillo"
nombre_completo = nombre + " " + apellido # "+ " " +" operardor para unir textos (concatenando), solo str
print(nombre_completo)