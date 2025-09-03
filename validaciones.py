from config import *

def validar_titulo(titulo):
    if not isinstance(titulo, str) or titulo.strip() == "":
        return False, mensaje_error["titulo_vacio"]
    return True, titulo

def validar_año(año):
    try:
        año = int(año)
        if año < año_minimo or año > año_maximo:
            return False, mensaje_error["año_rango"]
        return True, año
    except:
        return False, mensaje_error["año_numero"]

def validar_genero(genero):
    if not isinstance(genero, str) or genero.strip() == "":
        return False, mensaje_error["genero_vacio"]
    genero = genero.strip()
    if genero not in generos_peliculas:
        return False, f"Género no válido. Opciones: {', '.join(generos_peliculas)}"
    return True, genero

def validar_rating(rating):
    try:
        rating = float(rating)
        if rating < rating_minimo or rating > rating_maximo:
            return False, mensaje_error["rating_rango"]
        return True, rating
    except:
        return False, mensaje_error["rating_numero"]

def validar_director(director):
    if not isinstance(director, str) or director.strip() == "":
        return False, mensaje_error["director_vacio"]
    director = director.strip()
    if len(director) < longitud_min_director or len(director) > longitud_max_director:
        return False, "El nombre del director debe tener entre 3 y 50 caracteres."
    if not all(c.isalpha() or c.isspace() for c in director):
        return False, "El nombre del director solo puede contener letras y espacios."
    return True, director

def validar_duracion(duracion):
    try:
        duracion = int(duracion)
        if duracion < duracion_minima or duracion > duracion_maxima:
            return False, mensaje_error["duracion_rango"]
        return True, duracion
    except:
        return False, mensaje_error["duracion_numero"]

def validar_datos_completos(datos):
    try:
        valido, mensaje = validar_titulo(datos["titulo"])
        if not valido: return False, mensaje

        valido, mensaje = validar_año(datos["año"])
        if not valido: return False, mensaje

        valido, mensaje = validar_genero(datos["genero"])
        if not valido: return False, mensaje

        valido, mensaje = validar_rating(datos["rating"])
        if not valido: return False, mensaje

        valido, mensaje = validar_director(datos["director"])
        if not valido: return False, mensaje

        valido, mensaje = validar_duracion(datos["duracion"])
        if not valido: return False, mensaje

        return True, datos
    except KeyError as e:
        return False, f"Falta el campo {e}"
    except Exception as e:
        return False, str(e)
