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
        retorno = print("Verifique que el campo ingresado sea un puesto valido.")
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
def validar_existencia_id(lista: list[dict])->int:
    while True:
        id_a_modificar = validar_entero("Ingrese un ID : ")
        for i in range(len(lista)):
            if id_a_modificar == lista[i]['id']:
                return id_a_modificar
        print("ERROR. ID no encontrado")
            
#----------------------------------------------------------------------------------------------------------------       
def validar_opcion_menu()->str:
    eleccion = input("Ingrese la opcion que quiera modificar: ")
    lista_opciones_validar = ["a", "b", "c", "d", "e"]
    while True:
        while eleccion.isalpha() == False or len(eleccion) > 1:
            eleccion = input("Reingrese una opcion válida: ")
        opcion = eleccion
        if eleccion.isalpha() == True:
            eleccion = eleccion.lower()
            for eleccion in lista_opciones_validar: 
                return opcion
#----------------------------------------------------------------------------------------------------------------
def validad_lista(lista_empleados:list[dict])-> bool:
    mensaje = False
    longitud = len(lista_empleados)
    if longitud > 0:
        mensaje = True
    return mensaje    

        