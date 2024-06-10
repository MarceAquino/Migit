from validaciones import*
from cargar_mostrar import*



#----------------------------------------------------------------------------------------------------------------
def modificar_dato(lista_peliculas:list[dict],titulo:str,clave:str,modificacion:str)->None:
    
    cambio_realizado = False
    for i in range(len(lista_peliculas)): 
        if cambio_realizado == False:
            if lista_peliculas[i]["titulo"] == titulo.capitalize():
                lista_peliculas[i][clave] = modificacion
                cambio_realizado = True
                print (f"se modifico el {clave}.")
    
#----------------------------------------------------------------------------------------------------------------
def ingresar_pelicula_a_modificar(lista_peliculas):

    titulo = input("Seleccione la pelicula que desea modificar: ") 
    validacion = validar_existecia_de_pelicula(lista_peliculas,titulo)
    while validacion != True:
        print("\n¡Error la pelicula ingresada no existe ingrese nuevamente una pelicula valida!\n")
        titulo = input("Seleccione la pelicula que desea modificar: ") 
        validacion = validar_existecia_de_pelicula(lista_peliculas,titulo)
    return titulo    
#----------------------------------------------------------------------------------------------------------------
def eliminar_empleado(lista_peliculas:list[dict])->None:
       
    titulo = input("Ingrese el titulo de la pelicula a eliminar: ")
    existencia = validar_existecia_de_pelicula(lista_peliculas,titulo)
    if existencia == True:
        for i in range(len(lista_peliculas)):
            if titulo.capitalize() == lista_peliculas[i]["titulo"]:
                opcion = input("\n ¿Se esta por eliminar una pelicula desea continuar? si/no: ")
                if opcion == "si":
                    pelicula_eliminada = lista_peliculas.pop(i)
                    return  print(f"Se ha eliminado correctamentea la pelicula: {pelicula_eliminada["titulo"]}")
                else:
                    break
    else:
        print("Error titulo no encontrado.")         


