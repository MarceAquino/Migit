
class Boligrafo:
    def __init__(self, color: str, grosor: str) -> None:
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80
        self.grosor_punta = grosor
        self.color = color

    def escribir(self, texto: str) -> str:
        longitud = len(texto)
    
        if self.cantidad_tinta >= longitud:
            self.cantidad_tinta -= longitud
            respuesta = f"¨{texto} la longitud del texto es de {longitud} caracteres, La tinta restante es % {self.cantidad_tinta}"
        else:
            respuesta = f"No alcanza la tinta, la cantidad de tinta actual es: % {self.cantidad_tinta} y el texto ingresado es de {longitud} caracteres." 
        return respuesta

    def recargar(self, cantidad_recargar: int) -> str:

        suma_tinta = self.cantidad_tinta+ cantidad_recargar
        if suma_tinta <= self.capacidad_tinta_maxima:
            self.cantidad_tinta = suma_tinta
            respuesta = f"Lapicera recargada el cartucho quedo cargado en un % {self.cantidad_tinta}"
        else:
            diferencia_de_tinta = suma_tinta - self.capacidad_tinta_maxima
            self.cantidad_tinta = self.capacidad_tinta_maxima
            respuesta = f"Se recargó la lapicera un % {cantidad_recargar} y sobró  % {diferencia_de_tinta}"
        return respuesta





