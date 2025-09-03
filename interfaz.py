
# INTERFAZ DE USUARIO

import database
import validaciones
import config


def limpiar_pantalla():
    print("\n" * 30)


def mostrar_menu_principal():
    print("=" * 60)
    print("CATALOGO DE PELICULAS")
    print("=" * 60)
    print("1. Agregar pelicula")
    print("2. Eliminar pelicula")
    print("3. Buscar pelicula")
    print("4. Ver todas las peliculas")
    print("5. Actualizar pelicula")
    print("6. Ver generos disponibles")
    print("7. Estadisticas")
    print("8. Salir")
    print("=" * 60)


def mostrar_generos_peliculas():
    print("\n" + "=" * 40)
    print("GENEROS DE PELICULAS DISPONIBLES")
    print("=" * 40)

    for i, genero in enumerate(config.generos_peliculas, 1):
        print(f"{i:2d}. {genero}", end="   ")
        if i % 4 == 0:
            print()
    print(f"\n\nTotal: {len(config.generos_peliculas)} generos disponibles")


def mostrar_estadisticas():
    """Muestra estadisticas del catalogo de peliculas"""
    total = database.total_peliculas()
    peliculas = database.obtener_todas_peliculas()

    print("\n" + "=" * 40)
    print("ESTADISTICAS DEL CATALOGO")
    print("=" * 40)

    print(f"Total de peliculas: {total}")

    # Contar peliculas por genero
    generos_contador = {}
    for pelicula in peliculas:
        if "/" in pelicula['genero']:
            for genero in pelicula['genero'].split("/"):
                generos_contador[genero] = generos_contador.get(genero, 0) + 1
        else:
            generos_contador[pelicula['genero']] = generos_contador.get(pelicula['genero'], 0) + 1

    print("\nPeliculas por genero:")
    for genero, cantidad in sorted(generos_contador.items()):
        print(f"  {genero}: {cantidad}")

    # Pelicula con mayor rating
    if total > 0:
        mejor_pelicula = max(peliculas, key=lambda x: x['rating'])
        print(f"Mejor valorada: {mejor_pelicula['titulo']} ({mejor_pelicula['rating']}/10)")


def solicitar_datos_pelicula():
    datos = {}

    try:
        # Validar titulo
        while True:
            titulo = input("Titulo de la pelicula: ").strip()
            valido, mensaje = validaciones.validar_titulo(titulo)
            if valido:
                datos['titulo'] = mensaje
                break
            print(f"ERROR: {mensaje}")

        # Validar año
        while True:
            año = input("Año de estreno: ").strip()
            valido, mensaje = validaciones.validar_año(año)
            if valido:
                datos['año'] = mensaje
                break
            print(f"ERROR: {mensaje}")

        # Validar genero
        while True:
            print(f"\nGeneros disponibles: {', '.join(config.generos_peliculas)}")
            genero = input("Genero (ejemplo: Acción o Drama/Romance): ").strip()
            valido, mensaje = validaciones.validar_genero(genero)
            if valido:
                datos['genero'] = mensaje
                break
            print(f"ERROR: {mensaje}")

        # Validar rating
        while True:
            rating = input("Rating (0.0-10.0): ").strip()
            valido, mensaje = validaciones.validar_rating(rating)
            if valido:
                datos['rating'] = mensaje
                break
            print(f"ERROR: {mensaje}")

        # Validar director
        while True:
            director = input("Director: ").strip()
            valido, mensaje = validaciones.validar_director(director)
            if valido:
                datos['director'] = mensaje
                break
            print(f"ERROR: {mensaje}")

        # Validar duracion
        while True:
            duracion = input("Duracion en minutos: ").strip()
            valido, mensaje = validaciones.validar_duracion(duracion)
            if valido:
                datos['duracion'] = mensaje
                break
            print(f"ERROR: {mensaje}")

        return True, datos

    except KeyboardInterrupt:
        return False, "Operacion cancelada por el usuario"
    except Exception as e:
        return False, f"Error inesperado: {e}"


def menu_agregar_pelicula():
    """Menu para agregar pelicula"""
    print("\n" + "=" * 40)
    print("AGREGAR NUEVA PELICULA")
    print("=" * 40)

    exito, resultado = solicitar_datos_pelicula()
    if not exito:
        print(f"ERROR: {resultado}")
        return

    datos = resultado
    clave = datos['titulo'].lower()
    exito, mensaje = database.agregar_pelicula(clave, datos)
    print(f"\n{mensaje}")


def menu_eliminar_pelicula():
    print("\n" + "=" * 40)
    print("ELIMINAR PELICULA")
    print("=" * 40)

    titulo = input("Titulo de la pelicula a eliminar: ").strip()

    if not database.existe_pelicula(titulo):
        print("ERROR: Pelicula no encontrada")
        return

    pelicula = database.buscar_pelicula(titulo)
    print(f"\nInformacion de la pelicula:")
    print(f"   Titulo: {pelicula['titulo']}")
    print(f"   Año: {pelicula['año']}")
    print(f"   Director: {pelicula['director']}")

    confirmacion = input("\n¿Esta seguro de eliminar esta pelicula? (s/n): ").lower().strip()
    if confirmacion in ['s', 'si', 'sí']:
        exito, mensaje = database.eliminar_pelicula(titulo)
        print(mensaje)
    else:
        print("Eliminacion cancelada")


def menu_buscar_pelicula():
    print("\n" + "=" * 40)
    print("BUSCAR PELICULA")
    print("=" * 40)

    titulo = input("Titulo de la pelicula: ").strip()
    pelicula = database.buscar_pelicula(titulo)

    if not pelicula:
        print("ERROR: Pelicula no encontrada")
        return

    print(f"\nINFORMACION DE '{pelicula['titulo'].upper()}'")
    print("=" * 40)
    print(f"Titulo: {pelicula['titulo']}")
    print(f"Año: {pelicula['año']}")
    print(f"Genero: {pelicula['genero']}")
    print(f"Rating: {pelicula['rating']}/10")
    print(f"Director: {pelicula['director']}")
    print(f"Duracion: {pelicula['duracion']} minutos")


def menu_listar_peliculas():
    print("\n" + "=" * 40)
    print("LISTA DE PELICULAS")
    print("=" * 40)

    peliculas = database.obtener_todas_peliculas()

    if not peliculas:
        print("No hay peliculas en el catalogo")
        return

    for i, pelicula in enumerate(peliculas, 1):
        print(f"\n{i}. {pelicula['titulo']} ({pelicula['año']})")
        print(f"   Genero: {pelicula['genero']}")
        print(f"   Rating: {pelicula['rating']}/10")
        print(f"   Director: {pelicula['director']}")
        print(f"   Duracion: {pelicula['duracion']} min")

    print(f"\nTotal: {len(peliculas)} peliculas")


def menu_actualizar_pelicula():
    print("\n" + "=" * 40)
    print("ACTUALIZAR PELICULA")
    print("=" * 40)

    titulo = input("Titulo de la pelicula a actualizar: ").strip()

    if not database.existe_pelicula(titulo):
        print("ERROR: Pelicula no encontrada")
        return

    pelicula = database.buscar_pelicula(titulo)
    print(f"\nEditando: {pelicula['titulo']}")

    print("\nValores actuales:")
    campos = [
        ("año", "Año", str(pelicula['año']), validaciones.validar_año),
        ("genero", "Genero", pelicula['genero'], validaciones.validar_genero),
        ("rating", "Rating", str(pelicula['rating']), validaciones.validar_rating),
        ("director", "Director", pelicula['director'], validaciones.validar_director),
        ("duracion", "Duracion", str(pelicula['duracion']), validaciones.validar_duracion)
    ]

    for i, (clave, nombre_campo, valor_actual, validador) in enumerate(campos, 1):
        print(f"{i}. {nombre_campo}: {valor_actual}")

    try:
        opcion = int(input("\n¿Que campo desea actualizar? (1-5): "))
        if opcion < 1 or opcion > 5:
            print("Opcion no valida")
            return

        clave, nombre_campo, valor_actual, validador = campos[opcion - 1]
        nuevo_valor = input(f"Nuevo valor para {nombre_campo} ({valor_actual}): ").strip()

        if nuevo_valor:
            valido, resultado = validador(nuevo_valor)
            if valido:
                exito, mensaje = database.actualizar_pelicula(titulo, {clave: resultado})
                print(mensaje)
            else:
                print(f"ERROR: {resultado}")
        else:
            print("No se realizaron cambios")

    except ValueError:
        print("ERROR: Ingrese un numero valido")
    except Exception as e:
        print(f"ERROR: {e}")