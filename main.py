import csv


# == TAREA: INTEGRANTE A (Arquitecto de Datos)

def cargar_datos_csv(nombre_archivo):
    pass

def buscar_pais(lista_paises):
    pass

def filtrar_paises(lista_paises):
    pass

# HELPERS



# == TAREA: INTEGRANTE B (Analista de Datos)

def agregar_pais(lista_paises):
    pass

def actualizar_pais(lista_paises):
    pass

def ordenar_paises(lista_paises):
    pass

def mostrar_estadisticas(lista_paises):
    pass


# == TAREA: INTEGRANTE A (Arquitecto de Datos)
def mostrar_menu():
    print("--- DATOS DE PAÍSES ---")
    print("1. Agregar país")
    print("2. Actualizar datos de país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países (por continente, población, superficie)")
    print("5. Ordenar países (por continente, población, superficie)")
    print("6. Mostrar estadísticas")
    print("7. Salir")

    return input ("Seleccione una opción (1-7): ").strip()

def main ():

    archivo_csv = "archivo-paises.csv"

    mis_paises = cargar_datos_csv(archivo_csv)

    if not mis_paises:
        print(f"Error. No se pudieron cargar los datos desde {archivo_csv}.")
        return
    
    while True:
        opcion = mostrar_menu()

        match opcion:
            case "1":
                agregar_pais(mis_paises)
            case "2":
                actualizar_pais(mis_paises)
            case "3":
                buscar_pais(mis_paises)
            case "4":
                filtrar_paises(mis_paises)
            case "5":
                ordenar_paises(mis_paises)
            case "6":
                mostrar_estadisticas(mis_paises)
            case "7":
                print("Gracias por usar el programa!")
                break
            case _:
                print("Opción inválida. Vuelva a intentarlo.")


if __name__ == "__main__":
    main()