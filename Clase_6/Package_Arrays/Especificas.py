

#Funcion para determinar positividad (Especial)
def  determinar_positividad(number: int)->bool:

    """Esta funcion determina si un numero es positivo o negativo 
    Args:
        number (int): Si el numero es mayor a cero el mismo se valida como positivo 

    Returns:
        bool: Retorna True en caso de numero positivo False en caso de numero negativo. 
    """
    retorno = False
    if number > 0:
        retorno = True
    return retorno

#Funcion para validad pariedad (Especial)
def validar_pariedad (numero)-> bool:
    
    """Esta funcion determina si un numero es par o imapar
    Args:
        numero (_type_): Se evalua el modulo del numero para saber si dicho numero es par o impar 

    Returns:
        bool: En caso de ser par el mismo retorna True, caso impar retorna False. 
    """
    par = False
    if numero % 2 == 0:
        par = True
    return par 


    
