from funciones_matriz import *
from colorama import init, Fore
init()

print(Fore.GREEN+ "\nBienvenidos programa para multiplicar matrices: \n" +Fore.RESET)

while True :
    #----------------------------------------------------------------------------------------------------------------------------------   
    matriz_a = crear_matriz(filas = input (Fore.GREEN+"Ingrese la cantidad de filas de su primer matriz: " +Fore.RESET), 
                            columnas = input (Fore.GREEN+"Ingrese la cantidad de columnas de su primer matriz: " +Fore.RESET))
                                    
    matriz_b = crear_matriz(filas = input (Fore.GREEN+"Ingrese la cantidad de filas de su segunda matriz: " +Fore.RESET), 
                            columnas = input (Fore.GREEN+"Ingrese la cantidad de columnas de su segunda matriz: " +Fore.RESET))  
    #----------------------------------------------------------------------------------------------------------------------------------
    validar_filas_a_martriz = validar_matriz(matriz_a,"filas")
    validar_columnas_a_martriz = validar_matriz(matriz_a,"columnas")

    validar_filas_b_martriz = validar_matriz(matriz_b,"filas")
    validar_columnas_b_martriz = validar_matriz(matriz_b,"columnas")
    #----------------------------------------------------------------------------------------------------------------------------------    
    
    if validar_columnas_a_martriz != validar_filas_b_martriz:
        print(Fore.RED+ "\nLas matrices no se puede multiplicar, verifique las filas y columnas de las mismas.\n" +Fore.RESET)   
        continuar = input(Fore.GREEN + "Desea volverlo a intentarlo: " +Fore.RESET)
        if continuar.lower() != "si":
            break

    else: 
        matriz_resultado = matriz_vacia = [[0]*validar_columnas_b_martriz    for _ in range(validar_filas_a_martriz)] 
        matriz_resultado = multiplicar_matriz(matriz_a,matriz_b,matriz_resultado)  
        print(Fore.CYAN + "\nLa matriz resultante es:\n" +Fore.RESET)     
        for i in range(len(matriz_resultado)): 
            for j in range(len(matriz_resultado[i])): 
                print (f"{matriz_resultado[i][j]:4}", end = " ") 
            print (" ")
        continuar = input(Fore.GREEN + "Desea continuar: " +Fore.RESET )
        if continuar.lower() != "si":
            break                 
    #----------------------------------------------------------------------------------------------------------------------------------


      
