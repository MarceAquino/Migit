from Package_input.Input import get_int
# ----------------------------------------------------------------------------------------------------------------------------
def calcular_factorial(numero: int) -> int:

    if numero == 1:
        return 1 
  
    return numero * calcular_factorial(numero - 1)

numero = get_int("Calcular factorial: ","Error, ingrese un numero del 1 al 10: ",0,10,2,"int")
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
# ----------------------------------------------------------------------------------------------------------------------------
def calcular_potencia(base: int, exponente: int) -> int:

    if exponente == 0:
        return 1
    return base * calcular_potencia(base, exponente - 1)

base = get_int("Ingrese la base de la potencia: ","Error",0,100,2,"int")
exponente = get_int("Ingrese el exponente de la potencia: ","Error",0,100,2,"int")
resultado = calcular_potencia(base, exponente)
print(f"La potencia de {base} elevado al {exponente} es: {resultado}")

#----------------------------------------------------------------------------------------------------------------------------
def sumar_digitos (numero:int)->int:

     if numero == 0:
        return 0
     ultimo_digito = numero % 10
     resto_numero = numero // 10
     return ultimo_digito + sumar_digitos(resto_numero)
        
numero = get_int("Ingrese los digitos a sumar: ","Error",0,9999,2,"int")
suma = sumar_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {suma}")
# ----------------------------------------------------------------------------------------------------------------------------
def calcular_numero_fibonacci(numero: int) -> int:
    """_summary_

    Args:
        numero (int): _description_

    Returns:
        int: _description_
    """
    if numero <= 1:
        return numero
    else:
        return calcular_numero_fibonacci(numero - 1) + calcular_numero_fibonacci(numero -2)
               
numero = get_int("Ingrese el numero de Fibonacci que quiere calcular: ","Error",0,9999,2,"int")
resultado = calcular_numero_fibonacci(numero)
print(f"El número de Fibonacci de {numero} es: {resultado}")
# ----------------------------------------------------------------------------------------------------------------------------
