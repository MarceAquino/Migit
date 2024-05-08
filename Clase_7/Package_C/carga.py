from validaciones import *
matriz_colectivo = [[100,1,2,3,4,5,],
                    [23,1,2,3,4,5],
                    [33,1,2,3,4,5]] 
#------------------------------------------------------------------------------------    
def cargar_legajo(legajo:int)->None:
    validacion = validar_legajo(legajo, matriz_legajo)
    while validacion == False:
        legajo = int(input("Error ingrese un legajo válido: "))
        validacion = validar_legajo(legajo, matriz_legajo)
    return print("Carga exitosa")      
#------------------------------------------------------------------------------------ 
def cargar_linea(linea:int)->None:
    validacion = validar_linea(linea, matriz_colectivo)
    while validacion == False:
        linea = int(input("Error ingrese un linea valida: "))
        validacion = validar_linea(linea, matriz_colectivo)
    return print("Carga exitosa")  
#------------------------------------------------------------------------------------ 
def cargar_coche(coche:int)->None:
    validacion = validar_coche(coche, matriz_colectivo)
    while validacion == False:
        coche = int(input("Error ingrese una unidad valida: "))
        validacion = validar_coche(coche, matriz_colectivo)
    return print("Carga exitosa")  
#------------------------------------------------------------------------------------  



















