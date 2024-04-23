# mi_lista = [-1] * 5
# largo_lista = len(mi_lista)
# respuesta = "Si"

# while respuesta == "Si":

#     posicion =int(input("Por favor ingrese la posicion del numero a cargar: "))
#     while posicion < 1 or posicion > largo_lista:
#         posicion =int(input("Error ingrese la posicion del numero a cargar: "))

#     numero = int(input("Por favor ingrese el numero a cargar: ")) 

#     mi_lista[posicion -1] = numero   
       


#     respuesta = input("¿Desea contunuar? Si/No: ")
#     while respuesta != "Si" and respuesta != "No":
#         respuesta = input ("¿Desea contunuar? Si/No: ")

# for i in range (len(mi_lista)):
#     print(mi_lista[i])    


# # #busqueda

lista = [9,45,10,3,3]

# numero_buscado = 45

# for i in range(len(lista)):
#     if numero_buscado == lista[i]:
#         print (f"El numero se encuntra en el indice: {i}")


# acumulador = 0
# for i in range(len(lista)):
#     if lista[i] > 0:
#         acumulador += lista[i]

# print(acumulador)        
                

# for i in range(len(lista)):
#     if i == 0 or lista[i ] > numero_max:
#         numero_max = lista[i]
#         # guardar indice 
#         #indice_max = i
# print(numero_max)       

# numero_buscado = 3
# reemplazo = 11

# for i in range(len(lista)):
#     if lista[i] == 3:
#         lista[i] = reemplazo

# for i in range (len(lista)):
#     print(lista[i])           

def buscar_reemplazar(lista:list,numero_buscado: int, reemplazo:int) -> None:
    for i in range(len(lista)):
        if lista[i] == numero_buscado:
            lista[i] = reemplazo
def mostrar_lista(lista:list)->None:
    for i in range (len(lista)):
        print(lista[i])    

mostrar_lista(lista)
print("---------------------------")
buscar_reemplazar(lista, 3 ,11)
mostrar_lista(lista)