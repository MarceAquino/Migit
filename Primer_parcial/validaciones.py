         
#------------------------------------------------------------------------------
def validar_titulo(titulo:str,lista_peliculas:list[dict])->bool:
    longitud = len(titulo)
    validacion = True
    if longitud > 30 or longitud == 0:
        validacion = False
    if validacion == True:
        for i in range(len(lista_peliculas)):
            if lista_peliculas[i]["titulo"] == titulo:
                validacion = False
                break
    return validacion


#------------------------------------------------------------------------------          
def validar_genero(genero:str,lista_genero:list)->bool:

    validacion = False
    for i in range(len(lista_genero)):
        if genero.capitalize() == lista_genero[i]:
            validacion = True
            break

    return validacion
#------------------------------------------------------------------------------
def validar_anio(anio:str)->bool:

    validar_anio = True
    longitud = len(anio)
    if longitud > 4:
       validar_anio = False
    validar_entero = anio.isnumeric()
    if validar_entero == True:
        anio = int(anio)   
        if anio < 1888 or anio > 2024:
            validar_anio = False   
        else:
            validar_anio = True           
    else:
        validar_anio = False
    return validar_anio

#------------------------------------------------------------------------------
def validar_duracion(duracion:str)->int|bool:

    validar_duracion = True
    validar_entero = duracion.isnumeric()
    if validar_entero == True:
        duracion = int(duracion)
        if duracion < 1:
            validar_duracion = False
        else:
            validar_duracion = True   
    else:
        validar_duracion = False        
   
    return validar_duracion    
#------------------------------------------------------------------------------
def validar_plataforma(plataforma: str) -> bool:

    validar_plataforma = True
    if len(plataforma) > 20 or len(plataforma) < 1:
        validar_plataforma = False   
    for i in range(len(plataforma)):
        if plataforma[i].isdigit() == True:
            validar_plataforma = False

    return validar_plataforma 
#------------------------------------------------------------------------------
def validar_existecia_de_pelicula(lista_peliculas:list[dict],titulo:str)->bool:

    pelicula_encontrada = False
    for i in range(len(lista_peliculas)):
        if titulo.capitalize() == lista_peliculas[i].get("titulo"):
            pelicula_encontrada = True

    return pelicula_encontrada
#------------------------------------------------------------------------------
        





        

    
        



    
