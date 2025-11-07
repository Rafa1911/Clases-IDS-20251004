
def dui_validacion():
    condiciones = 0
    dui = input("Ingrese su dui: ")
    
    
    if len(dui) == 10: 
        condiciones += 1
   
    if dui.count("-") == 1:
        condiciones += 1 
        
        partes = dui.split("-")
        
        if len(partes[-1]) == 1:
         condiciones += 1
    print(f"cumple {condiciones} de condiciones")
dui_validacion()