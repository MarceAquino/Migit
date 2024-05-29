from funciones_validaciones import *
#--------------------------------------------------------------------------------------------
def crear_empleado(id_actual: int)->dict:
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
def agregar_empelado(lista:list,datos:dict ,empleado:dict)->str:
    
    lista.append(empleado)
    datos["id_actual"] += 1
    retorno = f"El empleado con el ID: {empleado['id']} fue agregado exitosamente"
    return retorno
#--------------------------------------------------------------------------------------------