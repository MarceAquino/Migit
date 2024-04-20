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
        
        

    
        
