
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
            respuesta = texto
        else:
            respuesta = "No alcanza la tinta"
        return respuesta

    def recargar(self, cantidad_recargar: int) -> str:
        suma_tinta = self.cantidad_tinta + cantidad_recargar
        if suma_tinta <= self.capacidad_tinta_maxima:
            self.cantidad_tinta = suma_tinta
            respuesta = "Lapicera recargada"
        else:
            diferencia_de_tinta = suma_tinta - self.capacidad_tinta_maxima
            self.cantidad_tinta = self.capacidad_tinta_maxima
            respuesta = f"Se recargó la lapicera y sobró {diferencia_de_tinta}"
        return respuesta



