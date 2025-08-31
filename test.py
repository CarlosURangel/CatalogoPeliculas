
import unittest
import types
import database as db
import validaciones as v
import config

class TestValidaciones(unittest.TestCase):
    def test_titulo_ok(self):
        self.assertEqual(v.validar_titulo("  Matrix "), "Matrix")

    def test_titulo_vacio(self):
        with self.assertRaises(ValueError):
            v.validar_titulo("   ")

    def test_anio_ok(self):
        self.assertEqual(v.validar_anio(config.anio_minimo), config.anio_minimo)
        self.assertEqual(v.validar_anio(config.anio_maximo), config.anio_maximo)

    def test_anio_tipo(self):
        with self.assertRaises(ValueError):
            v.validar_anio("2000")  # no int

    def test_anio_fuera_rango(self):
        with self.assertRaises(ValueError):
            v.validar_anio(config.anio_minimo - 1)

    def test_rating_ok(self):
        self.assertEqual(v.validar_rating(5), 5)
        self.assertEqual(v.validar_rating(7.5), 7.5)

    def test_rating_tipo(self):
        with self.assertRaises(ValueError):
            v.validar_rating("10")

    def test_rating_fuera_rango(self):
        with self.assertRaises(ValueError):
            v.validar_rating(config.rating_maximo + 0.1)

    def test_genero_vacio(self):
        with self.assertRaises(ValueError):
            v.validar_genero("   ")

    def test_director_vacio(self):
        with self.assertRaises(ValueError):
            v.validar_director("   ")

    def test_duracion_ok(self):
        self.assertEqual(v.validar_duracion(config.duracion_minima), config.duracion_minima)
        self.assertEqual(v.validar_duracion(config.duracion_maxima), config.duracion_maxima)

    def test_duracion_tipo(self):
        with self.assertRaises(ValueError):
            v.validar_duracion("120")

    def test_duracion_fuera_rango(self):
        with self.assertRaises(ValueError):
            v.validar_duracion(config.duracion_maxima + 1)

class TestCRUD(unittest.TestCase):
    def setUp(self):
        # Copia profunda del estado original
        self._backup = dict(db.peliculas_database)

    def tearDown(self):
        # Restaurar estado original
        db.peliculas_database.clear()
        db.peliculas_database.update(self._backup)

    def test_agregar_y_buscar(self):
        datos = {
            "titulo": "Interstellar",
            "anio": 2014,
            "genero": "Ciencia Ficción",
            "rating": 8.6,
            "director": "Christopher Nolan",
            "duracion": 169,
        }
        ok, _ = db.agregar_pelicula("interstellar", datos)
        self.assertTrue(ok)
        peli = db.buscar_pelicula("interstellar")
        self.assertIsNotNone(peli)
        self.assertEqual(peli["titulo"], "Interstellar")

    def test_agregar_existente(self):
        # Usa una clave conocida del dataset por defecto
        ok, msg = db.agregar_pelicula("matrix", {"titulo": "X", "anio": 2000, "genero": "X", "rating": 5, "director": "X", "duracion": 100})
        self.assertFalse(ok)
        self.assertIn("ya está registrada", msg)

    def test_eliminar(self):
        ok, _ = db.eliminar_pelicula("parasite")
        self.assertTrue(ok)
        self.assertIsNone(db.buscar_pelicula("parasite"))

    def test_actualizar(self):
        ok, _ = db.actualizar_pelicula("inception", {"rating": 9.1})
        self.assertTrue(ok)
        self.assertEqual(db.buscar_pelicula("inception")["rating"], 9.1)

    def test_total(self):
        total_inicial = db.total_peliculas()
        ok, _ = db.agregar_pelicula("up", {"titulo": "Up", "anio": 2009, "genero": "Animación", "rating": 8.2, "director": "Pete Docter", "duracion": 96})
        self.assertTrue(ok)
        self.assertEqual(db.total_peliculas(), total_inicial + 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
