
#------------------------------------------------------------------------------------------------------------------------ 
def obtener_dato(persona:dict,clave:str)->str|bool: 
    longitud = len(persona)
    if longitud < 0:
        mensaje = False
    else:    
        mensaje = persona.get(clave)
    return mensaje
#------------------------------------------------------------------------------------------------------------------------ 
def sumar_salario(lista_empleados:dict,clave:str)-> int|float:

    suma = 0
    for i in range(len(lista_empleados)):
        if type(lista_empleados[i]) == dict:
            dato = obtener_dato(lista_empleados[i],clave)
            suma += dato                       
    return suma
#------------------------------------------------------------------------------------------------------------------------ 
def dividir(dividendo: float, divisor: float) -> int | float:
        
    mensaje_resultado = False
    mensaje_resultado = dividendo / divisor

    return mensaje_resultado
#------------------------------------------------------------------------------------------------------------------------ 
def calcular_promedio(lista_empleado:list,clave:str) -> None:

    suma = sumar_salario(lista_empleado,clave)
    cantidad_empleados = len(lista_empleado)
    promedio = dividir(suma,cantidad_empleados)
    resultado = print(f"El promedio de los sueldos es: {promedio}")
    return resultado
#------------------------------------------------------------------------------------------------------------------------ 