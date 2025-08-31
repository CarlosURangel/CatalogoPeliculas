# Base de datos
peliculas_database = {
    "matrix": {
        "titulo": "Matrix",
        "año": 1999,
        "genero": "Ciencia Ficción",
        "rating": 9.0,
        "director": "Lana y Lilly Wachowski",
        "duracion": 136
    },
    "inception": {
        "titulo": "Inception",
        "año": 2010,
        "genero": "Acción/Ciencia Ficción",
        "rating": 8.8,
        "director": "Christopher Nolan",
        "duracion": 148
    },
    "parasite": {
        "titulo": "Parasite",
        "año": 2019,
        "genero": "Drama/Thriller",
        "rating": 8.6,
        "director": "Bong Joon-ho",
        "duracion": 132
    },
}

# CRUD
# Agregar pelicula 
def agregar_pelicula(nombre, datos):
    pelicula = nombre.lower()
    if pelicula in peliculas_database:
        return False, "La película ya está registrada"
    peliculas_database[pelicula] = datos
    return True, f" {pelicula} ha sido registrada"

# Eliminar pelicula
def eliminar_pelicula(nombre):
    pelicula = nombre.lower()
    if pelicula not in peliculas_database:
        return False, "Película no encontrada."
    titulo = peliculas_database[pelicula]["titulo"]
    del peliculas_database[pelicula]
    return True, f"{titulo} ha sido eliminada."

# Buscar pelicula
def buscar_pelicula(nombre):
    return peliculas_database.get(nombre.lower(), None)

#Listar peliculas
def obtener_todas_peliculas():
    return sorted(peliculas_database.values(), key=lambda x: x["titulo"])

# Actualizar pelicula
def actualizar_pelicula(nombre, nuevos_datos):
    pelicula = nombre.lower()
    if pelicula not in peliculas_database:
        return False, "Película no encontrada"
    peliculas_database[pelicula].update(nuevos_datos)
    return True, f"Los datos de {peliculas_database[pelicula]['titulo']} se han actualizado."


def existe_pelicula(nombre):
    return nombre.lower() in peliculas_database

def total_peliculas():
    return len(peliculas_database)
