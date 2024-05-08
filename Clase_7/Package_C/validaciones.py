import random

matriz_legajo =[[0]*5 for _ in range(3)]    
#------------------------------------------------------------------------------------

def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')
        print("")

#------------------------------------------------------------------------------------

def general_legajos (matriz_legajo)->list:
    leg_choferes = random.randint(1,1000)
    for i in range(len(matriz_legajo)):
        for j in range(len(matriz_legajo[0])):
            leg_choferes = leg_choferes + 1
            matriz_legajo [i][j] = leg_choferes
    return matriz_legajo  

#------------------------------------------------------------------------------------

general_legajos (matriz_legajo)  
mostrar_matriz(matriz_legajo)  

#------------------------------------------------------------------------------------

def validar_legajo (legajo: int, matriz_legajo: list)-> bool:
    for i in range(len (matriz_legajo)):
        for j in range (len(matriz_legajo[i])):
            if matriz_legajo[i][j] == legajo:
                return True
    return False

#------------------------------------------------------------------------------------   
     
def validar_linea (linea: int, matriz: int)-> bool:
    for i in range(len(matriz)):
        if matriz[i][0] == linea:
            return True
    return False

#------------------------------------------------------------------------------------ 
   
def validar_coche (coche: int, matriz: list)-> bool:
    for i in range (len(matriz)):
        for j in range (1, len(matriz[i])):
            if matriz[i][j] == coche:
                return True
    return False
