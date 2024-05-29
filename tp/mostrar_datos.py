
def mostrar_persona(persona:dict):
    mensaje = f"""
                ********************************************************************************************
                Nombre: {persona['nombre']}
                Apellido:{persona['apellido']}	
                Puesto: {persona['puesto']}
                Salario: {persona['salario']}
                ******************************************************************************************** 
                """
    return print(mensaje)  
 
def mostrar_personas(lista_empeados:list):
    for i in range (len(lista_empeados)):
        mostrar_persona(lista_empeados[i])

def mostrar_personas_por_puesto(lista_empleados: list, puesto: str):
    for i in range(len(lista_empleados)):
        if lista_empleados[i]['puesto'] == puesto:
            mostrar_persona(lista_empleados[i])       