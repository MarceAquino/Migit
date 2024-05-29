from crear_persona import *
from data import lista_empleados
from b_funciones_sub_menu import *
from mostrar_datos import *
from funcion_calculo import *
from crear_persona import *

#----------------------------------------------------------------------------------------------------------------
def mostrar_menu()->None:
    print("""
        1. Dar de alta.
        2. Modificar.
        3. Eliminar.
        4. Mostrar todos.
        5. Mostrar gerentes.
        6. Calcular salario promedio.
        7. Salir.
        """)
#----------------------------------------------------------------------------------------------------------------  
def mostar_menu(lista_empleados: list) -> None:
    print("\n=====¡Bienvenidos al programa para altas, bajas y modificaciones de empleados!=====\n")
    datos = {"id_actual": 1}
    while True:
        lista_vacia = validad_lista(lista_empleados)
        mostrar_menu()
        opcion = validar_entero("Ingrese una opcion valida: ")
        print()
        if opcion == 1:
            lista_vacia = nuevo_empleado(datos)   
        elif opcion == 7:
            continuar = input("¿Desea salir? si/no: ")
            if continuar == "si":
                break
        if lista_vacia != False:
            if opcion == 2:
                submenu(lista_empleados)
            elif opcion == 3:
                eliminar_empleado(lista_empleados)
            elif opcion == 4:
                mostrar_personas(lista_empleados)
            elif opcion == 5:
                mostrar_personas_por_puesto(lista_empleados, "Gerente")
            elif opcion == 6:
                calcular_promedio(lista_empleados, "salario")
        else:
            print("La lista de empleados está vacía. No se pueden realizar las operaciones 2 a 6.")
            continue            
#----------------------------------------------------------------------------------------------------------------       
    
mostar_menu(lista_empleados)

#----------------------------------------------------------------------------------------------------------------