
#------------------------------------------------------------------------------------------------------------------------ 
def obtener_maximo_minimo(lista_peliculas:list,clave:str,condicion:bool)->int|float|bool:
    base = None
    bandera = True
    mensaje = False
    for i in range(len(lista_peliculas)):
        dato = lista_peliculas[i].get(clave)
        tipo_de_dato = type(lista_peliculas[i].get(clave))
        if dato != None:
            if tipo_de_dato == int or tipo_de_dato == float:
                if condicion == True:    
                    if bandera == True or dato > base:
                        base = dato
                        mensaje = base
                        bandera = False 
                else:
                     if bandera == True or dato < base:
                        base = dato
                        mensaje = base
                        bandera = False 
    return mensaje
#------------------------------------------------------------------------------------------------------------------------ 
def bubble_sort(lista_peliculas: list[dict],clave: str,criterio: bool) -> None:
    if clave == "duracion":
        for i in range(len(lista_peliculas)):
            lista_peliculas[i][clave] = int(lista_peliculas[i][clave])
    for i in range(len(lista_peliculas)):
        intercambio = False
        for j in range(len(lista_peliculas) - 1 - i):
            if criterio == True:
                if lista_peliculas[j][clave] > lista_peliculas[j + 1][clave]:
                    auxiliar = lista_peliculas[j]
                    lista_peliculas[j] = lista_peliculas[j + 1]
                    lista_peliculas[j + 1] = auxiliar
                    intercambio = True
            else:
                if lista_peliculas[j][clave] < lista_peliculas[j + 1][clave]:
                    auxiliar = lista_peliculas[j]
                    lista_peliculas[j] = lista_peliculas[j + 1]
                    lista_peliculas[j + 1] = auxiliar
                    intercambio = True
        if intercambio != True:
            break

       
#------------------------------------------------------------------------------------------------------------------------ 
def obtener_dato(pelicula:dict,clave:str)->str|bool:   
    longitud = len(pelicula)
    if longitud < 0:
        mensaje = False
    else:    
        mensaje = pelicula.get(clave)
    return mensaje
#------------------------------------------------------------------------------------------------------------------------  
def sumar_dato_peliculas(lista_pelicula:dict,clave:str)-> int|float:
    suma = 0
    for i in range(len(lista_pelicula)):
        if type(lista_pelicula[i]) == dict:
            dato = int(obtener_dato(lista_pelicula[i],clave))
            if dato != None :
                suma += dato                 
    return suma
#------------------------------------------------------------------------------------------------------------------------ 
def dividir(dividendo: float, divisor: float) -> float:
    mensaje_resultado = False
    if divisor != 0:
        mensaje_resultado = dividendo / divisor
    return mensaje_resultado
#------------------------------------------------------------------------------------------------------------------------ 
def calcular_promedio(lista_pelicula:list,clave:str) -> None:
    suma = sumar_dato_peliculas(lista_pelicula,clave)
    cantidad_peliculas = len(lista_pelicula)
    promedio = dividir(suma,cantidad_peliculas)
    print(promedio)
#------------------------------------------------------------------------------------------------------------------------ 
def calcular_porcentaje(lista_peliculas:list[dict],clave:str)->None:   
    contador_atp = 0
    contador_no_atp = 0  
    for i in range(len(lista_peliculas)):   
        if lista_peliculas[i][clave].get() == ["si"]:
            contador_atp += 1
        else:
            contador_no_atp += 1                
#------------------------------------------------------------------------------------------------------------------------ 
def calcular_porcentaje(lista_peliculas: list[dict], criterio: str) -> str:

    contador_atp = 0
    contador_no_atp = 0
    contador_genero = 0
    bandera = True

    for pelicula in lista_peliculas:
        if pelicula["genero"] == criterio:
            contador_genero += 1
            bandera = False
            
        if pelicula["atp"] == "Si":
            contador_atp += 1

        else:
            contador_no_atp += 1

    total = contador_atp + contador_no_atp
    if bandera == False:
        porcentaje_genero = (contador_genero / total) * 100
        mensaje = f"El {porcentaje_genero}% son del género: {criterio}"
    else:
        porcentaje_atp = (contador_atp / total) * 100
        porcentaje_no_atp = (contador_no_atp / total) * 100
        mensaje = f"El {porcentaje_atp}% son películas ATP y el {porcentaje_no_atp}% son no ATP."

    print (mensaje)
#------------------------------------------------------------------------------------------------------------------------ 