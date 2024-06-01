from funciones_validaciones import *
from modificar_eliminar import *

#----------------------------------------------------------------------------------------------------------------
def mostrar_submenu()->None:
    
    print("""
        a. Modificar el nombre del empleado.
        b. Modificar el apellido del empleado.
        c. Modificar el puesto del empleado.
        d. Modificar el salario del empleado.
        e. Salir
        """)
#----------------------------------------------------------------------------------------------------------------   
def submenu(lista_empleados: list[dict])->None:

    print("¡Bienvenido al menu de modificaciones!\n")
    numero_id = validar_existencia_id(lista_empleados)
    retorno = ""
    bandera = False

    while True:
        mostrar_submenu()
        opcion = validar_opcion_menu()
        match opcion:
            case "a":
                modificar_dato(validar_nombre_apellido("nombre").capitalize(),"nombre",numero_id)
                bandera = True
            case "b":
                modificar_dato(validar_nombre_apellido("apellido").capitalize(),"apellido",numero_id)
                bandera = True
            case "c":
                modificar_dato(validar_puesto(),"puesto",numero_id)
                bandera = True
            case "d":
                modificar_dato(validar_salario(),"salario",numero_id)
                bandera = True
            case "e":
                continuar = input("¿Desea salir? si/no: ")
                if continuar == "si":
                    if bandera == False:
                        retorno = "no se realizaron cambios"
                    else:
                        retorno = retorno
                    return retorno
                
                
            case _:
                print("No es una opcion válida")
#----------------------------------------------------------------------------------------------------------------                    