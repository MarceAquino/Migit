from crear_persona import *
from data import lista_empleados
from b_funciones_sub_menu import *
from mostrar_datos import *
from funcion_calculo import *

def mostrar_menu():
    print("""
        
            1. Leer desde CSV / JSON
            2. Dar de alta.
            3. Modificar.
            4. Eliminar.
            5. Mostrar todos.
            6. Mostrar gerentes.
            7. Mostrar Analistas con sueldo mayor a $500000.
            8. Calcular salario promedio.
            9. Ordenar empleados.
            10.  Salir.

        """)

def mostar_menu(lista_empleados:list):

    datos = { "id_actual": 1}
    bandera_continuar = False
    while True:
        mostrar_menu()
        opcion = validar_entero("Ingrese una opcion valida: ")
        if opcion == 2 :
            empleado = crear_empleado(datos["id_actual"])
            agregar_empelado(lista_empleados,datos,empleado)
            bandera_continuar = True
        elif opcion == 1:
            pass
            # Leer desde CSV / JSON
        elif opcion == 10:
            continuar = input("¿Desea salir? si/no: ")
            if continuar == "si":
                break
        if bandera_continuar != False :
            if opcion == 3:
                submenu(lista_empleados)
            elif opcion == 4:
                eliminar_empleado(lista_empleados)
                print(lista_empleados)
            elif opcion == 5:
                mostrar_personas(lista_empleados)
            elif opcion == 6:
                mostrar_personas_por_puesto(lista_empleados,"Gerente")
            elif opcion == 7:
                #Mostrar Analistas con sueldo mayor a $500000.
                pass    
            elif opcion == 8:
                calcular_promedio(lista_empleados, "salario")  
            elif opcion == 9:
                #Ordenar empleados.
                pass    
        else:
            print("normalizar datos primero")   
    return lista_empleados 

mostar_menu(lista_empleados)
