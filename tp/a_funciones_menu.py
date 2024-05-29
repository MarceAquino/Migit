from crear_persona import *
from data import lista_empleados
from b_funciones_sub_menu import *
from mostrar_datos import *
from funcion_calculo import *

def mostrar_menu():
    print("""
        1. Dar de alta.
        2. Modificar.
        3. Eliminar.
        4. Mostrar todos.
        5. Mostrar gerentes.
        6. Calcular salario promedio.
        7. Salir.
        """)

def mostar_menu(lista_empleados:list):

    datos = { "id_actual": 1}
    bandera_continuar = False
    while True:
        mostrar_menu()
        opcion = validar_entero()
        if opcion == 1 :
            empleado = crear_empleado(datos["id_actual"])
            empleado_agregado = agregar_empelado(lista_empleados,datos,empleado)
            print(empleado_agregado)
            bandera_continuar = True
        elif opcion == 7:
            continuar = input("¿Desea salir? si/no: ")
            if continuar == "si":
                break
        if bandera_continuar != False :
            if opcion == 2:
                submenu(lista_empleados)
            elif opcion == 3:
                eliminar_empleado(lista_empleados)
                print(lista_empleados)
            elif opcion == 4:
                mostrar_personas(lista_empleados)
            elif opcion == 5:
                mostrar_personas_por_puesto(lista_empleados,"Gerente")
            elif opcion == 6:
                calcular_promedio(lista_empleados, "salario")  
        else:
            print("normalizar datos primero")   
    return lista_empleados 

mostar_menu(lista_empleados)
