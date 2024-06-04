

def validar_id (lista_empleados:list[dict]):
    lista_ids = []
    for i in range(len(lista_empleados)):
        lista_ids.append(lista_empleados[i]["id"])
    return lista_ids    
        
#----------------------------------------------------------------------------------------------------------------
def validar_nombre_apellido(clave:str)->str|None:

    identificacion = input (f"Ingrese el {clave}: ")
    longitud = len(identificacion)
    validar_letras = identificacion.isalpha()
    while True:

        if validar_letras == False or longitud > 15:
            print("Verifique que el campo ingresado no tenga mas de 15 caracteres y sean todos alfabeticos.")
            identificacion = input (f"Ingrese el {clave}: ")
            validar_letras = identificacion.isalpha()
        else:
            return identificacion
        
#----------------------------------------------------------------------------------------------------------------
def validar_puesto()->str:

    lista_puestos = ["Gerente","Supervisor","Analista","Encargado","Asistente"]
    puesto = input ("Ingrese el puesto: ").capitalize()

    while True:
        for i in range(len(lista_puestos)):
            if puesto == lista_puestos[i]:
                retorno = puesto
                return retorno
            
        retorno = print("""
        Verifique que el campo ingresado sea un puesto valido:
        --Gerente---Supervisor---Analista---Encargado---Asistente-- """)
        puesto = input (f"Ingrese un puesto valido puesto: ").capitalize()
            
#----------------------------------------------------------------------------------------------------------------
def validar_salario()->int:

    salario = input("Ingrese un salario: ")
    while salario.isnumeric() != True or int(salario) < 234315:
        salario = input ("Error ingrese solo numeros y un valor superior a $234315: ")

    salario = int(salario)
    return salario
#----------------------------------------------------------------------------------------------------------------
def validar_entero(mensaje:str)->int:

    dato = input(mensaje)

    while dato.isnumeric() == False:
        dato = input("Error reingrese nuevamente un numero valido: ")
    dato = int(dato)
    return dato
#----------------------------------------------------------------------------------------------------------------
def validar_existencia_id(lista_empleados:list[dict],ids:int)->int:
        
        mensaje = False
        for i in range(len(lista_empleados)):
            if ids == lista_empleados[i]["id"]:
                mensaje = True
        return mensaje        
            
        
#----------------------------------------------------------------------------------------------------------------       
def validar_opcion_menu()->str:

    eleccion = input("Ingrese la opcion que quiera modificar: ")
    lista_opciones_validar = ["a", "b", "c", "d", "e"]

    while True:
        while eleccion.isalpha() == False or len(eleccion) > 1:
            eleccion = input("Reingrese una opcion válida (--a--b--c--d--e--): ")
        opcion = eleccion

        if eleccion.isalpha() == True:
            eleccion = eleccion.lower()

            for eleccion in lista_opciones_validar: 
                return opcion

#----------------------------------------------------------------------------------------------------------------
def validar_lista_vacia(lista_empleados:list[dict])->bool:
    mensaje = False
    if len(lista_empleados) > 0:
        mensaje = True
    return mensaje


    