"""
PROGRAMA PRINCIPAL - SISTEMA DE GESTIÓN DE PELÍCULAS
"""
import interfaz


def main():
    """Función principal del programa"""
    print("Bienvenido al Sistema de Gestion de Peliculas")

    while True:
        try:
            interfaz.mostrar_menu_principal()
            opcion = input("\nSeleccione una opcion (1-8): ").strip()

            if opcion == "1":
                interfaz.menu_agregar_pelicula()
            elif opcion == "2":
                interfaz.menu_eliminar_pelicula()
            elif opcion == "3":
                interfaz.menu_buscar_pelicula()
            elif opcion == "4":
                interfaz.menu_listar_peliculas()
            elif opcion == "5":
                interfaz.menu_actualizar_pelicula()
            elif opcion == "6":
                interfaz.mostrar_generos_peliculas()
            elif opcion == "7":
                interfaz.mostrar_estadisticas()
            elif opcion == "8":
                print("\nGracias por usar el Sistema de Gestion de Peliculas. Hasta pronto!")
                break
            else:
                print("Opcion no valida. Por favor, elija 1-8.")

            input("\nPresione Enter para continuar...")
            interfaz.limpiar_pantalla()

        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario. Hasta pronto!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("Presione Enter para continuar...")
            interfaz.limpiar_pantalla()


if __name__ == "__main__":
    main()