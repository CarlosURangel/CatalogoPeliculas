# Pruebas automáticas

import random
import validaciones as v
import database as db
import config


def prueba_validar_titulo(cantidad=5):
    print("\n--- PRUEBAS: validar_titulo ---")
    for i in range(cantidad):
        titulo = f"Pelicula{i}"
        ok, res = v.validar_titulo(titulo)
        try:
            assert ok and res == titulo
            print(f"Prueba {i+1} superada. '{titulo}' es válido")
        except AssertionError:
            print(f"Prueba {i+1} fallida con '{titulo}'")


def prueba_validar_año():
    print("\n--- PRUEBAS: validar_año ---")
    try:
        ok, res = v.validar_año(2000)
        assert ok and res == 2000
        print("Prueba año válido superada (2000)")
    except AssertionError:
        print("Falló prueba con año válido")

    try:
        ok, res = v.validar_año(1800)  # fuera de rango
        assert not ok
        print("Prueba año inválido superada (1800)")
    except AssertionError:
        print("Falló prueba con año inválido")


def prueba_validar_genero():
    print("\n--- PRUEBAS: validar_genero ---")
    genero_ok = config.generos_peliculas[0]
    ok, res = v.validar_genero(genero_ok)
    try:
        assert ok and res == genero_ok
        print(f"Prueba género válido superada ({genero_ok})")
    except AssertionError:
        print("Falló prueba con género válido")

    ok, res = v.validar_genero("Inventado")
    try:
        assert not ok
        print("Prueba género inválido superada")
    except AssertionError:
        print("Falló prueba con género inválido")


def prueba_database_crud():
    print("\n--- PRUEBAS: CRUD en database ---")
    datos = {
        "titulo": "PruebaX",
        "año": 2020,
        "genero": "Acción",
        "rating": 7.5,
        "director": "Director Test",
        "duracion": 120,
    }
    clave = datos["titulo"].lower()

    # Agregar
    ok, msg = db.agregar_pelicula(clave, datos)
    try:
        assert ok
        print(f"Agregar: superada ({msg})")
    except AssertionError:
        print("Falló al agregar película")

    # Buscar
    peli = db.buscar_pelicula(clave)
    try:
        assert peli is not None and peli["titulo"] == "PruebaX"
        print("Buscar: superada")
    except AssertionError:
        print("Falló al buscar película")

    # Actualizar
    ok, msg = db.actualizar_pelicula(clave, {"rating": 9.0})
    try:
        assert ok and db.buscar_pelicula(clave)["rating"] == 9.0
        print("Actualizar: superada")
    except AssertionError:
        print("Falló al actualizar película")

    # Eliminar
    ok, msg = db.eliminar_pelicula(clave)
    try:
        assert ok and not db.existe_pelicula(clave)
        print("Eliminar: superada")
    except AssertionError:
        print("Falló al eliminar película")


if __name__ == "__main__":
    # Ejecutar todas las pruebas
    prueba_validar_titulo()
    prueba_validar_año()
    prueba_validar_genero()
    prueba_database_crud()
