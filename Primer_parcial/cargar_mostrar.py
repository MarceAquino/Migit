from validaciones import *
from funciones_calculo import *
from lectura_escritura import*
lista_generos = [
        "Acción", "Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica",
        "Comedia dramática", "Crimen", "Documental", "Drama", "Fantasía", "Histórico",
        "Infantil", "Musical", "Misterio", "Policíaco", "Romance", "Ciencia ficción",
        "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental",
        "Familiar", "Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe",
        "Melodrama", "Erótico", "Cine independiente", "Zombies", "Vampiros", "Cyberpunk",
        "Steampunk", "Distopía", "Utopía", "Road Movie", "Docuficción", "Mockumentary",
        "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"
    ]

#--------------------------------------------------------------------------------------------
def imprimir_generos(lista_generos)->None:

    columnas = 5
    ancho_celda = 20
    tabla = ""
    contador = 0
    while contador < len(lista_generos):
        fila = ""
        for i in range(columnas):
            if contador < len(lista_generos):
                genero = lista_generos[contador]
                genero_ajustado = genero + " " * (ancho_celda - len(genero))
                fila += genero_ajustado
                contador += 1
        tabla += fila + "\n"
        
    print("\n=================== Listado de todos los generos disponibles =====================")
    print(f"\n{tabla}")
    genero = cargar_genero (lista_generos)
    return genero.capitalize() 
lista_peliculas = cargar_peliculas_csv("peliculas_3.csv")
#------------------------------------------------------------------------------
def cargar_genero(lista_genero:list) -> str:  

    genero = input("\nIngrese el género de la película: ")
    validar = validar_genero(genero, lista_genero)
    while validar != True:
        print("\n¡¡Error el género ingresado no existe!!\n")
        genero = input("Ingrese el género de la película nuevamente: ")
        validar = validar_genero(genero, lista_genero)
    return genero
#------------------------------------------------------------------------------
def cargar_titulo(lista_peliculas:list[dict])->str:

    titulo = input("\nIngresar el titulo de la pelicula: ")
    validar = validar_titulo(titulo,lista_peliculas)
    while validar != True:
        print("\n¡¡Error el titulo ingresado ya se encuentra en el sistema!!\n")
        titulo = input("Ingresar el titulo de la pelicula nuevamente: ")
        validar = validar_titulo(titulo,lista_peliculas)
    return titulo.capitalize()    
#------------------------------------------------------------------------------
def cargar_anio_lanzamiento()->int:

    anio = input("\nIngrese el año de la pelicula: ")
    validar = validar_anio(anio)
    while validar != True:
        print("\n¡¡Error año de la pelicula fuera de rango o erronea verifique!!\n")
        anio = input("Ingrese el año de la pelicula nuevamente: ")
        validar = validar_anio(anio)
    anio = int(anio)    
    return anio
#--------------------------------------------------------------------------------------------
def cargar_duracion()->int:

    duracion = input("\nIngrese la duracion de la pelicula: ")
    validar = validar_duracion(duracion)
    while validar != True:
        print("\n¡¡Error duracion de la pelicula fuera de rango/invalida ingresar en minutos!!\n")
        duracion = input("Ingrese la duracion de la pelicula: ")
        validar = validar_duracion(duracion)
    duracion = int(duracion)
    return duracion   
#--------------------------------------------------------------------------------------------
def cargar_atp()->bool:

    validacion = False
    atp= input("\nLa pelicula es ATP si/no: ")
    while atp.lower() != "si" and atp.lower() != "no":
        print("\n¡¡Error ingrese si/no reitente nuevamente: !!\n")
        atp= input("La pelicula es ATP si/no: ")
        atp = atp.lower()
    if atp != "si":
        validacion = True
   
    return validacion    
#--------------------------------------------------------------------------------------------
def cambiar_atp():
    if cargar_atp() != True:
        atp = "si"
    else:
        atp = "no"    
    return atp.capitalize()
#--------------------------------------------------------------------------------------------
def cargar_plataforma()->str:

    lista_plataformas = []

    while True:

        plataforma = input("Porfavor ingrese la/las plataforma de la pelicula: ")
        validar = validar_plataforma(plataforma)


        while validar != True:
            print("\n¡Error verifique que no tenga mas de 20 caracteres y la misma no contenga numeros ")
            plataforma = input("Porfavor ingrese la/las plataforma de la pelicula: ")
            validar = validar_plataforma(plataforma)

        lista_plataformas.append(plataforma.capitalize()) 

        opcion = input("¿Desea agregar otra plataforma para la pelicula ? si/no: ")    
        if opcion.lower() == "si":
            pass
        else:
            return lista_plataformas
#--------------------------------------------------------------------------------------------
def cargar_pelicula(lista_peliculas:list[dict])->dict:

    id_actual = obtener_maximo_minimo(lista_peliculas,"id",True) + 1
    titulo = cargar_titulo(lista_peliculas)
    genero = imprimir_generos(lista_generos)
    anio_lanzamiento = cargar_anio_lanzamiento()
    duracion = cargar_duracion()
    atp = cambiar_atp()  
    plataforma = cargar_plataforma()    
    

    pelicula = {
        "id": id_actual,
        "titulo": titulo,
        "genero": genero,
        "año_de_lanzamiento": anio_lanzamiento,
        "duracion": duracion,
        "atp":atp,
        "plataformas":plataforma
     }
    lista_peliculas.append(pelicula)
    
    print(f"\n¡La pelicula con el ID: {pelicula['id']} fue agregado exitosamente!{pelicula}")   
#--------------------------------------------------------------------------------------------
def crear_lista_plataformas(lista_peliculas:list[dict]):
    lista_plataformas = []
    for pelicula in lista_peliculas:
        for plataforma in pelicula["plataformas"]:
            if plataforma not in lista_plataformas:
                lista_plataformas.append(plataforma)
    return lista_plataformas


def crear_lista_genero(lista_peliculas:list[dict])->list:
    lista_generos_csv = []
    for i in range(len(lista_peliculas)):
        genero = lista_peliculas[i]["genero"]
        lista_generos_csv.append(genero)
    lista_generos_csv = set(lista_generos_csv)
    lista_generos_csv = list(lista_generos_csv)
    return lista_generos_csv


def crear_lista_por_plataforma(lista_peliculas: list[dict]) -> list[dict]:
    lista_filtrada = []
    plataforma = input("Ingrese la plataforma: ").strip()
    
    for pelicula in lista_peliculas:
        if plataforma in pelicula.get("plataformas"):
            lista_filtrada.append(pelicula)
    
    return lista_filtrada

#--------------------------------------------------------------------------------------------   
def mostrar_peliculas(pelicula: dict) -> None:
   
    longitud_titulo = 52 - len(str(pelicula['titulo']))
    longitud_genero = 28 - len(pelicula['genero'])
    longitud_año = 23 - len(str(pelicula['año_de_lanzamiento']))
    longitud_duracion = 11 - len(str(pelicula['duracion']))
    longitud_plataformas = 27 - len(str(pelicula['plataformas']))

    titulo = pelicula['titulo'] + ' ' * (longitud_titulo)
    genero = pelicula['genero'] + ' ' * (longitud_genero)
    año = str(pelicula['año_de_lanzamiento']) + ' ' * (longitud_año)
    duracion = str(pelicula['duracion']) + ' ' * (longitud_duracion)
    if pelicula['atp'] == "Si":
        atp = "Si"
    else:
        atp = "No"
    plataformas = pelicula.get('plataformas')

    if type(plataformas) == list:
                plataformas = "-".join(plataformas)

    plataformas = str(pelicula['plataformas']) + ' ' * (longitud_plataformas)            
    
    mensaje = f"| {titulo} | {genero} | {año} | {duracion} | {atp} | {plataformas} |"
    print(mensaje)
#--------------------------------------------------------------------------------------------
def imprimir_peliculas(lista_peliculas: list[dict],clave:str,criterio:str) -> None:

    if clave == "plataformas":
        lista_peliculas = crear_lista_plataformas(lista_peliculas)

    vacio = " " * 6
    mensaje = "*" * 162
    print(mensaje)
    primeros = f"\n|{vacio*4}Título{vacio*4}|{vacio*2}Género{vacio*2}"
    segundo = f"|Año de lanzamiento{vacio}|Duración{vacio}|ATP |{vacio}Plataformas{vacio*2}|"
    print(f"{primeros}{segundo}")
    print(mensaje)

    bandera_imprimir = False

    for pelicula in lista_peliculas:
        if clave != None and clave != "plataformas":
            if str(pelicula.get(clave, "")) == str(criterio):
                mostrar_peliculas(pelicula)
                bandera_imprimir = True
        elif clave == "plataformas":
            mostrar_peliculas(pelicula)
            bandera_imprimir = True
        else:
            mostrar_peliculas(pelicula)
            bandera_imprimir = True    

    if not bandera_imprimir:
        print("\n No se encontraron películas!! \n")
                
    print(mensaje)
#--------------------------------------------------------------------------------------------  
def ordenar_peliculas(lista_peliculas:list[dict],clave:str)->None:
    while True:
        print("\nIngrese a/b para ordenar las peliculas de manera asendente o desendente\n")
        criterio = input("Desea ordenar las peliculas de manera asendente o desendente: ")
        if criterio == "a":
            bubble_sort(lista_peliculas,clave,True)
            imprimir_peliculas(lista_peliculas,None,None)
            break
        elif criterio == "b":
            bubble_sort(lista_peliculas,clave,False)  
            imprimir_peliculas(lista_peliculas,None,None)
            break
        else:
            print("Error opcion no valida seleccione a/b:")              
#--------------------------------------------------------------------------------------------



