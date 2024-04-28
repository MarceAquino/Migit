from .validate import *

#-------------------------------------------------------------------------------------------------------------------------------
def get_int (numero:int,mensaje_error:str,minimo:int,maximo:int)->int|None:

   
    """   Solicita al usuario ingresar un número entero dentro de un rango especificado y lo valida.
    Esta función solicita al usuario ingresar un número entero, lo convierte a tipo float para permitir la validación, y luego utiliza la función `validar_numero` 
    para asegurarse de que esté dentro del rango especificado y sea un número entero válido. Si la entrada no es válida o está fuera del rango especificado, 
    se solicita al usuario que ingrese nuevamente el número hasta que se proporcione una entrada válida.
    Args:
        numero (int): Un identificador numérico para mostrar al usuario.
        mensaje_error (str): El mensaje de error a mostrar si la validación falla o la entrada no es válida.
        minimo (int): El valor mínimo permitido para el número.
        maximo (int): El valor máximo permitido para el número.
    Returns:
        int | None: El número entero validado, o None si la entrada no es válida."""
    numero = input (numero)
    numero = float(numero)
    numero = validar_numero(numero,mensaje_error,minimo,maximo)
    return numero 

#-------------------------------------------------------------------------------------------------------------------------------
















    





