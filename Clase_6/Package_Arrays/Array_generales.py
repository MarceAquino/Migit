from Especificas import *
import sys
sys.path.append(r"C:\Users\marce\Desktop\Programacion UTN\Primer cuatrimestre\Programacion\Clase_6")
from Package_input.Input import get_int


lista = [-1] * 10
validar = False

#------------------------------------------------------------------------------

def seleccionar_opcion_a(lista: list) -> None:

    """Pide al usuario ingresar 10 números enteros en el rango de -1000 a 1000.
    Args:
        lista (list): La lista donde se almacenarán los números ingresados.
    Returns: None """

    for i in range(len(lista)):
        lista[i] = get_int("Ingrese 10 numeros: ", "Ingrese un numero del -1000 al 1000: ", -1000, 1000)

#------------------------------------------------------------------------------    
    
def contador_positivos_negativos(lista: list) -> None:

    """Cuenta la cantidad de números positivos y negativos en la lista dada.
    Args:
        lista (list): La lista de números a analizar.
    Returns: None. """
    
    contador_positivos = 0
    contador_negativos = 0

    for i in range(len(lista)):
        if determinar_positividad(lista[i]) == True:
            contador_positivos += 1
        elif determinar_positividad(lista[i]) == False:
            contador_negativos += 1

    print(f"La cantidad de positivos es {contador_positivos}, la cantidad de negativos es {contador_negativos}")

#------------------------------------------------------------------------------

def sumar_pares(lista: list) -> None:

    """Calcula la suma de todos los números pares en la lista dada.
    Args:
        lista (list): La lista de números a sumar.
    Returns: None. """

    suma_pares = 0

    for i in range(len(lista)):
        if validar_pariedad(lista[i]) == True:
            suma_pares += lista[i]       
    print(f"La suma total de numeros pares es: {suma_pares}")

#------------------------------------------------------------------------------
def calcular_max_impar(lista: list) -> None:

    """Encuentra el número impar más alto en la lista dada.
    Args:
        lista (list): La lista de números a analizar.
    Returns: None. """

    bandera_primer_ingreso = True
    for i in range(len(lista)):
        if  bandera_primer_ingreso == True or validar_pariedad(lista[i]) == False :
            numero_max_impar = lista[i]
            bandera_primer_ingreso = False
            if numero_max_impar < lista[i]: 
                numero_max_impar = lista[i]

    print(f"El número impar más alto ingresado es {numero_max_impar}")

#------------------------------------------------------------------------------

def listar_numeros(lista: list) -> None:

    """ Imprime todos los números en la lista dada.
    Args:
        lista (list): La lista de números a imprimir.
    Returns: None. """

    for i in range(len(lista)):
        print(f"Los números de la lista son: {lista[i]}") 

#------------------------------------------------------------------------------

def listar_numeros_pares(lista: list) -> None:

    """ Imprime todos los números pares en la lista dada.
    Args:
        lista (list): La lista de números a imprimir.
    Returns: None. """

    for i in range(len(lista)):
        if validar_pariedad(lista[i]) == True:
            print(f"Los números pares de la lista son: {lista[i]}")

#------------------------------------------------------------------------------

def listar_indices_impares(lista: list) -> None:

    """ Imprime los números en los índices impares de la lista dada.
    Args:
        lista (list): La lista de números.
    Returns: None. """
    
    for i in range(len(lista)):
        if validar_pariedad(i) == False:
            print(f"Los números en los índices impares son: {lista[i]}")

#------------------------------------------------------------------------------

while True:
   
    Menu = print(""" 
    A. Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
    B. Mostrar la cantidad de números positivos y negativos.
    C. Mostrar la sumatoria de los números pares.
    D. Informar el mayor de los números impares.
    E. Listar todos los números ingresados.
    F. Listar todos los números pares.
    G. Listar los números de las indices impares.  
    H. Salir 
    """)
    
    opcion = input("Elegir una de estas opciones: ")
    
    match opcion:
        case "A": 
            seleccionar_opcion_a(lista)
            print("Carga de datos exitosa")
            validar = True
        case _ if validar:
            match opcion:
                case "B":
                    contador_positivos_negativos(lista)
                case "C":
                    sumar_pares(lista)   
                case "D":
                    calcular_max_impar(lista)    
                case "E":
                    listar_numeros(lista)
                case "F":
                    listar_numeros_pares(lista)
                case "G":
                    listar_indices_impares(lista)
                case "H":
                    print("Muchas gracias por utilizar este programa.")
                    break                       
                case _:
                    error = input("Error: ingrese una opción válida: ")
        case _:
            print("Datos sin cargar. Por favor, ingrese primero la opción A.")    
               
                

       
                    
                
              
   

    






            



            












