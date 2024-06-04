from funciones_generales import *
from funciones_cuentas import *

#------------------------------------------------------------------------------------------------------------------------
def encontrar_genero_nb(lista_heroes:list)->None:

    for i in range(len(lista_heroes)):
        if obtener_dato(lista_heroes[i],"genero") == "NB":
            print(obtener_nombre(lista_heroes[i]))
#------------------------------------------------------------------------------------------------------------------------              
def encontrar_mas_alto_menor(lista_heroes:list,genero:str,criterio:bool)->None:   

    lista_genero = []

    for i in range(len(lista_heroes)):
        if obtener_dato(lista_heroes[i],"genero") == genero:
            lista_genero.append(lista_heroes[i]) 
    if criterio == True:
        maximo = obtener_maximo(lista_genero,"altura")
        datos = obtener_dato_cantidad(lista_genero,maximo,"altura")
        stark_imprimir_heroes(datos)
    else:
        minimo = obtener_minimo(lista_genero,"fuerza")
        datos = obtener_dato_cantidad(lista_heroes,minimo,"fuerza")
        stark_imprimir_heroes(datos)
    
#------------------------------------------------------------------------------------------------------------------------
def listar_atributos(lista_heroes: list,clave:str):

    lista_atributo = []

    for heroe in lista_heroes:
        atributo = obtener_dato(heroe, clave)
        if atributo not in lista_atributo:
            lista_atributo.append(atributo)

    return lista_atributo

#------------------------------------------------------------------------------------------------------------------------
def agrupar_heroes(lista_heroes: list,clave:str):  

    for valor in listar_atributos(lista_heroes,clave):
        print(f"Atributo: {clave.replace('_', ' de ').capitalize()} {valor.capitalize()}")
        for heroe in lista_heroes:
            if heroe.get(clave) == valor:
                nombre = obtener_nombre(heroe)
                print(nombre)
        print()  
#------------------------------------------------------------------------------------------------------------------------
def calcular_promedio_genero(lista_heroes:list, genero:str, rasgo:str) -> None:

    lista_calcular = []

    for heroe in lista_heroes:
        if obtener_dato(heroe, "genero") == genero:
            lista_calcular.append(heroe)

    print (f"El promedio de {rasgo} del genero {genero} es: {calcular_promedio(lista_calcular, rasgo)}")
#------------------------------------------------------------------------------------------------------------------------
def obtener_cantidad_rasgos(lista_heroes:list, clave:str) -> None:
    contador_por_valor = {}
    
    for heroe in lista_heroes:
        valor = heroe.get(clave)
        if valor not in contador_por_valor:
            contador_por_valor[valor] = 1
        else:
            contador_por_valor[valor] += 1

    print(f"Conteo total por cada {clave.replace('_', ' de ')}:")
    for valor, contador in contador_por_valor.items():
        print(f"{valor.capitalize()}: {contador}")
#------------------------------------------------------------------------------------------------------------------------