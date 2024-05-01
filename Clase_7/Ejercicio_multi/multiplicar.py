from funciones_matriz import *


while True :
    #----------------------------------------------------------------------------------------------------------------------------------   
    matriz_a = crear_matriz(filas = input ("Ingrese la cantidad de filas de su primer matriz: "), 
                            columnas = input("Ingrese la cantidad de columnas de su primer matriz: "))
                                    
    matriz_b = crear_matriz(filas = input ("Ingrese la cantidad de filas de su segunda matriz: "), 
                            columnas = input("Ingrese la cantidad de columnas de su segunda matriz: "))  
    #----------------------------------------------------------------------------------------------------------------------------------
    validar_filas_primera_martriz = validar_matriz(matriz_a,"filas")
    validar_columnas_primera_martriz = validar_matriz(matriz_a,"columnas")

    validar_filas_segunda_martriz = validar_matriz(matriz_b,"filas")
    validar_columnas_segunda_martriz = validar_matriz(matriz_b,"columnas")
    #----------------------------------------------------------------------------------------------------------------------------------    
    if validar_columnas_primera_martriz != validar_filas_segunda_martriz:
        print("Las matrices no se puede multiplicar, verifique las filas y columnas de las mismas")   
        continuar = input("Desea volverlo a intentarlo: ")
        if continuar.lower() == "si":
            continue
        else:
            break
    else: 
        matriz_resultado = matriz_vacia = [[0]*validar_columnas_segunda_martriz    for _ in range(validar_filas_primera_martriz)] 
        matriz_resultado = multiplicar_matriz(matriz_a,matriz_b,matriz_resultado)   
        for i in range(len(matriz_resultado)): 
            for j in range(len(matriz_resultado[i])): 
                print (f"{matriz_resultado[i][j]:4}", end = " ") 
            print(" ")     
        continuar = input("Desea continuar: ")
        if continuar.lower() == "si":
            continue
        else:
            break                 
    #----------------------------------------------------------------------------------------------------------------------------------         




      
