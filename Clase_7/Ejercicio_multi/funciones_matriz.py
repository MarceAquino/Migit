from colorama import init, Fore
#----------------------------------------------------------------------------------------------------------------------------------
def crear_matriz (filas:int,columnas:int)-> list:

    """Crea una matriz de tamaño especificado y la llena con valores proporcionados por el usuario.
    Parámetros:
        filas (int): El número de filas de la matriz.
        columnas (int): El número de columnas de la matriz.
    Retorna:
        list: La matriz creada con valores ingresados por el usuario."""
    
    filas = int(filas)
    columnas = int(columnas)
    nueva_matriz = [[0]*columnas    for _ in range(filas)]  
    for i in range(len(nueva_matriz)): 
        for j in range(len(nueva_matriz[i])): 
            nueva_matriz [i][j] = int(input (Fore.GREEN+ f"Ingrese un numero a cargar en la fila {i+1} y en la columna {j+1}: " +Fore.RESET))
    return nueva_matriz 
       
#----------------------------------------------------------------------------------------------------------------------------------
def validar_matriz (matriz:list,filas:str)-> int:
     
    """Determina el número de filas o columnas en una matriz basada en una cadena de entrada.
    Parámetros:
        matriz (list): La matriz de la cual se determinará el número de filas o columnas.
        filas (str): La cadena que indica si se deben validar las filas o columnas.
    Retorna:
        int: El número de filas o columnas de la matriz, dependiendo de la cadena de entrada."""
    
    if filas == "filas":
        for i in range(len(matriz)):
            filas = (i+1) 
        return filas
    else:
        for j in range(len(matriz[0])): 
            columnas = (j+1)    
        return columnas
    
#----------------------------------------------------------------------------------------------------------------------------------
def multiplicar_matriz (matriz_a:list,matriz_b:list,matriz_resultado:list)->list:
    """Realiza la multiplicación de matrices entre dos matrices dadas.
    Parámetros:
        matriz_a (list): La primera matriz a multiplicar.
        matriz_b (list): La segunda matriz a multiplicar.
        matriz_resultado (list): La matriz en la que se almacenará el resultado de la multiplicación.
    Retorna:
        list: La matriz resultante de la multiplicación."""
    
    for i in range(len(matriz_a)): #Recorre las filas de A
        for j in range (len(matriz_b[0])): # Recorre las columnas de B
            for k in range(len(matriz_b)): # Recorre las filas de B y opera 
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
                print (matriz_resultado)
    return matriz_resultado            
#----------------------------------------------------------------------------------------------------------------------------------

       
    
    # for i in range(len(matriz1)):
    #     fila = []
    #     for j in range(len(matriz2[0])):
    #         suma = 0
    #         for k in range(len(matriz2)):
    #             suma += matriz1[i][k] * matriz2[k][j]
    #         fila += [suma]
    #     resultado += [fila]
    # return resultado