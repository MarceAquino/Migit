from funciones_del_menu import *
from funciones_generales import *
#------------------------------------------------------------------------------------------------------------------------  
def sumar_dato_heroe(lista_heroes:dict,clave:str)-> int|float:
    suma = 0
    for i in range(len(lista_heroes)):
        if type(lista_heroes[i]) == dict:
            dato = obtener_dato(lista_heroes[i],clave)
            if dato != None and isinstance(dato, (int, float)):
                suma += dato                 
    return suma
#------------------------------------------------------------------------------------------------------------------------ 
def dividir(dividendo: float, divisor: float) -> float:

    mensaje_resultado = False
    if isinstance(dividendo, (int, float)) and isinstance(divisor, (int, float)):
        if divisor != 0:
            mensaje_resultado = dividendo / divisor
    return mensaje_resultado
#------------------------------------------------------------------------------------------------------------------------ 
def calcular_promedio(lista_heroes:list,clave:str) -> float:

    suma = sumar_dato_heroe(lista_heroes,clave)
    cantidad_heroes = len(lista_heroes)
    promedio = dividir(suma,cantidad_heroes)

    return promedio
#------------------------------------------------------------------------------------------------------------------------ 