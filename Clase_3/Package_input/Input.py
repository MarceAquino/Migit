from validate import *

def get_int (numero:int,mensaje_error:str,minimo:int,maximo:int,reintentos:int ,tipo_dato:str)->int|None:

    numero = int(input(numero))
    numero = validar_numero(numero,mensaje_error,minimo,maximo,reintentos,tipo_dato)
    return numero 

#print (get_int("Hola ingrese un numero entero del 1 al 10: ","Error, ingrese un numero del 1 al 10: ",0,10,2,"int"))


def get_float (numero:str,mensaje_error:str,minimo:float,maximo:float,reintentos:float,tipo_dato:str)->float|None:
    numero = float(input(numero))
    numero = validar_numero(numero,mensaje_error,minimo,maximo,reintentos,tipo_dato)
    return numero
#print (get_float("Hola ingrese un numero decimal del 1 al 10: ","Error, ingrese un numero del 1 al 10: ",0,10,2,"float"))

def get_string (mensaje:str,mensaje_error:str,longitud:int,reintentos:int)->str|None:

    ingreso = input(mensaje)   
    cadena = ingreso
    cadena = validar_cadena(mensaje,mensaje_error,longitud,reintentos)
    return cadena

print (get_string("Ingrese una cadena de texto: ","Error cadena texto max 4 caracteres: ",4,2))




    





