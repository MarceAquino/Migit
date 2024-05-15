# class Alumno:
#     especie = "Humano" # atributos de clase
#     def __init__ (self,nombre:str,apellido:str,DNI:int,contrasenia:str):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.DNI = DNI
#         self.contrasenia = contrasenia
#         self.especie = "Humano" # atributos de instancia 



# alumno_1 = Alumno("Marcelo","Aquino",26456565,"123")
# alumno_2 = Alumno("Juan","Perez",27156465,"1234")

# print(alumno_1.apellido)
# print(alumno_2.nombre, alumno_2.apellido)

# class Alumno:
#     def __init__ (self,nombre:str,apellido:str,DNI:int,contrasenia:str):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.DNI = DNI
#         self.contrasenia = contrasenia

#     def presentarse(self, saludo_final:str):
#         return f"Hola a todos mi nombre es: {self.nombre}, mi apellido es: {self.apellido}, y mi Dni es: {self.DNI}.\n{saludo_final}" 
            
# alumno_1 = Alumno("Marcelo","Aquino",26456565,"123")
# print(alumno_1.presentarse("Chau nos vemos"))   

#-------------------------------------appen--------------------------------------
lista = [1,2,3,4]
lista.append(-3) #lo agrega al final 
print(lista)
#-------------------------------------inser--------------------------------------
mi_lista = [1,2,3]
mi_lista.insert(1,-5)  # ingresa el elemento en el indice indicado el -5 en el indice 1 
print(mi_lista) 
#-------------------------------------remove--------------------------------------
mi_lista = [1,2,3]
mi_lista.remove(2)  # elimina el elemento de la lista
print(mi_lista) 
#-------------------------------------pop--------------------------------------
mi_lista = [1,2,3]
elemento = mi_lista.pop() # quita y devuelve el elemento sin dato el ultimo  
print(elemento)
print(mi_lista) 
#-------------------------------------index--------------------------------------
mi_lista = [1,2,3]
mi_lista.index(2)  # devuelve el indice de un elemento que buscamos solo la primera vez q lo encuentre 
print(mi_lista)
#-------------------------------------sort--------------------------------------
mi_lista = [8,1,2,3]
mi_lista.sort(reverse = True )  # ordena de menor a mayor sin parametro con reverse true de mayor a menor 
print(mi_lista)
#-------------------------------------reverse--------------------------------------
mi_lista = [8,1,2,3]
mi_lista.reverse()  # funcion espejo de lista
print(mi_lista)
#-------------------------------------clear--------------------------------------
mi_lista = [8,1,2,3]
mi_lista.clear()  # vacia la lista 
print(mi_lista)
#-------------------------------------copy--------------------------------------
mi_lista = [8,1,2,3,[2,6,7,8]]
lista_copia = mi_lista.copy()
  
print(mi_lista)
print(lista_copia)
