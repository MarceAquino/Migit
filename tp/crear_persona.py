from funciones_validaciones import *
from funcion_calculo import obtener_maximo 




#--------------------------------------------------------------------------------------------
def crear_empleado(id_actual:list)->dict:

    id_actual = obtener_maximo(id_actual) + 1
    nombre = validar_nombre_apellido("nombre").capitalize()
    apellido = validar_nombre_apellido("apellido").capitalize()
    puesto = validar_puesto().capitalize()
    salario = validar_salario()

    persona_nueva = {
        "id": id_actual,
        "nombre": nombre,
        "apellido": apellido,
        "puesto": puesto,
        "salario": salario,
    }
    return persona_nueva
#--------------------------------------------------------------------------------------------
def agregar_empleado(lista_empleados:list[dict],empleado:dict)->str:

    lista_empleados.append(empleado)
    print(f"\n¡El empleado con el ID: {empleado['id']} fue agregado exitosamente!")
    
#--------------------------------------------------------------------------------------------

    