
#------------------------------------------------------------------------------
def cargar_peliculas_csv(path: str) -> list[dict]:
    lista_peliculas = []
    titulos_set = set()

    with open(path, "r", encoding='utf-8') as archivo:
        lineas = archivo.readlines()

        for linea in lineas[1:]:  # Iterar sobre cada línea excepto la primera (encabezado)
            datos = linea.strip().split(",")
            
            # Verificar si hay suficientes elementos en la lista de datos
            if len(datos) < 7:
                continue

            titulo = datos[1]
            if titulo in titulos_set:
                continue

            ids = int(datos[0])
            genero = datos[2]
            año_de_lanzamiento = datos[3]
            duracion = datos[4]
            atp = datos[5]
            plataformas = datos[6].replace("\n", "")

            pelicula = {
                "id": ids,
                "titulo": titulo,
                "genero": genero,
                "año_de_lanzamiento": año_de_lanzamiento,
                "duracion": duracion,
                "atp": atp,
                "plataformas": plataformas
            }

            lista_peliculas.append(pelicula)
            titulos_set.add(titulo)

    return lista_peliculas
#------------------------------------------------------------------------------
def guardar_peliculas_csv(lista_peliculas:list[dict],path:str):

    with open(path,"w",encoding='utf-8') as archivo:
        archivo.write("id,titulo,genero,año_de_lanzamiento,duracion,atp,plataformas\n")

        for i in range(len(lista_peliculas)):
            pelicula = lista_peliculas[i]
            ids = pelicula["id"]
            titulo = pelicula["titulo"]
            genero = pelicula["genero"]
            anio_de_lanzamiento = pelicula["año_de_lanzamiento"]
            duracion = pelicula["duracion"]
            atp = pelicula["atp"]
            plataformas = pelicula["plataformas"]

            if type(plataformas) == list:
                plataformas = "-".join(plataformas)

            archivo.write(f"{ids},{titulo},{genero},{anio_de_lanzamiento},{duracion},{atp},{plataformas}\n")
#------------------------------------------------------------------------------
