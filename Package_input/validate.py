# ----------------------------------------------------------------------------------------------------------------------------
def validar_numero (numero:int|float,mensaje_error:str,minimo:int,maximo:int,reintentos:int,tipo_dato:str)->int|float|None:
    """_Esta funcion valida si el numero es int o float_

    Args:
        numero (int | float): _Se ingresa un numero int o float_
        mensaje_error (str): _Msj de error al ingresar un dato no valido en las validaciones_
        minimo (int): _Numero min permitido_
        maximo (int): _Numero max permitido_
        reintentos (int): _Cantidad de errores aceptados_
        tipo_dato (str): _Tipo de dato solicitada int o float_

    Returns:
        int|float|None: _Retorna numero, el mismo validado y parceado_
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
        

  