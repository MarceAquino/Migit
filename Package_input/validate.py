# ----------------------------------------------------------------------------------------------------------------------------
def validar_numero (numero:int|float,mensaje_error:str,minimo:int,maximo:int,reintentos:int,tipo_dato:str)->int|float|None:
    
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
        

  