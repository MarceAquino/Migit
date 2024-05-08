
from validaciones import *
from carga import *
from calcular import *
#----------------------------------------------------------------------------------------
bandera_validar = False
#----------------------------------------------------------------------------------------
matriz_colectivo = [[100,1,2,3,4,5,],
                    [23,1,2,3,4,5],
                    [33,1,2,3,4,5]] 
#----------------------------------------------------------------------------------------    
menu = print("""
A)Cargar planilla             
B)Mostrar la recaudación de todos los coches y líneas.
C)Calcular y mostrar recaudación por línea.
D)Calcular y mostrar recaudación por coche.
E)Calcular y mostrar la recaudación total.
F)Salir""")
#--------------------------------------------------------------------------------------  
while True:
    opcion = input("Elegir una de estas opciones: ")
#--------------------------------------------------------------------------------------  
    if opcion == "A": 
        bandera_validar = True
        continuar = "si"
#--------------------------------------------------------------------------------------  
        while continuar == "si":
            legajo = int(input("Por favor ingrese su legajo: "))
            cargar_legajo(legajo) 
            coche = int(input("Por favor ingrese el coche: "))
            cargar_coche(coche)
            linea = int(input("Por favor ingrese linea : "))
            cargar_linea(linea)
            matriz_recaudacion = cargar_recaudacion(
                recaudacion=int(input("Ingrese la recaudacion: ")),
                coche=coche,
                linea=linea,
                matriz_recaudacion=matriz_recaudacion,
                matriz_colectivo=matriz_colectivo)        
            mostrar_matriz(matriz_recaudacion)
            continuar = input("¿Desea continuar? si/no: ")
#--------------------------------------------------------------------------------------  
    elif bandera_validar:            
        if opcion == "B":
            mostrar_recaudacion(matriz_recaudacion)                            
        elif opcion == "C":
            calcular_recaudacion_linea(matriz_recaudacion)  
        elif opcion == "D":
            calcular_recaudacion_coche(matriz_recaudacion)     
        elif opcion == "E":
            calcular_recaudacion_total(matriz_recaudacion)
        elif opcion == "F":
            continuar = input("¿Desea salir? si/no: ")
            if continuar == "si":
                break
        else:
            print("Error: ingrese una opción válida.")
    else: 
       print("Error: seleccione la opción 'A' primero para cargar los datos.") 
#--------------------------------------------------------------------------------------         