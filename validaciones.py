import config

def validar_titulo(titulo):
    if not titulo.strip():
        raise ValueError(config.mensaje_error["titulo_vacio"])
    return titulo.strip()

def validar_anio(anio):
    if not isinstance(anio, int):
        raise ValueError(config.mensaje_error["anio_numero"])
    if not (config.anio_minimo <= anio <= config.anio_maximo):
        raise ValueError(config.mensaje_error["anio_rango"])
    return anio

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
