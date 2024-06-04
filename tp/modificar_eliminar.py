
from funciones_validaciones import *
from funcion_calculo import obtener_dato

#----------------------------------------------------------------------------------------------------------------
def modificar_dato(validacion:str,clave:str,numero_id:int,lista_empleados:list[dict])->str:
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
    
    id_empleado =validar_entero("Ingrese el id del empleado a eliminar: ")
    existencia = validar_existencia_id (lista_empleados,id_empleado)
    if existencia == True:
        for i in range(len(lista_empleados)):
            if id_empleado == lista_empleados[i]['id']:
                opcion = input("\nSe esta a punto de eliminar un empleado desea continuar si/no: ")
                if opcion == "si":
                    persona_eliminada = lista_empleados.pop(i)
                    return  print(f"Se ha eliminado correctamentea a {persona_eliminada['nombre']}{persona_eliminada['apellido']}")
                else:
                    break
    else:
        print("Error id no encontrado.")            
                 
#----------------------------------------------------------------------------------------------------------------
