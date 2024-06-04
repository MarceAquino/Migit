from funciones_del_menu import *
from data_stark import lista_personajes

def imprimir_menu ()->None:
    print("""
1)Normalizar datos.
2)Lista de nombres superhéroes de género NB.
3)Superhéroe más alto de género F.
4)Superhéroe más alto de género M.
5)Superhéroe más débil de género M.
6)Superhéroe más débil de género NB.
7)Fuerza promedio de los superhéroes de género NB
8)Determinar cuántos superhéroes tienen cada tipo de color de ojos.
9)Determinar cuántos superhéroes tienen cada tipo de color de pelo.
10)Listar todos los superhéroes agrupados por color de ojos.
11)Listar todos los superhéroes agrupados por tipo de inteligencia.
12)Salir                                                       
                 """)
#----------------------------------------------------------------------------------    
def validar_entero(numero:str)->bool:
    mensaje = False
    if numero.isdigit():
        mensaje = True
    return mensaje   
#---------------------------------------------------------------------------------- 
def stark_menu_principal ()->None:
    imprimir_menu()
    opcion = input("ingrese una opcion valida: ")
    validar = validar_entero(opcion)
    if validar == True:
        opcion = int(opcion)
    else:
        opcion = "Ingrese un numero entero valido: "
    return opcion
#---------------------------------------------------------------------------------- 
def stark_marvel_app(lista_heroes:list)->int|float|None|bool:

    bandera_validar = False
    while True:
        opcion = stark_menu_principal()
        if opcion == 1 : 
            stark_normalizar_datos(lista_personajes) 
            bandera_validar = True
        elif opcion == 12:
            continuar = input("¿Desea salir? si/no: ")
            if continuar == "si":
                break
        if bandera_validar != False :
            if opcion == 2:
                encontrar_genero_nb(lista_personajes)
            elif opcion == 3:
                encontrar_mas_alto_menor(lista_personajes,"F",True) 
            elif opcion == 4:
                encontrar_mas_alto_menor(lista_personajes,"M",True) 
            elif opcion == 5:
                encontrar_mas_alto_menor(lista_personajes,"M",False) 
            elif opcion == 6:
                encontrar_mas_alto_menor(lista_personajes,"NB",False) 
            elif opcion == 7:
                calcular_promedio_genero(lista_personajes,"NB","fuerza")          
            elif opcion == 8:
                obtener_cantidad_rasgos(lista_personajes,"color_ojos" )
            elif opcion == 9:
                obtener_cantidad_rasgos(lista_personajes,"color_pelo" )
            elif opcion == 10:
                agrupar_heroes(lista_personajes,"color_ojos")
            elif opcion == 11:
                agrupar_heroes(lista_personajes,"inteligencia")
        else:
            print("normalizar datos primero")        
#----------------------------------------------------------------------------------         
    
                