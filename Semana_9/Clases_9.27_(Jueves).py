#1 = Funciones

#Este es un docstrising de modulo 
# Vamos a crear varias funciones 

def saludar():
    """Es una funcion que va a saludr""" 
    nombre = input("Digite el nombre: ")
    apellido = input("Digite su apellido: ")
    nombre_completo = f"{nombre.upper()} {apellido.upper()}"
    print(f"Hola {nombre_completo}")
    
def saludar_con_param(nombre, apellido):
   """Es una funcion que va a saluar"""
   
   print(f"Hola {nombre.title()} {apellido.title()}")
   
"""saludar_con_param("Fer", "Calvo")
saludar_con_param("FRANCO", "ROSALES")"""

def describir_mascota(animal, nombre_mascota): 
    """Vamos a describir mascotas."""
    print(f"Tengo un {animal}, y su nombre es {nombre_mascota}.")
    
describir_mascota(nombre_mascota = "Firulais", animal = "perro")   
describir_mascota("gato", "Mishito") 
describir_mascota(
    
    input("Digite el tipo de animal: "),
    input("Digite el nombre de la mascota: ")

