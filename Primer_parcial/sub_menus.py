from validaciones import*
from modificar_eliminar import *
from cargar_mostrar import * 

#----------------------------------------------------------------------------------------------------------------
def mostrar_submenu_modificar()->None:
    
    print("""
        a. Modificar el titulo de la pelicula.
        b. Modificar genero de la pelicula.
        c. Modificar año de lanzamiento de la pelicula.
        d. Modificar duracion de la pelicula.
        e. Modificar atp de la pelicula.
        f. Modificar plataforma/s de la pelicula.    
        g. Salir
        """)    
#----------------------------------------------------------------------------------------------------------------   
def submenu_modificar(lista_peliculas:list[dict])->None:

    print("\n¡Bienvenido al menu de modificaciones!\n")
    
    retorno = ""
    bandera = False
    pelicula_a_modificar = ingresar_pelicula_a_modificar(lista_peliculas)
    while True:
        mostrar_submenu_modificar()
        opcion = input("ingrese una opcion valida de la entre la 'a' y la 'g': ")
        match opcion.lower():
            case "a":
                modificar_dato(lista_peliculas,pelicula_a_modificar,"titulo",cargar_titulo(lista_peliculas))
                print("\nSe realizo un cambio en el titulo ingrese el nuevo titulo para continuar: \n")
                pelicula_a_modificar = ingresar_pelicula_a_modificar(lista_peliculas)
            case "b":
                modificar_dato(lista_peliculas,pelicula_a_modificar,"genero",imprimir_generos(lista_generos))
                bandera = True
            case "c":
                modificar_dato(lista_peliculas,pelicula_a_modificar,"año_de_lanzamiento",cargar_anio_lanzamiento())
                bandera = True
            case "d":
                modificar_dato(lista_peliculas,pelicula_a_modificar,"duracion",cargar_duracion())
                bandera = True
            case "e":
                modificar_dato(lista_peliculas,pelicula_a_modificar,"atp",cambiar_atp())
                bandera = True
            case "f":
                nueva_plataforma = cargar_plataforma()
                modificar_dato(lista_peliculas, pelicula_a_modificar, "plataformas", nueva_plataforma)
                bandera = True       
            case "g":
                continuar = input("¿Desea salir? si/no: ")
                if continuar == "si":
                    if bandera == False:
                        retorno = print("No se realizaron cambios.")
                    else:
                        retorno = retorno
                    return retorno    
            case _:
                print("No es una opcion válida")             
#---------------------------------------------------------------------------------------------------------------- 
def mostrar_submenu_mostrar()->None:
    
    print("""
        a. Mostrar Todas las peliculas.
        b. Mostrar peliculas por genero.
        c. Mostrar peliculas por año.
        d. Mostrar peliculas Atp
        e. Mostrar peliculas No Atp. 
        f. Mostrar peliculas por plataforma.    
        g. Salir
        """)   
#----------------------------------------------------------------------------------------------------------------                      
def submenu_mostrar_peliculas(lista_peliculas:list[dict])->None:

    print("\n¡Bienvenido al menu mostrar pelicuolas!\n")
    
    
    while True:
        mostrar_submenu_mostrar()
        opcion = input("ingrese una opcion valida de la entre la 'a' y la 'g': ")
        match opcion:
            case "a":
                imprimir_peliculas(lista_peliculas,None,None)
            case "b":
                imprimir_peliculas(lista_peliculas,"genero",imprimir_generos(lista_generos))
            case "c":
                imprimir_peliculas(lista_peliculas,"año_de_lanzamiento",cargar_anio_lanzamiento())
            case "d":
                imprimir_peliculas(lista_peliculas,"atp","Si")
            case "e":
                imprimir_peliculas(lista_peliculas,"atp","No") 
            case "f":
                imprimir_peliculas(lista_peliculas,"plataformas",None)       
            case "g":
                continuar = input("¿Desea salir? si/no: ")
                if continuar == "si":
                    break
            case _:
                print("No es una opcion válida")         
#---------------------------------------------------------------------------------------------------------------- 
def mostrar_submenu_ordenar_peliculas()->None:
    
    print("""
        a. Ordenar peliculas por titulo.
        b. Ordenar peliculas por genero.
        c. Ordenar peliculas por año.
        d. Ordenar peliculas por duracion.  
        e. Salir
        """)   
#----------------------------------------------------------------------------------------------------------------     
def submenu_ordenar_peliculas(lista_peliculas:list[dict])->None:

    print("\n¡Bienvenido al menu de ordenar peliculas!\n")
    
    while True:
        mostrar_submenu_ordenar_peliculas()
        opcion = input("ingrese una opcion valida de la entre la 'a' y la 'e': ")
        match opcion:
            case "a":
                ordenar_peliculas(lista_peliculas,"titulo")
            case "b":
                ordenar_peliculas(lista_peliculas,"genero")
            case "c":
                ordenar_peliculas(lista_peliculas,"año_de_lanzamiento")
            case "d":
                ordenar_peliculas(lista_peliculas,"duracion")   
            case "e":
                continuar = input("¿Desea salir? si/no: ")
                if continuar == "si":
                    break
            case _:
                print("No es una opcion válida")  
#----------------------------------------------------------------------------------------------------------------  
def mostrar_submenu_calcular_promedio()->None:
    
    print("""
        a. Calcular promedio por año de lanzamiento.
        b. Calcular promedio por duracion de las peliculas. 
        c. Salir
        """)                  
#----------------------------------------------------------------------------------------------------------------      
def submenu_calcular_promedio(lista_peliculas:list[dict])->None:

    print("\n¡Bienvenido al menu de promedios!\n")
    
    while True:
        mostrar_submenu_calcular_promedio()
        opcion = input("ingrese una opcion valida entre la 'a' y la 'c': ")
        match opcion:
            case "a":
                calcular_promedio(lista_peliculas,"año_de_lanzamiento")
            case "b":
                calcular_promedio(lista_peliculas,"duracion")   
            case "c":
                continuar = input("¿Desea salir? si/no: ")
                if continuar == "si":
                    break  
            case _:
                print("No es una opcion válida")                  
#----------------------------------------------------------------------------------------------------------------      
def mostrar_submenu_calcular_porcentaje()->None:
    
    print("""
        a. Calcular porcentaje por genero.
        b. Calcular porcentaje por Atp.  
        c. Salir
        """)   
#----------------------------------------------------------------------------------------------------------------    
def submenu_calcular_porcentaje(lista_peliculas:list[dict])->None:

    print("\n¡Bienvenido al menu calcular porcentaje!\n")
    
    while True:
        mostrar_submenu_calcular_porcentaje()
        opcion = input("ingrese una opcion valida entre la 'a' y la 'c': ")
        match opcion:
            case "a":
                calcular_porcentaje(lista_peliculas,"Si")
            case "b":
                calcular_porcentaje(lista_peliculas,cargar_genero(lista_generos))   
            case "c":
                continuar = input("¿Desea salir? si/no: ")
                if continuar == "si":
                    break    
            case _:
                print("No es una opcion válida")  

        