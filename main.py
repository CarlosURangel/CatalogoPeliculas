
"""
main.py
Punto de entrada de la aplicación de consola.
"""
import sys
import interfaz

ACCIONES = {
    "1": interfaz.listar_todas,
    "2": interfaz.buscar_por_nombre,
    "3": interfaz.agregar,
    "4": interfaz.actualizar,
    "5": interfaz.eliminar,
    "6": interfaz.estadisticas,
}

def run() -> None:
    while True:
        interfaz.mostrar_menu()
        opcion = interfaz.pedir_opcion()
        if opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        accion = ACCIONES.get(opcion)
        if accion:
            accion()
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        sys.exit(0)
