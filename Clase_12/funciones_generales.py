
#------------------------------------------------------------------------------------------------------------------------
def stark_normalizar_datos(Lista_heroes)->None|bool :
    bandera = False
    longitud = len(Lista_heroes)
    if longitud > 0:
        for i in range(len(Lista_heroes)):
            if Lista_heroes [i] == {}:
                continue
            if type(Lista_heroes[i]["fuerza"]) != int :   
                fuerza = int(Lista_heroes[i]["fuerza"])
                bandera = True
                Lista_heroes[i]["fuerza"] = fuerza
            if type(Lista_heroes[i]["altura"]) != float :
                altura = float(Lista_heroes[i]["altura"])
                bandera = True
                Lista_heroes[i]["altura"] = altura
            if type((Lista_heroes[i]["peso"])) != float:      
                peso = float(Lista_heroes[i]["peso"])
                bandera = True  
                Lista_heroes[i]["peso"] = peso   

    if bandera == True:         
        print("Datos Normalizados\n")
    else:   
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n")
               
        return bandera 
#------------------------------------------------------------------------------------------------------------------------       
def obtener_dato(heroe:dict,clave:str)->str|bool:
        
    longitud = len(heroe)
    if longitud < 0:
        mensaje = False
    else:    
        mensaje = heroe.get(clave)
    return mensaje
#------------------------------------------------------------------------------------------------------------------------     
def obtener_nombre(heroe:dict)->str|bool:

    longitud = len(heroe)
    if longitud < 0 and mensaje != False:
        mensaje_formateado = False
    else:    
        mensaje = obtener_dato(heroe,"nombre")
        mensaje_formateado = f"Nombre: {mensaje}" 
    return mensaje_formateado 
#------------------------------------------------------------------------------------------------------------------------ 
def obtener_nombre_dato(heroe:dict,clave:str)->str|bool:
    longitud = len(heroe)
    mensaje = heroe.get(clave)
    if longitud < 0 and mensaje != False:
        mensaje_formateado = False
    else:    
        atributo = obtener_dato(heroe,clave)
        

        mensaje_formateado = f" {obtener_nombre(heroe)} | {clave}: {atributo}" 
    return mensaje_formateado   
#------------------------------------------------------------------------------------------------------------------------  
def obtener_maximo(lista_heroes:list,clave:str)->int|float|bool:

    maximo = None
    bandera = True
    mensaje = False
    for i in range(len(lista_heroes)):
        dato = lista_heroes[i].get(clave)
        tipo_de_dato = type(lista_heroes[i].get(clave))
        if dato != None:
            if tipo_de_dato == int or tipo_de_dato == float:
                    if bandera == True or dato > maximo:
                        maximo = dato
                        mensaje = maximo
                        bandera = False                
    return mensaje
#------------------------------------------------------------------------------------------------------------------------   
def obtener_minimo(lista_heroes:dict,clave:str)->int|float|bool:

    minimo = None
    bandera = True
    mensaje = False
    for i in range(len(lista_heroes)):
        dato = lista_heroes[i].get(clave)
        if dato != None:
            tipo_de_dato = type(lista_heroes[i].get(clave))
            if tipo_de_dato == int or tipo_de_dato == float:
                    if bandera == True or dato < minimo :
                        minimo = dato
                        mensaje = minimo 
                        bandera = False                               
    return mensaje  
#------------------------------------------------------------------------------------------------------------------------ 
def obtener_dato_cantidad(lista_heroes:list,dato:int|float,clave:str)->list:
    lista_datos_heroes = []
    for i in range(len(lista_heroes)):
        buscador = lista_heroes[i].get(clave)
        if buscador == dato:
            lista_datos_heroes.append(lista_heroes[i])
           
    return lista_datos_heroes 
#------------------------------------------------------------------------------------------------------------------------   
def stark_imprimir_heroes(lista_heroes:list)->None:
    mensaje = False
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            for clave in heroe:  # Iterar sobre las claves del héroe
                valor = heroe[clave]  # Obtener el valor correspondiente a la clave
                clave = clave.capitalize()
                print(f"- {clave}: {valor}")
            mensaje = print()  # Imprimir una línea en blanco   
        return mensaje 
#------------------------------------------------------------------------------------------------------------------------ 
def mostrar_promedio_dato(lista_heroes:list,clave:str)->list:
    mensaje = False
    validad_cantidad = len(lista_heroes)
    if validad_cantidad > 0:
        for i in range (validad_cantidad):
            tipo_de_dato = type(lista_heroes[i].get(clave))
            if tipo_de_dato == int or tipo_de_dato == float:
                mensaje = True
        return mensaje 
#------------------------------------------------------------------------------------------------------------------------      












        




        
        


                 






   
    
       


        



