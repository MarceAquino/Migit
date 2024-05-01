
    
#----------------------------------------------------------------------------------------------------------------------      
matriz = [[2,3,4],
          [4,8,9],
          [1,2,3]]
#----------------------------------------------------------------------------------------------------------------------  
#print (matriz) no 
#matriz [2][2] = 3 fila columna

#----------------------------------------------------------------------------------------------------------------------  
#imprimir matriz
for i in range(len(matriz)): 
    for j in range(len(matriz[i])): 
      print (f"{matriz[i][j]:4}", end = " ") 
    print(" ")  
#----------------------------------------------------------------------------------------------------------------------  

#crear matriz del cualquier tamaño vacia 
m = 2
n = 2
                #columnas       #filas 
matriz_vacia = [[0]*m     for _ in range(n)] 

for i in range(len(matriz_vacia)): 
    for j in range(len(matriz_vacia[i])): 
      print (matriz_vacia[i][j], end = " ") 
    print(" ")  

for i in range(len(matriz_vacia)): 
    for j in range(len(matriz_vacia[i])): 
      matriz_vacia [i][j] = int(input (f"Ingrese un numero a cargar en la fila {i+1} y en la columna {j+1}: "))


for i in range(len(matriz_vacia)): 
    for j in range(len(matriz_vacia[i])): 
            # :4 deja lugar adelante para ser mas legible la matriz 
      print (f"{matriz_vacia[i][j]:4}", end = " ") 
    print(" ")        

#----------------------------------------------------------------------------------------------------------------------       
#recorrido por columnas 
matriz = [[2,3,4,5],
          [4,8,9,6],
          [1,2,3,7]]

# el len toda el valor de la primer lista determina la cantidad de columnas
for j in range(len(matriz[0])): 
    print (f"Columna: {j+1}")
    # el len de matriz determina la cantidad de listas seria la cantidad de filas
    for i in range(len(matriz)): 
       print (matriz[i][j])     

#----------------------------------------------------------------------------------------------------------------------       
def mostrar_matriz (matriz:list) -> None:

  for i in range(len(matriz)): 
    for j in range(len(matriz[i])): 
          # :4 deja lugar adelante para ser mas legible la matriz 
      print (f"{matriz[i][j]:4}", end = " ") 
    print(" ")             
#----------------------------------------------------------------------------------------------------------------------   
#multiplicar matriz por numero escalar 


escalar = 5
matriz = [[2,3,4,5],
          [4,8,9,6],
          [1,2,3,7]]

for i in range(len(matriz)): 
  for j in range(len(matriz[i])):
    #guardo en cada columna y fila el nuevo valor lo voy pisando 
    matriz[i][j] *= escalar 

mostrar_matriz(matriz)
#----------------------------------------------------------------------------------------------------------------------  
#suma de matriz 

matriz_a = [[2,3,4,5],
          [4,8,9,6],
          [1,2,3,7]]

matriz_b = [[2,3,4,5],
          [4,8,9,6],
          [1,2,3,7]]

matriz_resultado =[[0]*3 for _ in range(4)]

for i in range(len(matriz_a)): 
  for j in range(len(matriz_a[i])):
    #guardo en cada columna y fila el nuevo valor lo voy pisando 
    matriz_resultado = matriz_a[i][j] + matriz_b[i][j]

mostrar_matriz(matriz_a)    
#----------------------------------------------------------------------------------------------------------------------

