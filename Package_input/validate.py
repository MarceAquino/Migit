# ----------------------------------------------------------------------------------------------------------------------------
def validar_numero (numero:int|float,mensaje_error:str,minimo:int,maximo:int,reintentos:int,tipo_dato:str)->int|float|None:
    """Esta función valida si el número es int o float.

    Args:
        numero (int|float): Se ingresa un número int o float.
        mensaje_error (str): Msj de error al ingresar un dato no válido.
        minimo (int): Número mínimo permitido.
        maximo (int): Número máximo permitido.
        reintentos (int): Cantidad de errores aceptados.
        tipo_dato (str): Tipo de dato solicitada int o float.

    Returns:
        int|float|None: Retorna numero, el mismo validado y parseado.
    """
    if tipo_dato == "int":
        while numero % 1 != 0 or (numero > maximo or numero < minimo):
            reintentos -= 1
            numero = input (mensaje_error)
            numero = float(numero)
            if reintentos == 0:
                return None
        return int(numero) 
    
    else:
        while (numero > maximo or numero < minimo):
            reitentos = reitentos - 1
            numero = input(mensaje_error)
            numero = float (numero)
            if reintentos == 0:
                return None
        return numero 
# ---------------------------------------------------------------------------------------------------------------------------- 
def validar_cadena (mensaje:str,mensaje_error:str,longitud:int,reintentos:int)->str|None:
    """Esta funcion valida la cantidad de caracteres de una cadena te texto.

    Args:
        mensaje (str): Mensaje solicitando el ingreso de la cadena de texto. 
        mensaje_error (str): Mensaje error cadena supera la longitud maxima permitida. 
        longitud (int): Numero maximo de caracteres. 
        reintentos (int): Cantidad de intentos para consider el ingreso invalido retorna none.

    Returns:
        str|None: Retorna None en el caso de que la cadena sea invalida.
                  Retorna la cadena y el valor de la misma en el caso de que sea valida. 
    """
    cadena = len(mensaje)
    while cadena > longitud:
        reintentos -= 1
        ingreso = input(mensaje_error)   
        cadena = ingreso
        cadena = len(cadena)
        if reintentos == 0:
            return None       
    return f"El texto ingresado es: {ingreso} y su longitud es: {cadena}"
# ----------------------------------------------------------------------------------------------------------------------------
        

  