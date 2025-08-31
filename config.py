# Configuracion de validaciones
año_minimo = 1900
año_maximo = 2025
rating_minimo = 0.0
rating_maximo = 10.0
duracion_minima = 1
duracion_maxima = 400

# Mensajes de error
mensaje_error = {
    "titulo_vacio": "El título no puede estar vacío.",
    "año_rango": f"El año debe estar entre {año_minimo} y {año_maximo}.",
    "año_numero": "El año debe ser un número.",
    "rating_rango": f"El rating debe estar entre {rating_minimo} y {rating_maximo}.",
    "rating_numero": "El rating debe ser un número.",
    "genero_vacio": "El género no puede estar vacío.",
    "director_vacio": "El nombre del director no puede estar vacío.",
    "duracion_rango": f"La duración debe estar entre {duracion_minima} y {duracion_maxima} minutos.",
    "duracion_numero": "La duración debe ser un número."
}
