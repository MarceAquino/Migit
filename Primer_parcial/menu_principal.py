"""
3. Eliminar. Eliminará permanentemente a una película del listado original. Se pedirá el
título de la película a eliminar.
4. Mostrar películas. Ofrecer la opción de mostrar las películas en base a determinados
filtros.
a. Todas las películas.
b. De determinado género.
c. De determinado año.
d. Todas las ATP
e. Todas las No ATP.
Imprimirá por consola la información de las películas en formato de tabla:
5. Ordenar películas. Ofrecer la opción de ordenar y mostrar la lista de películas de forma
ascendente o descendente por:
a. Título.
b. Género.
c. Año de lanzamiento.
d. Duración.
6. Buscar película por título: Permitir al usuario buscar y mostrar la información de una
película específica ingresando su título.
7. Calcular promedio: Mostrar un submenú que permita calcular y mostrar el promedio
de:
a. Año de lanzamiento.
b. Duración de películas.
8. Calcular porcentaje:
a. Porcentaje por género.
b. Porcentaje por ATP.
9. Salir. Terminará la ejecución del programa."""
#------------------------------------------------------------------------------
from validaciones import *
from cargar_mostrar import *
from lectura_escritura import *
from sub_menus import *

#------------------------------------------------------------------------------

lista_peliculas = cargar_peliculas_csv("peliculas_3.csv")
lista_plataformas = crear_lista_plataformas(lista_peliculas)

#------------------------------------------------------------------------------
def imprimir_menu():
    print("""

            1. Dar de alta.
            2. Modificar.
            3. Eliminar.
            4. Mostrar peliculas.
            5. Ordenar peliculas.
            6. Buscar peliculas por titulos.
            7. Calcular promedio.
            8. Calcular porcentaje.
            9. Salir.

        """)
#------------------------------------------------------------------------------   
def mostrar_menu():
    while True:
        imprimir_menu()
        opcion = input("ingrese una opcion valida del 1 al 9: ")
        match opcion:
            case "1" :
                cargar_pelicula(lista_peliculas)    
            case "2":
                submenu_modificar(lista_peliculas)   
            case "3":
                eliminar_empleado(lista_peliculas)                   
            case "4":
                submenu_mostrar_peliculas(lista_peliculas)               
            case "5":
                submenu_ordenar_peliculas(lista_peliculas)                 
            case "6":                 
                imprimir_peliculas(lista_peliculas,"titulo",input("Ingrese el nombre de la pelicula a mostrar: ").capitalize())    
            case "7":
                submenu_calcular_promedio(lista_peliculas)                  
            case "8":
                submenu_calcular_porcentaje(lista_peliculas)    
            case "9":
                continuar = input("¿Desea salir? si/no: ")
                if continuar == "si":
                    guardar_peliculas_csv(lista_peliculas,"peliculas_3.csv")
                    break
            case _:
                print("¡Error! ingrese una opcion valida del 1 al 9: ")
#------------------------------------------------------------------------------
mostrar_menu()




