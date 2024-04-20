from .validate import validar_numero,validar_cadena
# ----------------------------------------------------------------------------------------------------------------------------
def get_int (mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int,tipo_dato)->int|None:

    numero = input (mensaje)
    numero = float(numero)
    numero = validar_numero (numero,mensaje_error,minimo,maximo,reintentos,tipo_dato)
    return numero
       
# ----------------------------------------------------------------------------------------------------------------------------
def get_float (mensaje:str,mensaje_error:str,minimo:float,maximo:float,reintentos:float,tipo_dato:str)->float|None:

    numero = input (mensaje)
    numero = float(numero)
    numero = validar_numero (numero,mensaje_error,minimo,maximo,reintentos,tipo_dato)
    return numero 
# ----------------------------------------------------------------------------------------------------------------------------
def get_string (mensaje:str,mensaje_error:str,longitud:int,reintentos:int)->str|None:

    ingreso = input(mensaje)   
    cadena = ingreso
    cadena = validar_cadena (mensaje,mensaje_error,longitud,reintentos)
    return cadena
# ----------------------------------------------------------------------------------------------------------------------------





    





