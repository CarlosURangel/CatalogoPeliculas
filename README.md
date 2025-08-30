
# Gestor de Películas (Consola)

App de consola con **validaciones robustas**, **operaciones CRUD**, **pruebas unitarias**, **manejo de errores** e **interfaz amigable** basada en menú.

## Estructura
- `config.py`: rangos y mensajes de error centralizados.
- `validaciones.py`: funciones de validación que lanzan `ValueError`.
- `database.py`: "base de datos" en memoria y funciones CRUD.
- `interfaz.py`: interacción por consola (entrada validada, menú, mensajes).
- `main.py`: punto de entrada, bucle principal del menú.
- `test.py`: pruebas unitarias con `unittest` para validaciones y CRUD.

## Requisitos
- Python 3.9+ (cualquier 3.x moderno funciona).

## Ejecutar
```bash
python main.py
```

## Pruebas
```bash
python -m unittest -v
```

## Notas de diseño
- **Validaciones**: todos los campos se validan con `validaciones.py` antes de crear/actualizar.
- **Errores**: se manejan con `try/except` y mensajes claros.
- **CRUD**: se usa `database.py` como almacén en memoria. Las claves son títulos en minúsculas.
- **Interfaz**: menú simple y accesible, con totales y estadísticas rápidas.
