def validar_numero(numero: int, mensaje_error: str, minimo: int | float, maximo: int | float, reintentos: int | float,
                   tipo_dato: str) -> int | float | None:
  
   
   
    while numero > maximo or numero < minimo :
        reintentos -= 1
        numero = int(input(mensaje_error))
        if reintentos < 0:
            return None
        if tipo_dato == "int":
            numero = int(numero)
        else:
            numero = float(numero)
    return numero    

def validar_cadena (mensaje:str,mensaje_error:str,longitud:int,reintentos:int)->str|None:

    
    cadena = len(mensaje)
    while cadena > longitud:
        reintentos -= 1
        ingreso = input(mensaje_error)   
        cadena = ingreso
        cadena = len (cadena)
        if reintentos == 0:
            return None
    return f"El texto ingresado es: {ingreso} y su longitud es: {cadena}"
        

  