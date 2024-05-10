#algoritmo de ordenamiento de lista ordenamiento por burbujeo


 
#       0 1 2 3 4 5 6 7    indices             
lista =[3,1,8,7,5,6,4,9,10]

def mostrar_lista(lista:list)->None:
    for i in range(len(lista)): # el primer for intera la cantidad de elementos de la lista la formula de bubble es n - 1 siendo n la cantidad de elementos de la lista # se le resta 1 para no comparar el ultimo con nada. 
        print(lista[i], end="")
            #intercambio

def bubble_sort(lista:list):
    for i in range(len(lista)):
        for j in range (len(lista)-1-i): # el primer for intera la cantidad de elementos de la lista. 
            	                        # la formula de bubble es n - 1 siendo n la cantidad   
                                        # se le resta -i para que en cada iteracion reste el indice para q no siga comparando de mas.  
            if lista[j] > lista[j+1]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
     

def bubble_sort_2(lista:list):
    for i in range(len(lista)):
        intercambio = False
        for j in range (len(lista)-1-i): # el primer for intera la cantidad de elementos de la lista. 
            	                        # la formula de bubble es n - 1 siendo n la cantidad   
                                        # se le resta -i para que en cada iteracion reste el indice para q no siga comparando de mas.  
            if lista[j] > lista[j+1]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
                intercambio = False
        if (intercambio == False):
            break      

def bubble_sort_3(lista:list):
    bandera = True
    while bandera == True:
        bandera = False
        for j in range (len(lista)-1): # el primer for intera la cantidad de elementos de la lista. 
                                        # la formula de bubble es n - 1 siendo n la cantidad   
                                        # se le resta -i para que en cada iteracion reste el indice para q no siga comparando de mas.  
            if lista[j] > lista[j+1]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
                bandera = True
                   
mostrar_lista(lista)
print("-------------------")
bubble_sort(lista)
mostrar_lista(lista)
bubble_sort_2(lista)
mostrar_lista(lista)
bubble_sort_3(lista)
mostrar_lista(lista)

def insertion_sort(lista):
    # Recorremos la lista empezando desde el segundo elemento hasta el final.
    for i in range(1, len(lista)):
        # Guardamos el valor del elemento actual que vamos a insertar.
        intercambio = lista[i]
        # Inicializamos el índice del elemento anterior al que estamos considerando.
        rastreador = i - 1
        # Comenzamos a buscar la posición correcta para insertar el elemento actual.
        # Mientras el rastreador sea mayor o igual a cero y el elemento en la posición del rastreador
        # sea mayor que el elemento que queremos insertar, movemos los elementos hacia la derecha.
        while rastreador >= 0 and lista[rastreador] > intercambio:
            lista[rastreador + 1] = lista[rastreador]
            rastreador -= 1
        # Insertamos el elemento en su posición correcta.
        lista[rastreador + 1] = intercambio

# Lista de ejemplo
lista = [10, 7, 13, 5, 6]
# Llamamos a la función de ordenamiento
insertion_sort(lista)
# Imprimimos la lista ordenada
print("Sorted array is:", lista)