def get_int (mensaje:str,mensaje_error:str,minimo:int,maximo:int,reitentos:int)->int|None:
    numero = input (mensaje)
    numero = float(numero)

    while numero % 1 != 0 or (numero > maximo or numero < minimo) :
        reitentos -= 1
        numero = input (mensaje_error)
        numero = int(numero)
        if reitentos < 0:
            return None
    return int(numero)    

    

print (type(get_int("Hola ingrese un numero entero del 1 al 10: ","Error, ingrese un numero del 1 al 10: ",0,10,2)))

#Bis 1 
def get_float (mensaje:str,mensaje_error:str,minimo:float,maximo:float,reitentos:float)->float|None:

    numero = input(mensaje)
    numero = float(numero)
    while numero % 1 == 0 or (numero > maximo or numero < minimo):
        reitentos = reitentos - 1
        numero = input(mensaje_error)
        numero = float (numero)
        if reitentos == 0:
            return None
    return numero 
    




    









print (get_float("Hola ingrese un numero decimal del 1 al 10: ","Error, ingrese un numero del 1 al 10: ",0,10,2))    

def get_string (mensaje:str,mensaje_error:str,longitud:int,reitentos:int)->str|None:
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
        
        

    
        
