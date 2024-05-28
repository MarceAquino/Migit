import datetime
from datetime import *

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print("*"*30)
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime('%d-%m-%Y')}")
        print("*"*30)

    def dividir_titulo(self):
        #Debe setear el atributo sesion y colaborador con los datos obtenidos del 
        #titulo del video
        dividir = self.titulo
        dividir = dividir.split(" | Sesión #")
        self.colaborador = dividir[0]
        self.sesion = dividir[1]
    
    def obtener_codigo_url(self):
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13
        #el codigo seria nicki13
        url_split = self.url_youtube.split("=")
        self.codigo_url = url_split[1]
    
    def formatear_fecha(self):
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberan dividir la fecha (en formato string) en dia, mes y año y a partir de 
        #esos datos, crear la nueva fecha. 
        fecha_string = self.fecha_lanzamiento.split("-")
        año =  int(fecha_string[0])
        mes =  int(fecha_string[1])
        dia =  int(fecha_string[2])
        fecha_lanzamiento = datetime(año,mes,dia)
        self.fecha_lanzamiento = fecha_lanzamiento
    
    def obtener_numero_sesion(self)->int:
        dividir = self.titulo
        dividir = dividir.split(" | Sesión #")
        numero_sesion = int(dividir[1])
        return numero_sesion
    
    def cantidad_vistas(self)->int:
        cantidad_vistas = self.vistas
        return cantidad_vistas
    
    def mostrar_url(self):
        url = self.url_youtube
        return url
    def mostrar_colaborador(self)->str:
        colaborador = self.colaborador
        return colaborador
    


    
def mostrar_opciones():
    print("""
        - A) NORMALIZAR OBJETOS
        - B) MOSTRAR TEMAS
        - C) ORDENAR TEMAS
        - D) PROMEDIO DE VISTAS
        - E) MAXIMA REPRODUCCION
        - F) BUSQUEDA POR CODIGO
        - G) LISTAR POR COLABORADOR
        - H) SALIR
          """)

def normalizar_datos(lista_videos: list[Video])->None:
    for i in range(len(lista_videos)):
        lista_videos[i].dividir_titulo()
        lista_videos[i].obtener_codigo_url()
        lista_videos[i].formatear_fecha()
    print("NORMALIZACION DE OBJETOS LISTA!")
   
def mostrar_temas(lista_videos: list[Video]):
    for i in range(len(lista_videos)):
        lista_videos[i].mostrar_tema()

def ordenar_temas(lista_videos: list[Video]):
    for i in range(len(lista_videos)):
        for j in range(0, len(lista_videos) -i -1):
            if lista_videos[j].obtener_numero_sesion() > lista_videos[j+1].obtener_numero_sesion():
                aux = lista_videos[j]
                lista_videos[j] = lista_videos[j+1]
                lista_videos[j+1] = aux
        lista_videos[i].mostrar_tema()

def promediar_vistas(lista_videos: list[Video]):
    suma = 0
    for i in range(len(lista_videos)):
        suma += lista_videos[i].cantidad_vistas()
    promedio = suma / len(lista_videos)
    cantidad_k = promedio / 1000
    print(f"El promedio de vistas en K es: {round(cantidad_k)}k")

def buscar_maxima_reproduccion(lista_videos: list[Video]):
    bandera = False
    for i in range(len(lista_videos)):
        if bandera == False or lista_videos[i].cantidad_vistas() > num_max:
            num_max = lista_videos[i].cantidad_vistas()
            bandera = True
    print(num_max)

def buscar_por_codigo(lista_videos: list[Video]):
    for i in range(len(lista_videos)):
        buscar = lista_videos[i].mostrar_url()
        buscar = buscar.count("nick")
        if buscar >= 1:
            lista_videos[i].mostrar_tema()

def listar_colaborador(lista_videos: list[Video]):
    colaborador = input("Ingrese el nombre de un colaborador: ")
    for i in range(len(lista_videos)):
        buscar = lista_videos[i].mostrar_colaborador()
        buscar = buscar.count(colaborador)
        if buscar >= 1:
            lista_videos[i].mostrar_tema()