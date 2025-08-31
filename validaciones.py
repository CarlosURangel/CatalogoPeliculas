import config

def validar_titulo(titulo):
    if not titulo.strip():
        raise ValueError(config.mensaje_error["titulo_vacio"])
    return titulo.strip()

def validar_año(año):
    if not isinstance(año, int):
        raise ValueError(config.mensaje_error["año_numero"])
    if not (config.año_minimo <= año <= config.año_maximo):
        raise ValueError(config.mensaje_error["año_rango"])
    return año

def validar_rating(rating):
    if not isinstance(rating, (int, float)):
        raise ValueError(config.mensaje_error["rating_numero"])
    if not (config.rating_minimo <= rating <= config.rating_maximo):
        raise ValueError(config.mensaje_error["rating_rango"])
    return rating

def validar_genero(genero):
    if not genero.strip():
        raise ValueError(config.mensaje_error["genero_vacio"])
    return genero.strip()

def validar_director(director):
    if not director.strip():
        raise ValueError(config.mensaje_error["director_vacio"])
    return director.strip()

def validar_duracion(duracion):
    if not isinstance(duracion, int):
        raise ValueError(config.mensaje_error["duracion_numero"])
    if not (config.duracion_minima <= duracion <= config.duracion_maxima):
        raise ValueError(config.mensaje_error["duracion_rango"])
    return duracion
