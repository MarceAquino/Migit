
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
    opcion = input("Elegir una de estas opciones: ")
    opcion = opcion.upper()    
#--------------------------------------------------------------------------------------
    if opcion == "A" and bandera_validar == False: 
        bandera_validar = True
        for i in range (len(lista_videos)):
            lista_videos[i].dividir_titulo()
            lista_videos[i].obtener_codigo_url()
            lista_videos[i].formatear_fecha()    

    elif opcion == "H":
        continuar = input("¿Desea salir? si/no: ")

        if continuar == "si":
            break
#--------------------------------------------------------------------------------------
    elif bandera_validar:

            if opcion == "B":
                for i in range(len(lista_videos)):
                    mostrar = lista_videos[i].mostrar_tema()
            elif opcion == "C":
                for i in range(len(lista_videos)):
                    for j in range(0, len(lista_videos) -i -1):
                        if lista_videos[j].obtener_numero_sesion() > lista_videos[j+1].obtener_numero_sesion():
                            aux = lista_videos[j]
                            lista_videos[j] = lista_videos[j+1]
                            lista_videos[j+1] = aux 
                    mostrar = lista_videos[i].mostrar_tema()    
            elif opcion == "D":
                suma = 0
                for i in range(len(lista_videos)):
                    suma += lista_videos[i].cantidad_vistas()
                promedio = suma / len(lista_videos)
                cantidad_k = promedio / 1000
                print (f"el promedio de vista en k es: {cantidad_k}" )
            elif opcion == "E":
                max_vistas = 0
                for i in range(len(lista_videos)):
                    if lista_videos[i].cantidad_vistas() > max_vistas:
                        max_vistas = lista_videos[i].cantidad_vistas()    
                print (f"el mas visto de vista en k es: {max_vistas}" ) 
            elif opcion == "F":
                for i in range(len(lista_videos)):
                    buscar = lista_videos[i].mostrar_url()
                    buscar = buscar.count("nick")
                    if buscar >= 1:
                        lista_videos[i].mostrar_tema()            
            elif opcion == "G":
                colaborador = input("Ingrese el nombre de un colaborador: ")
                for i in range(len(lista_videos)):
                    buscar = lista_videos[i].mostrar_colaborador()
                    buscar = buscar.count(colaborador)
                    if buscar >= 1:
                        lista_videos[i].mostrar_tema()  
            else:
                print("Error: ingrese una opción válida.")
    else:
        print("Error: ingrese una opción válida o normalice los datos primero.")
            



#--------------------------------------------------------------------------------------         +

