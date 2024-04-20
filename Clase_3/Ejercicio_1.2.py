def get_string (mensaje:str,mensaje_error:str,longitud:int,reitentos:int)->str|None:
    print(reitentos)
    ingreso = input(mensaje)   
    cadena = ingreso
    cadena = len (cadena)
    
    while cadena != longitud :
        reitentos -= 1 
        ingreso = input(mensaje_error)   
        cadena = ingreso
        cadena = len (cadena)       
        if reitentos == 0:
            return None
    return f"El texto ingresado es: {ingreso} y su longitud es: {cadena}"

print (get_string("Ingrese una cadena de texto de 4 caracteres: ","Error cadena texto max 4 caracteres: ",4,2))  



