from data import lista_empleados
from funciones_validaciones import *

def modificar_dato(validacion:str,clave,elemento):
    for i in range(len(lista_empleados)):
        dato = {validacion}
        lista_empleados[i][clave] = dato
        retorno = f"se modifico el {elemento}."
    return retorno    

 
def eliminar_empleado(lista_empleados:list[dict])->str:
    retorno = ""
    bandera_existe = False
    id_empleado = validar_existencia_id(lista_empleados)
    for i in range(len(lista_empleados)):
        if id_empleado == lista_empleados[i]["id"]:
            bandera_existe = True
            persona_eliminada = lista_empleados.pop(i)
            retorno = f"Se ha eliminado correctamentea a {persona_eliminada['nombre']}{persona_eliminada['apellido']}"
    if bandera_existe == False:
        retorno = "Error, no existe una persona con ese dni:"
    return retorno    