# Base de datos
peliculas_database = {
    "lost in translation": {
        "titulo": "Lost in Translation",
        "año": 2003,
        "genero": "Drama/Romance",
        "rating": 7.7,
        "director": "Sofia Coppola",
        "duracion": 102
    },
    "rocky": {
        "titulo": "Rocky",
        "año": 1976,
        "genero": "Deporte",
        "rating": 8.1,
        "director": "John G. Avildsen",
        "duracion": 120
    },
    "reyes de las olas": {
        "titulo": "Reyes de las Olas",
        "año": 2007,
        "genero": "Animación/Comedia",
        "rating": 6.7,
        "director": "Ash Brannon",
        "duracion": 85
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
