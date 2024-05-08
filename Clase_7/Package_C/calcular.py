from validaciones import *
matriz_recaudacion =[[0]*6 for _ in range(3)] 
#------------------------------------------------------------------------------------  
def cargar_recaudacion(recaudacion: int, coche: int, linea: int, matriz_recaudacion: list, matriz_colectivo: list) -> list:
    
    for i in range(len(matriz_colectivo)):
        for j in range(1, len(matriz_colectivo[i])):  
            if matriz_colectivo[i][0] == linea and matriz_colectivo[i][j] == coche:
                matriz_recaudacion[i][j] += recaudacion
                return matriz_recaudacion   
#------------------------------------------------------------------------------------             
def mostrar_recaudacion(matriz_recaudacion: list) -> None:
    print("Recaudación de todos los coches y líneas:")
    mostrar_matriz(matriz_recaudacion)    
#------------------------------------------------------------------------------------ 
def calcular_recaudacion_linea(matriz_recaudacion: list) -> None:
    print("Recaudación por línea:")
    for i in range(len(matriz_recaudacion)):
        recaudacion_total = 0
        for recaudacion in matriz_recaudacion[i]:
            recaudacion_total += recaudacion
        print(f"Línea {i}: {recaudacion_total}")
#------------------------------------------------------------------------------------ 
def calcular_recaudacion_coche(matriz_recaudacion: list) -> None:
    print("Recaudación por coche:")
    for i in range(len(matriz_recaudacion)):  
        for j in range(len(matriz_recaudacion[i])):
            recaudacion = matriz_recaudacion[i][j] 
            print(f"Línea {i}, Coche {j}: {recaudacion}")
#------------------------------------------------------------------------------------ 
def calcular_recaudacion_total(matriz_recaudacion: list) -> None:
    total = 0
    for fila in matriz_recaudacion:
        for recaudacion in fila:
            total += recaudacion
    print(f"Recaudación total: {total}")
#------------------------------------------------------------------------------------ 
