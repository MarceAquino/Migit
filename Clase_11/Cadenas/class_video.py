from datetime import datetime

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
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)
      

    def dividir_titulo(self) -> str:
        cadena = self.titulo.split("|")
        colaborador = cadena[0]
        colaborador = colaborador.strip()
        sesion = cadena[1]
        sesion = sesion.replace("Sesión #", "")
        sesion = sesion.strip()
        self.colaborador = colaborador
        self.sesion = int(sesion)

    def obtener_numero_sesion(self)->int:
        dividir = self.titulo
        dividir = dividir.split(" | Sesión #")
        numero_sesion = int(dividir[1])

        return numero_sesion    
    
    def obtener_codigo_url(self):
        url = self.url_youtube
        codigo_url = url.replace("https://www.youtube.com/watch?v=", "")
        self.codigo_url = codigo_url
    
    def formatear_fecha(self):

        fecha = (self.fecha_lanzamiento.split("-"))
        año = int(fecha[0])
        mes = int(fecha[1])
        dia = int(fecha[2])
        fecha_objeto = datetime(año, mes, dia)
        self.fecha_lanzamiento = fecha_objeto

    def cantidad_vistas (self)->int:
        suma = self.vistas
        return suma

    def mostrar_url (self)->str:
        url = self.codigo_url
        return url       
    def mostrar_colaborador(self)->str:
        colaborador = self.colaborador
        return colaborador




      
   

