
def prueba_validaciones():
    print("\n=== PRUEBAS DE VALIDACIONES ===")

    # ---- TÍTULO ----
    assert v.validar_titulo("Matrix")[0] is True
    assert v.validar_titulo("   ")[0] is False
    assert v.validar_titulo("El señor de los anillos")[0] is True

    # ---- AÑO ----
    assert v.validar_año(config.año_minimo)[0] is True
    assert v.validar_año(config.año_maximo)[0] is True
    assert v.validar_año(config.año_minimo - 1)[0] is False
    assert v.validar_año(config.año_maximo + 1)[0] is False
    assert v.validar_año("texto")[0] is False

    # ---- GÉNERO ----
    assert v.validar_genero("Drama")[0] is True
    assert v.validar_genero("   ")[0] is False
    assert v.validar_genero("Inventado")[0] is False
    assert v.validar_genero("Drama/Thriller")[0] is True
    assert v.validar_genero("Drama//Thriller")[0] is False
    assert v.validar_genero("Drama/Inventado")[0] is False

    # ---- RATING ----
    assert v.validar_rating(0)[0] is True
    assert v.validar_rating(10)[0] is True
    assert v.validar_rating(-1)[0] is False
    assert v.validar_rating(11)[0] is False
    assert v.validar_rating("texto")[0] is False

    # ---- DIRECTOR ----
    assert v.validar_director("Christopher Nolan")[0] is True
    assert v.validar_director("   ")[0] is False
    assert v.validar_director("X")[0] is False  # menor al mínimo
    nombre_largo = "a" * (config.longitud_max_director + 1)
    assert v.validar_director(nombre_largo)[0] is False
    assert v.validar_director("Nombre 123")[0] is False  # caracteres inválidos

    # ---- DURACIÓN ----
    assert v.validar_duracion(config.duracion_minima)[0] is True
    assert v.validar_duracion(config.duracion_maxima)[0] is True
    assert v.validar_duracion(config.duracion_minima - 1)[0] is False
    assert v.validar_duracion(config.duracion_maxima + 1)[0] is False
    assert v.validar_duracion("texto")[0] is False

    print("✅ Todas las pruebas de validaciones pasaron.")

