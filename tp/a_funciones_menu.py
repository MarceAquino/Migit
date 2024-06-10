from crear_persona import *
from b_funciones_sub_menu import *
from mostrar_cargar_datos import *
from funcion_calculo import *

lista_empleados = []
def imprimir_menu():
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
def mostrar_menu(lista_empleados:list):

    
    bandera_continuar = validar_lista_vacia(lista_empleados)
    while True:
        imprimir_menu()
        opcion = validar_entero("Ingrese una opcion valida: ")
        if opcion == 2 :
            empleado = crear_empleado(validar_id(lista_empleados))
            agregar_empleado(lista_empleados,empleado)
            
        elif opcion == 1:

            cargar = input("""\nIngrese desde donde desea cargar la lista de empleados a/b: """)
            while cargar != "a" and cargar != "b":
                print("Error ingrese una opcion valida")
                cargar = input("""\nIngrese desde donde desea cargar la lista de empleados a/b: """)
            if cargar == "a":    
                lista_empleados = cargar_personas_desde_csv(r"Programacion\Migit\tp\empleados.csv")
            else:    
                lista_empleados = cargar_personas_desde_json(r"Programacion\Migit\tp\empleados.json")

        elif opcion == 10:
            continuar = input("¿Desea salir? si/no: ")
            if continuar == "si":
                break
        if bandera_continuar != validar_lista_vacia(lista_empleados) :
            if opcion == 3:
                submenu(lista_empleados)
            elif opcion == 4:
                eliminar_empleado(lista_empleados)
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
            print("No se encuentran empleados, cargar al menos 1 empleado")   
    return lista_empleados 

mostrar_menu(lista_empleados)

# c sharp 
# tipo de datos
# sql