
"""
interfaz.py
Interfaz de usuario por consola para gestionar películas.
Usa validaciones robustas y operaciones CRUD del módulo database.
"""
from typing import Dict, Any
import sys
import database
import validaciones as v
import config

SEPARADOR = "-" * 60

def _input_entero(mensaje: str) -> int:
    valor = input(mensaje).strip()
    try:
        return int(valor)
    except ValueError:
        raise ValueError(config.mensaje_error["anio_numero"])

def _input_flotante(mensaje: str) -> float:
    valor = input(mensaje).strip().replace(",", ".")
    try:
        return float(valor)
    except ValueError:
        raise ValueError(config.mensaje_error["rating_numero"])

def pedir_datos_pelicula() -> Dict[str, Any]:
    """Solicita datos al usuario y valida cada campo.
    Lanza ValueError si algún campo no es válido.
    """
    titulo = v.validar_titulo(input("Título: "))
    anio = v.validar_anio(_input_entero("Año (ej. 2010): "))
    genero = v.validar_genero(input("Género: "))
    rating = v.validar_rating(_input_flotante("Rating (0-10): "))
    director = v.validar_director(input("Director/a: "))
    duracion = v.validar_duracion(_input_entero("Duración (min): "))
    return {
        "titulo": titulo,
        "anio": anio,
        "genero": genero,
        "rating": rating,
        "director": director,
        "duracion": duracion,
    }

def mostrar_menu() -> None:
    print(SEPARADOR)
    print("🎬 GESTOR DE PELÍCULAS")
    print(SEPARADOR)
    print("1) Listar todas")
    print("2) Buscar por nombre (clave)")
    print("3) Agregar")
    print("4) Actualizar")
    print("5) Eliminar")
    print("6) Estadísticas")
    print("0) Salir")
    print(SEPARADOR)

def pedir_opcion() -> str:
    return input("Elige una opción: ").strip()

def listar_todas() -> None:
    peliculas = database.obtener_todas_peliculas()
    if not peliculas:
        print("No hay películas registradas.")
        return
    print(f"Total: {database.total_peliculas()}")
    for p in peliculas:
        print(f"- {p['titulo']} ({p['anio']}) • {p['genero']} • {p['rating']}/10 • {p['duracion']} min")

def buscar_por_nombre() -> None:
    nombre = input("Ingresa el nombre/clave (ej. matrix): ").strip()
    peli = database.buscar_pelicula(nombre)
    if not peli:
        print("❌ Película no encontrada.")
        return
    print(SEPARADOR)
    print(f"🏷️  Título:   {peli['titulo']}")
    print(f"📅  Año:      {peli['anio']}")
    print(f"🎭  Género:   {peli['genero']}")
    print(f"⭐  Rating:   {peli['rating']}")
    print(f"🎬  Director: {peli['director']}")
    print(f"⏱️  Duración: {peli['duracion']} min")

def agregar() -> None:
    try:
        datos = pedir_datos_pelicula()
        clave = datos["titulo"].lower()
        ok, msg = database.agregar_pelicula(clave, datos)
        print(msg)
    except ValueError as e:
        print(f"❗ Error de validación: {e}")

def actualizar() -> None:
    nombre = input("Clave de la película a actualizar (ej. matrix): ").strip().lower()
    if not database.existe_pelicula(nombre):
        print("❌ Película no encontrada.")
        return
    print("Deja en blanco para mantener el valor actual.")
    actual = database.buscar_pelicula(nombre)
    try:
        # Campos opcionales (si se deja vacío, se conserva)
        nuevo_titulo = input(f"Título [{actual['titulo']}]: ").strip()
        if nuevo_titulo:
            actual["titulo"] = v.validar_titulo(nuevo_titulo)

        anio_txt = input(f"Año [{actual['anio']}]: ").strip()
        if anio_txt:
            actual["anio"] = v.validar_anio(int(anio_txt))

        genero_txt = input(f"Género [{actual['genero']}]: ").strip()
        if genero_txt:
            actual["genero"] = v.validar_genero(genero_txt)

        rating_txt = input(f"Rating [{actual['rating']}]: ").strip().replace(",", ".")
        if rating_txt:
            actual["rating"] = v.validar_rating(float(rating_txt))

        director_txt = input(f"Director/a [{actual['director']}]: ").strip()
        if director_txt:
            actual["director"] = v.validar_director(director_txt)

        duracion_txt = input(f"Duración [{actual['duracion']}]: ").strip()
        if duracion_txt:
            actual["duracion"] = v.validar_duracion(int(duracion_txt))

        ok, msg = database.actualizar_pelicula(nombre, actual)
        print(msg)
    except ValueError as e:
        print(f"❗ Error de validación: {e}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

def eliminar() -> None:
    nombre = input("Clave de la película a eliminar (ej. matrix): ").strip()
    ok, msg = database.eliminar_pelicula(nombre)
    print(msg)

def estadisticas() -> None:
    total = database.total_peliculas()
    peliculas = database.obtener_todas_peliculas()
    if not peliculas:
        print("No hay películas para analizar.")
        return
    promedio_rating = round(sum(p['rating'] for p in peliculas) / total, 2)
    promedio_duracion = round(sum(p['duracion'] for p in peliculas) / total, 2)
    anio_min = min(p['anio'] for p in peliculas)
    anio_max = max(p['anio'] for p in peliculas)
    print(SEPARADOR)
    print(f"📊 Total de películas: {total}")
    print(f"⭐ Rating promedio: {promedio_rating}")
    print(f"⏱️ Duración promedio: {promedio_duracion} min")
    print(f"📅 Rango de años: {anio_min} - {anio_max}")
    print(SEPARADOR)
