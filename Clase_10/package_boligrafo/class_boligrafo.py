from colorama import init, Fore, Style

class Boligrafo:
    def __init__(self, color: str, grosor: str) -> None:
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80
        self.grosor_punta = grosor
        self.color = color
       

    def estilo_color(self) -> str:
        if self.color.lower() == "rojo":
            return Fore.RED
        elif self.color.lower() == "azul":
            return Fore.BLUE
        elif self.color.lower() == "verde":
            return Fore.GREEN
        else:
            return "" 
            
    def escribir(self, texto: str) -> str:
        longitud = len(texto)
        texto_con_color = f"{self.estilo_color()}{texto}{Style.RESET_ALL}" 
        
        if self.cantidad_tinta >= longitud:
            self.cantidad_tinta -= longitud
            respuesta = f"{texto_con_color} - La longitud del texto es de {longitud} caracteres. La tinta restante es {self.cantidad_tinta}%"
        else:
            respuesta = f"No hay suficiente tinta. La cantidad de tinta actual es {self.cantidad_tinta}%. El texto ingresado tiene {longitud} caracteres."
        
        return respuesta


    def recargar(self,cantidad_recargar:str) -> str|int:
        cantidad_recargar = int(cantidad_recargar)
        suma_tinta = self.cantidad_tinta+ cantidad_recargar
        if suma_tinta <= self.capacidad_tinta_maxima:
            self.cantidad_tinta = suma_tinta
            respuesta = f"Lapicera recargada el cartucho quedo cargado en un % {self.cantidad_tinta}"
        else:
            continuar = input("La cantidad de tinta a recargar es mayor que la capacidad de la lapizera desea continuar si/no : ")
            if continuar == "si":
                diferencia_de_tinta = suma_tinta - self.capacidad_tinta_maxima
                self.cantidad_tinta = self.capacidad_tinta_maxima
                respuesta = f"Se recargó la lapicera un % {cantidad_recargar} y sobró  % {diferencia_de_tinta}"
            else:
                respuesta = "Muchas gracias por por no desperdiciar la tinta que tenga un buen dia." 


        return respuesta





