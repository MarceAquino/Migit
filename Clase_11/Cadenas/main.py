
from data import *
 


"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""
bandera_validar = False

while True:
   
    mostrar_opciones()
    opcion = input("Ingrese una de las opciones: ")
    opcion = opcion.upper() 
#--------------------------------------------------------------------------------------
    if opcion == "A" and bandera_validar == False: 
        bandera_validar = True
        normalizar_datos(lista_videos)

    elif opcion == "H":
        continuar = input("¿Desea salir? si/no: ")

        if continuar == "si":
            break
#--------------------------------------------------------------------------------------
    elif bandera_validar:

            if opcion == "B":
                mostrar_temas(lista_videos)
            elif opcion == "C":
                ordenar_temas(lista_videos)  
            elif opcion == "D":
              
                promediar_vistas(lista_videos)
            elif opcion == "E":
                buscar_maxima_reproduccion(lista_videos)        
            elif opcion == "F":
                buscar_por_codigo(lista_videos)
            elif opcion == "G":
                listar_colaborador(lista_videos)
            else:
                print("Error: ingrese una opción válida.")
    else:
        print("Error: ingrese una opción válida o normalice los datos primero.")
            



#--------------------------------------------------------------------------------------         +


   
               
       


