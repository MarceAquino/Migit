"""1)Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
2)Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
3)Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
4)Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
5)Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
6)Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo.
La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados."""
#---------------------------------------------------------------------------------------------------------------
lista = [5,80,-8,10,80,2,-50,80]
longitud_lista = len(lista)

def calcular_numero_entero (lista:list)->int:
    suma_enteros = 0

    for i in range(longitud_lista):

        suma_enteros += lista[i]
        promedio = round(suma_enteros / longitud_lista,2)

    return promedio   

promedio = calcular_numero_entero(lista)
print (f"El promedio de numero enteros es: {promedio}")
#---------------------------------------------------------------------------------------------------------------
def calcular_numero_entero (lista:list)->int:
    suma_positivos = 0
    cantidad_positivos = 0

    for i in range(longitud_lista):
        
        if lista[i] > 0:
            cantidad_positivos += 1
            suma_positivos += lista[i]
            promedio = round(suma_positivos / cantidad_positivos,2)
           
    return promedio   

promedio = calcular_numero_entero(lista)
print (f"El promedio de numero enteros es: {promedio}")
#---------------------------------------------------------------------------------------------------------------
def calcular_producto (lista:list)->int:
   
    producto = 1
    for i in range(longitud_lista):
        producto *= lista[i]
    return producto   

        
producto = calcular_producto(lista)
print (f"El producto de numero enteros es: {producto}")    

#---------------------------------------------------------------------------------------------------------------   
def encontrar_indice_max (lista:list):
    
    bandera = True
    for i in range(longitud_lista):

        if bandera == True or numero_max < lista[i]:
            bandera = False
            numero_max = lista[i]
            indice_max = i   
            mensaje = (f"El numero max es: {numero_max}, su indice es: {indice_max}")

    return mensaje

maximo = encontrar_indice_max(lista)
print (maximo) 
#---------------------------------------------------------------------------------------------------------------    
def encontrar_indice_max (lista:list):
    bandera = True
    for i in range(longitud_lista):

        if bandera == True or numero_max < lista[i]:
            bandera = False
            numero_max = lista[i]
            indices_maximos = i

        elif numero_max == lista[i] :          
            indices_maximos = (f"{indices_maximos}, {i}") 

    mensaje = f"El número máximo es: {numero_max}, sus índices son: {indices_maximos}"
    
    return mensaje
         
maximo = encontrar_indice_max(lista)
print(maximo)
   


#---------------------------------------------------------------------------------------------------------------
lista_nombres = ["Juan", "María", "Luis", "Ana", "Pedro", "María", "Carlos"]

def reemplazar_nombres (lista_nombres:list,nombre_buscado:str, reemplazo:str) -> list:

    contador_reemplazo = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_buscado:
            contador_reemplazo += 1
            lista_nombres[i] = reemplazo                 
    return contador_reemplazo    


contador_reemplazo = reemplazar_nombres(lista_nombres, "María" ,"Sabri")  
print (f"La cantidad de reemplazos fueron: {contador_reemplazo} y la lista final es {lista_nombres}")
#---------------------------------------------------------------------------------------------------------------


# MEJORADOS 


# """1)Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
# 2)Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
# 3)Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
# 4)Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
# 5)Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
# 6)Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo.
# La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados."""
# #---------------------------------------------------------------------------------------------------------------
lista = [5,80,-8,10,80,2,-50,80]


def calcular_promedio (lista:list)->int|float:
    suma_enteros = 0

    for i in range(len(lista)):

        suma_enteros += lista[i]
    promedio = round(suma_enteros / len(lista),2)

    return promedio   

promedio = calcular_promedio (lista)
print (f"El promedio de numero enteros es: {promedio}")
#---------------------------------------------------------------------------------------------------------------
def calcular_promedio_positivos (lista:list)->int|float:
    suma_positivos = 0
    cantidad_positivos = 0
    promedio = 0

    for i in range(len(lista)):
        
        if lista[i] > 0:
            cantidad_positivos += 1
            suma_positivos += lista[i]
    
    if promedio > 0:
        promedio = round(suma_positivos / cantidad_positivos,2)    
    return promedio   


promedio = calcular_promedio_positivos(lista)
print (f"El promedio de numero enteros es: {promedio}")
#---------------------------------------------------------------------------------------------------------------
def calcular_producto (lista:list)->int:
   
    producto = 1
    for i in range(len(lista)):
        producto *= lista[i]
    return producto   

        
producto = calcular_producto(lista)
print (f"El producto de numero enteros es: {producto}")    

#---------------------------------------------------------------------------------------------------------------   
def encontrar_posicion_max (lista:list)->int:
    
    for i in range(len(lista)):

        if i == 0 or numero_max < lista[i]:
            numero_max = lista[i]
            indice_max = (i + 1)   
           

    return indice_max

maximo = encontrar_posicion_max (lista)
print (maximo) 
#---------------------------------------------------------------------------------------------------------------    
def encontrar_posiciones_max (lista:list)-> None:
    
    for i in range(len(lista)):

        if i == 0 or numero_max < lista[i]:
            numero_max = lista[i]

    for i in range(len(lista)): 
        
        if numero_max == lista[i]:
            posicion = i + 1
            print (f"El numero maximo es {numero_max} y se encuentra en la posicion {posicion}")   
        
encontrar_posiciones_max(lista)

#---------------------------------------------------------------------------------------------------------------
lista_nombres = ["Juan", "María", "Luis", "Ana", "Pedro", "María", "Carlos"]

def reemplazar_nombres (lista_nombres:list,nombre_buscado:str, reemplazo:str) -> int:

    contador_reemplazo = 0
    for i in range(len(lista_nombres)):

        if lista_nombres[i] == nombre_buscado:
            lista_nombres[i] = reemplazo                 
            contador_reemplazo += 1

    return contador_reemplazo    

contador_reemplazo = reemplazar_nombres(lista_nombres, "María" ,"Sabri")  
print (f"La cantidad de reemplazos fueron: {contador_reemplazo} y la lista final es {lista_nombres}")
#---------------------------------------------------------------------------------------------------------------


    
    


   


            
            

    
    


   


            
            
