from funciones_validaciones import *
from modificar_eliminar import *

#----------------------------------------------------------------------------------------------------------------
def mostrar_submenu():
    print("""
        a. Modificar el nombre del empleado.
        b. Modificar el apellido del empleado.
        c. Modificar el puesto del empleado.
        d. Modificar el salario del empleado.
        e. Salir
        """)
#----------------------------------------------------------------------------------------------------------------   
def submenu(lista_empleados: list[dict]):
    print("¡Bienvenido al menu de modificaciones!")
    print("Ingrese el ID a modificar")
    validar_existencia_id(lista_empleados)
    retorno = ""
    bandera = False
    while True:
        mostrar_submenu()
        opcion = validar_opcion_menu()
        match opcion:
            case "a":
                modificar_dato(validar_nombre_apellido("nombre: ").capitalize(),"nombre","nombre")
                bandera = True
            case "b":
                modificar_dato(validar_nombre_apellido("apellido: ").capitalize(),"apellido","apellido")
                bandera = True
            case "c":
                modificar_dato(validar_puesto(),"puesto","puesto")
                bandera = True
            case "d":
                modificar_dato(validar_salario(),"salario","salario")
                bandera = True
            case "e":
                if bandera == False:
                    retorno = "no se realizaron cambios"
                else:
                    retorno = retorno
                return retorno
                
            case _:
                print("No es una opcion válida")
#----------------------------------------------------------------------------------------------------------------                    