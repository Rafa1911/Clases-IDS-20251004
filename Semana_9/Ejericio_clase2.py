
def dui_validacion():
    condiciones = 0
    dui = input("Ingrese su dui: ")
    
    guion = dui.split("-")
    
    if len(dui) == 10: 
        condiciones + 1
   
    if dui.count("-") == 1:
        condiciones + 1 
        
    if len(guion[-1]) == 1:
        condiciones + 1
    
print