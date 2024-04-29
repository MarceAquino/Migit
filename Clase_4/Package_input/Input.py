from .validate import validar_numero,validar_cadena
# ----------------------------------------------------------------------------------------------------------------------------
def get_int (mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int,tipo_dato)->int|None:
    """Esta funcion solicita el ingreso de un numero int.

     Args:
        numero (int|float): Se ingresa un número int.
        mensaje_error (str): Msj de error al ingresar un dato no válido.
        minimo (int): Número mínimo permitido.
        maximo (int): Número máximo permitido.
        reintentos (int): Cantidad de errores aceptados.
        tipo_dato (str): Tipo de dato solicitada int .

    Returns:
        int|None: Retorna numero int, el mismo validado y parseado.
                  Retorna none en caso de error en validaciones.   
    """

    numero = input (mensaje)
    numero = float(numero)
    numero = validar_numero (numero,mensaje_error,minimo,maximo,reintentos,tipo_dato)
    return numero
       
# ----------------------------------------------------------------------------------------------------------------------------
def get_float (mensaje:str,mensaje_error:str,minimo:float,maximo:float,reintentos:float,tipo_dato:str)->float|None:
    """Esta funcion solicita el ingreso de un numero float.

     Args:
        numero (int|float): Se ingresa un número float.
        mensaje_error (str): Msj de error al ingresar un dato no válido.
        minimo (int): Número mínimo permitido.
        maximo (int): Número máximo permitido.
        reintentos (int): Cantidad de errores aceptados.
        tipo_dato (str): Tipo de dato solicitada float.

    Returns:
        float|None: Retorna numero float, el mismo validado y parseado.
                    Retorna none en caso de error en validaciones. """                
    numero = input (mensaje)
    numero = float(numero)
    numero = validar_numero (numero,mensaje_error,minimo,maximo,reintentos,tipo_dato)
    return numero 
# ----------------------------------------------------------------------------------------------------------------------------
def get_string (mensaje:str,mensaje_error:str,longitud:int,reintentos:int)->str|None:
    """Esta funcion solitia el ingreso de una cadena de texto.

    Args:
        mensaje (str): Mensaje solicitando el ingreso de la cadena de texto. 
        mensaje_error (str): Mensaje error cadena supera la longitud maxima permitida. 
        longitud (int): Numero maximo de caracteres.
        reintentos (int): Cantidad de intentos para consider el ingreso invalido retorna None.
    Returns:
        str|None: Retorna none en el caso de que la cadena sea invalida.
                  Retorna la cadena y el valor de la misma en el caso de que sea valida. 
    """
    ingreso = input(mensaje)   
    cadena = ingreso
    cadena = validar_cadena (mensaje,mensaje_error,longitud,reintentos)
    return cadena
# ----------------------------------------------------------------------------------------------------------------------------





    





