# Base de datos simulada
peliculas_database = {
    "matrix": {
        "titulo": "Matrix",
        "anio": 1999,
        "genero": "Ciencia Ficción",
        "rating": 9.0,
        "director": "Lana y Lilly Wachowski",
        "duracion": 136
    },
    "inception": {
        "titulo": "Inception",
        "anio": 2010,
        "genero": "Acción/Ciencia Ficción",
        "rating": 8.8,
        "director": "Christopher Nolan",
        "duracion": 148
    },
    "parasite": {
        "titulo": "Parasite",
        "anio": 2019,
        "genero": "Drama/Thriller",
        "rating": 8.6,
        "director": "Bong Joon-ho",
        "duracion": 132
    },
}

# -------- CRUD --------
def agregar_pelicula(nombre, datos):
    clave = nombre.lower()
    if clave in peliculas_database:
        return False, "❌ La película ya está registrada."
    peliculas_database[clave] = datos
    return True, f"✅ {datos['titulo']} ha sido registrada."

def eliminar_pelicula(nombre):
    clave = nombre.lower()
    if clave not in peliculas_database:
        return False, "❌ Película no encontrada."
    titulo = peliculas_database[clave]["titulo"]
    del peliculas_database[clave]
    return True, f"🗑️ {titulo} ha sido eliminada."

def buscar_pelicula(nombre):
    return peliculas_database.get(nombre.lower(), None)

def obtener_todas_peliculas():
    return sorted(peliculas_database.values(), key=lambda x: x["titulo"])

def actualizar_pelicula(nombre, nuevos_datos):
    clave = nombre.lower()
    if clave not in peliculas_database:
        return False, "❌ Película no encontrada."
    peliculas_database[clave].update(nuevos_datos)
    return True, f"✏️ Los datos de {peliculas_database[clave]['titulo']} se han actualizado."

def existe_pelicula(nombre):
    return nombre.lower() in peliculas_database

def total_peliculas():
    return len(peliculas_database)
