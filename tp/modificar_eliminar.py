from data import lista_empleados
from funciones_validaciones import *
from funcion_calculo import obtener_dato

#----------------------------------------------------------------------------------------------------------------
def modificar_dato(validacion:str,clave:str,numero_id:int)->str:
    cambio_realizado = False
    
    for i in range(len(lista_empleados)):
        if cambio_realizado == False:
            if lista_empleados[i]["id"] == numero_id:    
                dato = validacion
                lista_empleados[i][clave] = dato
                cambio_realizado = True
                retorno = f"se modifico el {clave}."
                return retorno    

#----------------------------------------------------------------------------------------------------------------
def eliminar_empleado(lista_empleados:list[dict])->None:
    
    print("Ingrese el id del empleado a eliminar: ")
    id_empleado = validar_existencia_id(lista_empleados)
    for i in range(len(lista_empleados)):
        if id_empleado == lista_empleados[i]['id']:
            persona_eliminada = lista_empleados.pop(i)
            return  print(f"Se ha eliminado correctamentea a {persona_eliminada['nombre']}{persona_eliminada['apellido']}")
                 
#----------------------------------------------------------------------------------------------------------------
