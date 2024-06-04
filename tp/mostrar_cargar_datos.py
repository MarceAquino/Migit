import json
def cargar_personas_desde_csv(path:str)->list[dict]:
    lista_empleados = []
    with open(path,"r") as archivo:
        linea = archivo.readlines()    

        for  i in range(1,len(linea)):
            datos = linea[i]
            datos = datos.split(",")

            ids =int(datos[0])
            nombre = datos[1]
            apellido = datos[2]
            puesto = datos[3]
            salario = datos[4]
            salario = salario.replace("\n","")
            salario = int(salario)
        


            persona = {"id":ids,
                        "nombre":nombre,
                        "apellido":apellido,
                        "puesto":puesto,
                        "salario":salario}
            lista_empleados.append(persona)

        return lista_empleados   

def guardar_csv_persona (lista_empleados:list[dict],path:str):
    with open(path,"w") as archivo:
        archivo.write("id,nombre,apellido,puesto,salario,\n")
        for i in range(len(lista_empleados)):
            persona = lista_empleados[i]
            ids = persona["id"]
            nombre = persona["nombre"]
            apellido = persona["apellido"]
            puesto = persona["puesto"]
            salario = persona["salario"]
            archivo.write(f"{ids},{nombre},{apellido},{puesto},{salario}\n")

def guardar_persona_desde_json(lista_empleados:list[dict],path:str):

    data = {}
    data["persona"] = lista_empleados 
    with open(path,"w") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)
         


def cargar_personas_desde_json(path:str)->list[dict]:

    with open(path,"r") as archivo:
        retorno = json.load(archivo)
    return retorno["persona"]

#----------------------------------------------------------------------------------------------------------------
def mostrar_persona(persona:dict)->None:
    
    mensaje = f"""
                ********************************************************************************************
                Nombre: {persona['nombre']}
                Apellido: {persona['apellido']}	
                Puesto: {persona['puesto']}
                Salario: {persona['salario']}
                ******************************************************************************************** 
                """
    return print(mensaje)  
#---------------------------------------------------------------------------------------------------------------- 
def mostrar_personas(lista_empeados:list[dict])->None:
    guardar_csv_persona (lista_empeados,"Migit/tp/empleados.csv")
    guardar_persona_desde_json(lista_empeados,"Migit/tp/empleados.json")
    print("==== Los empleados encontrados son ====\n")
    for i in range (len(lista_empeados)):
        mostrar_persona(lista_empeados[i])
#----------------------------------------------------------------------------------------------------------------
def mostrar_personas_por_puesto(lista_empleados:list[dict], puesto: str)->None:

    print(f"==== Los {puesto} encontrados son ====\n")
    for i in range(len(lista_empleados)):
        if lista_empleados[i]['puesto'] == puesto:
            mostrar_persona(lista_empleados[i])       
#----------------------------------------------------------------------------------------------------------------            