#----------------------------------------------------------------------------------------------------------------
def mostrar_persona(persona:dict)->None:
    mensaje = f"""
                ********************************************************************************************
                Nombre: {persona['nombre']}
                Apellido: {persona['apellido']}	
                Puesto: {persona['puesto']}
                Salario: {persona['salario']}
                ******************************************************************************************** 
                """
    return print(mensaje)  
#---------------------------------------------------------------------------------------------------------------- 
def mostrar_personas(lista_empeados:list[dict])->None:
    print("==== Los empleados encontrados son ====\n")
    for i in range (len(lista_empeados)):
        mostrar_persona(lista_empeados[i])
#----------------------------------------------------------------------------------------------------------------
def mostrar_personas_por_puesto(lista_empleados:list[dict], puesto: str)->None:
    print(f"==== Los {puesto} encontrados son ====\n")
    for i in range(len(lista_empleados)):
        if lista_empleados[i]['puesto'] == puesto:
            mostrar_persona(lista_empleados[i])       
#----------------------------------------------------------------------------------------------------------------            